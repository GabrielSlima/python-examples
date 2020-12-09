import os


class Request:
    set_up = lambda env_variable_name : "http://localhost" if env_variable_name not in os.environ else env_variable_name
    
    _CONFIG = {
        "URI": set_up('API_ADDRESS')
    }

    def __init__(self):
        print(self._CONFIG)

request = Request()