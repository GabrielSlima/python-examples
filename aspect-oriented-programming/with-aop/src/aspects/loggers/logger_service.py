import logging


class LoggerService:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if not logger.hasHandlers():
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self.logger = logger

    def log(self, message, level):
        loggers_by_level = {
            "info": self.logger.info,
            "debug": self.logger.debug,
            "critical": self.logger.critical,
            "error": self.logger.error,
            "warning": self.logger.warning
        }
        _logger = loggers_by_level.get(level)
        if not _logger:
            raise Exception("Level Not Found for => {}".format(level))

        _logger(message)
