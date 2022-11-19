import EADClass
import ReplyTestBot

if __name__ == '__main__':

    url = input()
    # music_stream = EADClass.Extract(url)
    # music_stream.extract_audio()
    ReplyTestBot.app.run(port=8000)
