from abc import ABC, abstractmethod


class RequestDAO(ABC):

    @abstractmethod
    def create_request(self, request):
        pass

    @abstractmethod
    def get_request(self, request_id):
        pass

    @abstractmethod
    def all_requests(self):
        pass

    @abstractmethod
    def update_request(self, change):
        pass

    @abstractmethod
    def delete_request(self, request_id):
        pass
