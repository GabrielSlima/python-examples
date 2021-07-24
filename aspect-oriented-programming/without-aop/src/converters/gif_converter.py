from moviepy.editor import VideoFileClip
from datetime import datetime


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
