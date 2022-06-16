from src.app_modules.employees import employees_dao


def save_employees(employee_obj):
    return employees_dao.save_employees(employee_obj)


def get_employee_byid(employee_obj):
    return employees_dao.get_employee_byid(employee_obj)


def get_employees():
    return employees_dao.get_employees()
