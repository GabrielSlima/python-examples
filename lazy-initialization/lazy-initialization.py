from moviepy.editor import VideoFileClip
from datetime import datetime
from flask import Flask
from flask import request
from flask import send_file


app = Flask(__name__)


class GifConverterService:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.quota_service = None
        self.converter = None
    
    def convert_from(self, video):
        if not self.converter:
            self.converter = GifConverter() #Lazy Initialization
        
        self.converter.save(video)
        return self.converter.convert_from(video)


class GifConverter:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d-%H%m%s")
        self.video = '/tmp/video-{}.mp4'.format(self.timestamp)
    
    def convert_from(self, video):        
        __video = VideoFileClip(self.video).subclip(10, 20)
        absolute_path = '/tmp/video-{}.gif'.format(self.timestamp)
        __video.write_gif(absolute_path)
        return absolute_path
    
    def save(self, video):
        with open(self.video, 'wb') as _video_file:
            _video_file.write(video)
            _video_file.close()


@app.route("/gifs", methods=["POST"])
def convert():
    _converter = GifConverterService(request.remote_addr)
    _converter.convert_from(request.data)
    return send_file(
        _converter.convert_from(request.data),
        attachment_filename="video_to_gif.gif"
    )


if __name__ == "__main__":
    app.run()
