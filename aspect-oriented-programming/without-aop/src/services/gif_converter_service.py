class GifConverterService:
    def __init__(self, ip_address, converter, quota_service):
        self.ip_address = ip_address
        self.quota_service = quota_service
        self.converter = converter

    def convert_from(self, video):
        self.converter.save(video)
        return self.converter.convert_from(video)