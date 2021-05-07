from daos.employee_dao_impl import EmployeeDAOImpl


class EmployeeService:
    employee_dao = EmployeeDAOImpl()

    @classmethod
    def create_employee(cls, employee):
        return cls.employee_dao.create_employee(employee)

    @classmethod
    def get_employee(cls, employee_id):
        return cls.employee_dao.get_employee(employee_id)

    @classmethod
    def all_employees(cls):
        return cls.employee_dao.all_employees()

    @classmethod
    def update_employee(cls, change):
        return cls.employee_dao.update_employee(change)

    @classmethod
    def delete_employee(cls, employee_id):
        return cls.employee_dao.delete_employee(employee_id)
