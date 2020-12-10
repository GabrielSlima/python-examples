import os
import requests

class RequestUtils:
    
    def set_up(env_variable_name, default_value):
        if env_variable_name in os.environ:
            return os.environ[env_variable_name]
        return default_value
    
    _CONFIG = {
        "URI": set_up('API_ADDRESS', 'https://portfolio-gabrielslima.herokuapp.com/'),
        "CREDENTIALS": {
            'API_KEY': set_up('API_KEY', 'mocked'),
            'APP_SECRET': set_up('APP_SECRET', 'mocked')
        }
    }

    def __init__(self):
        print(self._CONFIG)
    
    def getConfig(self):
        return self._CONFIG

    def sendRequest(self):
        uri = self._CONFIG['URI']
        return requests.get(uri)
