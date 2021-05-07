from daos.department_dao_impl import DepartmentDAOImpl


class DepartmentService:
    department_dao = DepartmentDAOImpl()

    @classmethod
    def create_department(cls, department):
        return cls.department_dao.create_department(department)

    @classmethod
    def get_department(cls, department_id):
        return cls.department_dao.get_department(department_id)

    @classmethod
    def all_departments(cls):
        return cls.department_dao.all_departments()

    @classmethod
    def update_department(cls, change):
        return cls.department_dao.update_department(change)

    @classmethod
    def delete_department(cls, department_id):
        return cls.department_dao.delete_department(department_id)
