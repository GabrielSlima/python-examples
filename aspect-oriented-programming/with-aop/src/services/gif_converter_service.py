from src.aspects.loggers.converter_logger import stream_conversion_process


class GifConverterService:
    def __init__(self, ip_address, converter, quota_service):
        self.ip_address = ip_address
        self.quota_service = quota_service
        self.converter = converter

    @stream_conversion_process
    def convert_from(self, video):
        self.converter.save(video)
        return self.converter.convert_from(video)
