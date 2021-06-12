from src.vos.client import Client as ClientVo
from src.vos.non_existing_client import NonExistingClient


class ClientFactory:
    def __init__(self):
        pass
        
    @staticmethod
    def create(client):
        if not client.get('name') and not client.get('email'):
            return NonExistingClient()
        return ClientVo(**client)
