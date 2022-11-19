from pytube import YouTube
import pafy
import os


#inputvid = input('What Youtube song would you like to download?\n')
video_url = 'https://www.youtube.com/watch?v=Jbe7OruLk8I'
#try_video = YouTube('https://www.youtube.com/watch?v=Jbe7OruLk8I')
download_dest = 'C:\\Project\\YoutubeToMP3\\Download\\'
stream = pafy.new(video_url)
print(stream.videoid)
stream_audio = stream.getbestaudio('m4a')
audio_id = stream.videoid
audio_title = stream.title
old_name = download_dest + audio_title + 'm4a'
new_name = download_dest + audio_id + 'm4a'
# stream_audio.download(filepath=download_dest)
os.rename(old_name, new_name)
print(stream.author)
print(stream.title)
print(stream_audio)


# try:
#     video = YouTube(inputvid)
#     music = video.streams.filter(only_audio=True, file_extension='mp4').first()
#     music.download(output_path=download_dest)
#     print('You would like to download {}'.format(video.title))
#     print('Download Success, Thank You!!')
# except:
#     print('Invalid Youtube link Please input valid link')
