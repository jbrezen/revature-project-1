from daos.request_dao_impl import RequestDAOImpl


class RequestService:
    request_dao = RequestDAOImpl()

    @classmethod
    def create_request(cls, request):
        return cls.request_dao.create_request(request)

    @classmethod
    def get_request(cls, request_id):
        return cls.request_dao.get_request(request_id)

    @classmethod
    def all_requests(cls):
        return cls.request_dao.all_requests()

    @classmethod
    def join_requests_employees(cls):
        return cls.request_dao.join_requests_employees()

    @classmethod
    def join_requests_depts(cls):
        return cls.request_dao.join_requests_depts()

    @classmethod
    def update_request(cls, change):
        return cls.request_dao.update_request(change)

    @classmethod
    def delete_request(cls, request_id):
        return cls.request_dao.delete_request(request_id)
