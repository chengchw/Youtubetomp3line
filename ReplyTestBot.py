from email.mime import audio
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, AudioSendMessage, StickerMessage, StickerSendMessage
import json

# from EADClass import EADClass

app = Flask(__name__)

print('run robot')
line_bot_api = LineBotApi(
    'Zp9TmuWJhUo2NvJn441XY1WGi5aJro1zQlfbxjHohqIMwG3oQsYvJqECgJ0SL6t/gdFyGlns6oHQA8KNgVoIhw7LHBLnRRqCZIjGVu82+ZieZup7bR6zQBFio0fBJnHZ/kGmJ3KoOB+8zPIDw32pcQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f771b1bcca9fd09a9967fed403625d1a')


@app.route('/')
def hello():
    return 'Hello World!, Welcome'


@app.route('/callback', methods=['POST'])
def callbalck():
    signature = request.headers['x-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body:' + body)

    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handler_message(event):

    print(event)
    print(event.message.text)

    audio_url = event.message.text
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="https://drive.google.com/file/d/16e63t8May5FI3kFKOTRNpZhChseqQSfc/view?usp=sharing"))
    # event.reply_token, AudioSendMessage(original_content_url="https://drive.google.com/file/d/16e63t8May5FI3kFKOTRNpZhChseqQSfc/view?usp=sharing"))

    # extracter = EADClass(audio_url)

    # print(event.source.user_id)
    # user = event.source.user_id

    # audio = extracter.extract_audio()
    # print(audio.title)
    # audio_object = AudioSendMessage(
    #     original_content_url='', duration=5000000)
    # audio_object = AudioSendMessage(
    #     original_content_url='https://62db-2600-8800-1c83-2700-44d1-408e-b4c0-3371.ngrok.io/Be%20Thou%20My%20Vision%20-%20Audrey%20Assad.m4a', duration=300000)
    # # print(audio_object)
    # line_bot_api.push_message(user, audio_url)

    # try:
    #     line_bot_api.reply_message(event.reply_token,
    #                                AudioSendMessage(originalContentUrl=audio))
    #     print('good')
    # except:
    #     print('fail')
# app.run(port=8000)

# Sticker Message


@handler.add(MessageEvent, message=StickerMessage)
def handler_message(event):

    print(event)
    # print(event.message.text)
    replySticker = StickerSendMessage(

        package_id="446",
        sticker_id="1988"
    )

    message = {
        "type": "text",
        "text": "這裡是要回應的文字"
    }
    sticker = {
        "type": "sticker",
        "packageId": "446",
        "stickerId": "1988"
    }
    message_arr = [message, sticker]
    message_json = json.dumps(message)

    #audio_url = event.message.text
    line_bot_api.reply_message(
        event.reply_token, message_arr)


if __name__ == '__main__':
    print('start')
    app.run(port=8000, debug=True)
