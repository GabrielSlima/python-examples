import pytest
from setup_function import Request

def test_request_attributes():
    request = Request()
    print(request.getConfig())
    assert 2 == 2

