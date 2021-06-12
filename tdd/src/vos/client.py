from src.vos.abstract import AbstractVo


class Client(AbstractVo):
    def __init__(self, **client):
        self.__dict__.update(client)
