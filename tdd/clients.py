from src.exceptions.client_exception import ClientException
from src.factories.client import ClientFactory

super_cool_data_base_representation = [
    {
        "name": "Gabriel",
        "email": "gabriel@email.com"
    }
]


def save(client):
    if client in super_cool_data_base_representation:
        raise ClientException("Client already exists!")
    
    super_cool_data_base_representation.append(client)


def fetch_by(email):
    client = {}
    for registered_client in super_cool_data_base_representation:
        if registered_client.get('email') != email:
            continue
        client = registered_client
    return ClientFactory.create(client)
