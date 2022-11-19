from hashlib import new
import os
old_name = r"C:\Project\YoutubeToMP3\Download\Be Thou My Vision - Audrey Assad.m4a"
new_name = r"C:\Project\YoutubeToMP3\Download\Try.m4a"

os.rename(old_name, new_name)
