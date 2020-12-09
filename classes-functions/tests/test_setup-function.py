import pytest
from setup_function import Request

def test_request_attributes():
    request = Request()
    request_config = request.getConfig()
    assert 'htpp://localhost' == request_config['URI']

