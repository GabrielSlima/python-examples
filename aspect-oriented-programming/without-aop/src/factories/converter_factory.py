from src.converters.gif_converter import GifConverter


class ConverterFactory:
    @staticmethod
    def create_converter_by(name):
        converters = {
            "gif_converter": GifConverter
        }
        converter = converters.get(name)
        if not converter:
            raise Exception("Convert with name {} not Found".format(name))

        return converter

