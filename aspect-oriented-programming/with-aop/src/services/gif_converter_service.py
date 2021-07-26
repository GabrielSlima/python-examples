from src.aspects.loggers.converter import log_stream_conversion_process


class GifConverterService:
    def __init__(self, ip_address, converter, quota_service):
        self.ip_address = ip_address
        self.quota_service = quota_service
        self.converter = converter

    @log_stream_conversion_process
    def convert_from(self, video):
        self.converter.save(video)
        return self.converter.convert_from(video)
