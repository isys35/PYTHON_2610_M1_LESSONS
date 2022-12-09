from abc import ABC, abstractmethod


class XMLHttpRequestService:
    pass


class Connection(ABC):
    @abstractmethod
    def request(self, url, options):
        pass


class XMLHttpService(Connection):
    xhr = XMLHttpRequestService()

    def request(self, url, options):
        return self.xhr.request(url, options)


class Http:
    def __init__(self, connection: Connection):
        self.connection = connection

    def get(self, url: str, options: dict):
        self.connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.connection.request(url, 'POST')
