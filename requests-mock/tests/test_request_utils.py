import pytest
import json 
import request_utils


def test_request_should_return_valid_response(requests_mock):
    uri = 'https://portfolio-gabrielslima.herokuapp.com/'
    requests_mock.real_http = True
    requests_mock.get(uri, json = {"healthcheck": "OK"})
    
    response = json.loads(request_utils.get(uri).content.decode('UTF-8'))

    assert {"healthcheck": "OK"} == response
