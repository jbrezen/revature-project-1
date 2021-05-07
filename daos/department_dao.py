from abc import ABC, abstractmethod


class DepartmentDAO(ABC):

    @abstractmethod
    def create_department(self, department):
        pass

    @abstractmethod
    def get_department(self, department_id):
        pass

    @abstractmethod
    def all_departments(self):
        pass

    @abstractmethod
    def update_department(self, change):
        pass

    @abstractmethod
    def delete_department(self, department_id):
        pass
