from functools import wraps

import jwt
from flask import current_app
from flask import request

from common import logging_setup
from src.app_modules.employees import employees_service

logger = logging_setup.get_logger()


def check_user_authorized(loggedin_user, grants_required):
    user_role = loggedin_user["role"]
    # For the role identified inside the token, map the access grants
    access_grants = current_app.config["ACCESS_ROLES_MAPPING"][user_role]
    loggedin_user["accessGrants"] = access_grants
    missing_grants = []

    # Each action requires certain specific set of grants,
    # Required grants is listed in a list. [READ:ALL, READ]
    # Check whether the user has all the required access grants.
    for req_grant in grants_required:
        if req_grant not in access_grants:
            missing_grants.append(req_grant)

    if len(missing_grants) > 0:
        logger.error("[ACTION FORBIDDEN], Missing access grants: %s", missing_grants)
        # Status is 403, because even though authenticated, user is not authorized
        return {
                   "message": "Action is not authorized. Missing required access grants",
                   "data": None,
                   "error": "Unauthorized"
               }, 403
    else:
        return loggedin_user, 200


def auth_middleware(required_grants):
    def decorator(func):
        # Wraps the function on which the decorator is applied
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = None
            # Looking for the Authorization as headers
            if "Authorization" in request.headers:
                # The header value starts with `Bearer <token>`, hence extracting the token out of this
                token = request.headers["Authorization"].split(" ")[1]
            # If token is not present send out auth failure, request will end here
            if not token:
                return {
                           "message": "Authentication token is missing!",
                           "data": None,
                           "error": "Unauthorized"
                       }, 401
            try:
                # If the token is available. Decode the JWT token using the secret with which it was created.
                # refer jwt.io to create a token with the secret and appropriate payload
                data = jwt.decode(token, current_app.config["SECRET"], algorithms=["HS256"])
                loggedin_user = {
                    "employeeId": data["empid"],
                    "employeeCode": data["empcode"],
                    "employeeName": data["empname"],
                    "username": data.get("username", None),
                }

                # The code below if skipped will work fine without any authorization
                user = employees_service.get_employee_byid(loggedin_user["employeeId"])

                # Check even the employee status, for is he still working, left etc.
                # Check for the user exists within the system db
                if user is None:
                    return {
                               "message": f"Invalid Authentication token!. User does not exist with Id:{loggedin_user['employeeId']}",
                               "data": None,
                               "error": "Unauthorized"
                           }, 401
                # Best way is look for the role inside the database, where the user data is store.

                # If an external authorization server is used, get the role from there.

                # -------------------- AUTHORIZATION -----------------------------------
                auth_resp, status = check_user_authorized(user, required_grants)
                if status == 403:
                    return auth_resp, status
                # ----------------------- Authorization Ends -------------------------------
            except Exception as execp:
                logger.exception("Authentication failed with error: %s", execp)
            return func(loggedin_user, *args, **kwargs)

        return wrapper

    return decorator
