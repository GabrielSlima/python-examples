from src.aspects.loggers.logger_service import LoggerService
from flask import request

_logger = LoggerService()


def stream_conversion_process(converter):
    def _converter(*args, **kwargs):
        _logger.log("Converting {}".format("{} bytes".format(len(request.data))), "info")
        video = converter(*args, **kwargs)
        _logger.log("{} converted to Gif".format("{} bytes".format(len(request.data))), "info")
        return video
    return _converter
