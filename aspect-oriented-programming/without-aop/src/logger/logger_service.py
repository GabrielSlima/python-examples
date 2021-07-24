import logging


class LoggerService:
    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)

    def log(self, message, level):
        loggers_by_level = {
            "info": logging.info,
            "debug": logging.debug,
            "critical": logging.critical,
            "error": logging.error
        }
        _logger = loggers_by_level.get(level)
        if not _logger:
            raise Exception("Level Not Found for => {}".format(level))

        _logger(message)
