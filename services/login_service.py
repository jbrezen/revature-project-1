from daos.login_dao_impl import LoginDAOImpl


class LoginService:
    login_dao = LoginDAOImpl()

    @classmethod
    def create_login(cls, login):
        return cls.login_dao.create_login(login)

    @classmethod
    def get_login(cls, login_id):
        return cls.login_dao.get_login(login_id)

    @classmethod
    def all_logins(cls):
        return cls.login_dao.all_logins()

    @classmethod
    def update_login(cls, change):
        return cls.login_dao.update_login(change)

    @classmethod
    def delete_login(cls, login_id):
        return cls.login_dao.delete_login(login_id)
