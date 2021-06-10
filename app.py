from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from crawl_constellation import crawl
import time

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Z9wIs5xSAOaOPM8LoQz0pv/Tw9PoP0Ph2se6h1RlUEB0uSTKoRwBwSIJ0YQZ/9YWAneVWI5XQoAWuL5lkD2UEeuzhvMUlYZy+Re3psIaEyOAvtKPnrBCCp7OwM07CVWYSj1P/06bIRPxtY/Bp3whuAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ef72f810af4eee6fed399eae10ca7c10')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    text=event.message.text
    user_id = event.source.user_id
    if text == "開始":
        temp_text = "請問你的星座"
        message = TextSendMessage(text=temp_text)
        line_bot_api.push_message(user_id, message)  

    elif text == "天蠍座":
        website_address = "https://astro.click108.com.tw/daily_10.php?iAstro=8&iAcDay=" + time.strftime('%Y-%m-%d', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"])
        line_bot_api.push_message(user_id, message)
        
    else:
        buttons_template = ButtonsTemplate(
            title='Button Template', text='下面有不同功能的button', actions=[
                URIAction(label='好看的影片喔^^', uri='https://www.youtube.com/watch?v=072tU1tamd0'),
                PostbackAction(label='Postback', data='這就是postback'),
                MessageAction(label='按了就會輸出我設定的話', text='開始')#幫用戶說一段指定訊息
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.reply_message(event.reply_token, template_message)
        

@handler.add(PostbackEvent)
def handle_message(event):

    text=event.postback.data
    user_id = event.source.user_id

    message = TextSendMessage(text="這是postback的資訊： "+text)
    line_bot_api.push_message(user_id, message) 



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
