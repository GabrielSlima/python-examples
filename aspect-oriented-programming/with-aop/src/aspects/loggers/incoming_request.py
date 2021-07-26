from src.aspects.loggers.logger_service import LoggerService
from functools import wraps
from flask import request


def log_stream_incoming_request(request_handler):
    _logger = LoggerService("request")

    @wraps(request_handler)
    def _request_handler(*args, **kwargs):
        _logger.log(
            "Request received from => {} - payload size: {}".format(
                request.remote_addr,
                "{} bytes".format(len(request.data))
            ),
            "info"
        )
        return request_handler(*args, **kwargs)
    return _request_handler
