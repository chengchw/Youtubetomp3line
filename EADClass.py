
# Download music to local folder
#Extract and Download
import pafy
import os

download_dest = 'C:\Project\YoutubeToMP3\Download'


class Extract:

    def __init__(self, url):
        self.url = url
        self.stream = None
        print(url)

    def extract_audio(self):
        try:
            self.stream = pafy.new(self.url)
            audio_id = self.stream.videoid
            audio_title = self.stream.title
            stream_audio = self.stream.getbestaudio('m4a')
            stream_audio.download(filepath=download_dest)
            old_name = download_dest + stream_audio + 'm4a'
            new_name = download_dest + audio_id + 'm4a'
            os.rename(old_name, new_name)
            return stream_audio

        except:
            return None
