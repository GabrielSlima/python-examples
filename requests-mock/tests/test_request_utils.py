import pytest
from request_utils import RequestUtils
import json 


def test_request_should_return_valid_response(requests_mock):
    request = RequestUtils()
    requests_mock.real_http = True
    requests_mock.get('https://portfolio-gabrielslima.herokuapp.com/', json = {"healthcheck": "OK"})
    response = json.loads(request.sendRequest().content.decode('UTF-8'))

    assert {"healthcheck": "OK"} == response
