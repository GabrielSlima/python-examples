from src.logger.logger_service import LoggerService
from src.factories.converter_factory import ConverterFactory
from src.services.quota_service import QuotaService
from src.services.gif_converter_service import GifConverterService
from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)
_logger = LoggerService()


@app.route("/video_to_gif", methods=["POST"])
def convert():
    _logger.log(
        "Request received from => {} - payload size: {}".format(
            request.remote_addr,
            "{} bytes".format(len(request.data))
        ),
        "info"
    )

    _CONVERTER_NAME = "gif_converter"

    _converter = ConverterFactory.create_converter_by(_CONVERTER_NAME)
    _quota_service = QuotaService()

    _converter_service = GifConverterService(
        request.remote_addr,
        _converter,
        _quota_service
    )

    _logger.log("Converting {}".format("{} bytes".format(len(request.data))), "info")
    gif = _converter_service.convert_from(request.data)
    _logger.log("{} converted to Gif".format("{} bytes".format(len(request.data))), "info")
    return send_file(gif, attachment_filename="video_to_gif.gif")


if __name__ == "__main__":
    app.debug = False
    app.run(port=5001)
