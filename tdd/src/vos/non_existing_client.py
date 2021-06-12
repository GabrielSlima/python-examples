from src.vos.abstract import AbstractVo


class NonExistingClient(AbstractVo):
    def __init__(self):
        super().__init__(None, None)
