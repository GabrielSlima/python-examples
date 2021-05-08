from os import environ
import requests
import logging


def get(uri):
    response = None
    try:
        response = requests.get(uri)
    except Exception as e:
        logging.error(e)
    finally:
        return response
        
