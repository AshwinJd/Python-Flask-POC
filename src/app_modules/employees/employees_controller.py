from src.app_modules.employees import employees_service


def save_employees(employee_obj):
    response = {
        "status": 201,
        "error": None,
        "result": {}
    }
    response_project = employees_service.save_employees(employee_obj)
    response['result'] = response_project
    return response


def get_employee_byid(employee_obj):
    return employees_service.get_employee_byid(employee_obj)


def get_employees():
    response = {
        "status": 200,
        "error": None,
        "result": {}
    }

    response['result'] = employees_service.get_employees()
    return response
