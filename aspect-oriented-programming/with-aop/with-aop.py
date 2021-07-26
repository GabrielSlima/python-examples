from src.factories.converter_factory import ConverterFactory
from src.services.quota_service import QuotaService
from src.services.gif_converter_service import GifConverterService
from src.aspects.loggers.incoming_request import log_stream_incoming_request
from flask import Flask
from flask import request
from flask import send_file


app = Flask(__name__)


@app.route("/video_to_gif", methods=["POST"])
@log_stream_incoming_request
def convert():
    _CONVERTER_NAME = "gif_converter"
    _converter = ConverterFactory.create_converter_by(_CONVERTER_NAME)
    _quota_service = QuotaService()

    _converter_service = GifConverterService(
        request.remote_addr,
        _converter,
        _quota_service
    )

    gif = _converter_service.convert_from(request.data)
    return send_file(gif, attachment_filename="video_to_gif.gif")


if __name__ == "__main__":
    app.debug = False
    app.run(port=5001)
