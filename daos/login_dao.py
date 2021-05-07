from abc import ABC, abstractmethod


class LoginDAO(ABC):

    @abstractmethod
    def create_login(self, login):
        pass

    @abstractmethod
    def get_login(self, login_id):
        pass

    @abstractmethod
    def all_logins(self):
        pass

    @abstractmethod
    def update_login(self, change):
        pass

    @abstractmethod
    def delete_login(self, login_id):
        pass
