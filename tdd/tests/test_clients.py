from src.exceptions.client_exception import ClientException
import clients


def test_should_raise_exception_if_the_client_already_exists():
    client = {
        "name": "Gabriel",
        "email": "gabriel@email.com"
    }
    try:
        clients.save(client)
        assert False
    except ClientException:
        assert True


def test_should_return_null_object_if_client_does_not_exists():
    client = clients.fetch_by("gabriel@non.registered.email.domain.com")
    assert not client.exists()
