from src.aspects.loggers.logger_service import LoggerService
from flask import request
from functools import wraps

_logger = LoggerService()


def stream_incoming_request(request_handler):
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
