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
    """
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
                MessageAction(label='按了就會輸出我設定的話', text='開始'),#幫用戶說一段指定訊息
                MessageAction(
                    label='金牛座',
                    text='金牛座'
                )
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.push_message(user_id, template_message)

        buttons_template = ButtonsTemplate(
            title='Button Template2', text='下面有不同功能的button', actions=[
                MessageAction(
                    label='巨蟹座',
                    text='巨蟹座'
                ),
                MessageAction(
                    label='獅子座',
                    text='獅子座'
                ),
                MessageAction(
                    label='處女座',
                    text='處女座'
                ),
                MessageAction(
                    label='金牛座',
                    text='金牛座'
                )
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.push_message(user_id, template_message)
        """
    if text == "開始":
        
        buttons_template = ButtonsTemplate(
            title='魔法師咒語', text='請選擇星座(這裡是水象星座)', actions=[
                MessageAction(
                    label='雙魚座',
                    text='雙魚座'
                ),
                MessageAction(
                    label='巨蟹座',
                    text='巨蟹座'
                ),
                MessageAction(
                    label='天蠍座',
                    text='天蠍座'

                )
            ])
        template_message = TemplateSendMessage(
            alt_text='請到手機版確認魔法師的箴言喔！', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.push_message(user_id, template_message)

        buttons_template = ButtonsTemplate(
            title='魔法師咒語', text='請選擇星座(這裡是火象星座)', actions=[
                MessageAction(
                    label='牡羊座',
                    text='牡羊座'
                ),
                MessageAction(
                    label='射手座',
                    text='射手座'
                ),
                MessageAction(
                    label='獅子座',
                    text='獅子座'

                )
            ])
        template_message = TemplateSendMessage(
            alt_text='請到手機版確認魔法師的箴言喔！', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.push_message(user_id, template_message)

        buttons_template = ButtonsTemplate(
            title='魔法師咒語', text='請選擇星座(這裡是風象星座)', actions=[
                MessageAction(
                    label='天秤座',
                    text='天秤座'
                ),
                MessageAction(
                    label='雙子座',
                    text='雙子座'
                ),
                MessageAction(
                    label='水瓶座',
                    text='水瓶座'
                )
            ])
        template_message = TemplateSendMessage(
            alt_text='請到手機版確認魔法師的箴言喔！', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.push_message(user_id, template_message)

        buttons_template = ButtonsTemplate(
            title='魔法師咒語', text='請選擇星座(這裡是土象星座)', actions=[
                MessageAction(
                    label='處女座',
                    text='處女座'
                ),
                MessageAction(
                    label='摩羯座',
                    text='摩羯座'
                ),
                MessageAction(
                    label='金牛座',
                    text='金牛座'
                )
            ])
        template_message = TemplateSendMessage(
            alt_text='請到手機版確認魔法師的箴言喔！', template=buttons_template) #alt_text為無法輸出時產生的字樣
        line_bot_api.push_message(user_id, template_message)


    elif text == "天蠍座":
        website_address = "https://astro.click108.com.tw/daily_7.php?iAstro=7#lucky"
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "水瓶座":
        website_address = "https://astro.click108.com.tw/daily_10.php?iAstro=10&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "雙魚座":
        website_address = "https://astro.click108.com.tw/daily_11.php?iAstro=11&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "牡羊座":
        website_address = "https://astro.click108.com.tw/daily_0.php?iAstro=0&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "金牛座":
        website_address = "https://astro.click108.com.tw/daily_1.php?iAstro=1&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "雙子座":
        website_address = "https://astro.click108.com.tw/daily_2.php?iAstro=2&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "巨蟹座":
        website_address = "https://astro.click108.com.tw/daily_3.php?iAstro=3&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "獅子座":
        website_address = "https://astro.click108.com.tw/daily_4.php?iAstro=4&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "處女座":
        website_address = "https://astro.click108.com.tw/daily_5.php?iAstro=5&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "天秤座":
        website_address = "https://astro.click108.com.tw/daily_6.php?iAstro=6&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "射手座":
        website_address = "https://astro.click108.com.tw/daily_8.php?iAstro=8&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)

    elif text == "摩羯座":
        website_address = "https://astro.click108.com.tw/daily_9.php?iAstro=9&Type=0&iAcDay=" + time.strftime('%Y-%m-%d+1', time.localtime())
        dic_constellation = crawl(website_address)
                
        message = TextSendMessage(text="今天財運描述: \n"+dic_constellation["fortune_descri"])
        line_bot_api.push_message(user_id, message)

        if int(dic_constellation["fortune_index"]) >= 3:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天您適合投資喔！想繼續看下去的話，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
        if int(dic_constellation["fortune_index"]) <= 2:
            message = TextSendMessage(text="今天財運指數: \n"+dic_constellation["fortune_index"]+"顆🌟" + "今天的運勢不太適合投資呢，若仍想繼續看下去，請打：財運滾滾來")
            line_bot_api.push_message(user_id, message)
    
    elif text == "財運滾滾來":
            message = TextSendMessage(text="請輸入您的風險承受度，如：風險高 / 如：風險中 / 如：風險低，讓魔法師給你最佳投資建議")
            line_bot_api.push_message(user_id, message)

    elif text == "結束":
        pass

    else:
        buttons_template = ButtonsTemplate(
            title='魔法師的小幫手', text='您可能輸入錯誤了，請重新選擇', actions=[
                MessageAction(label='想輸入投資風險跟預算', text='財運滾滾來'),#幫用戶說一段指定訊息
                MessageAction(label='今天問夠了，魔法師請休息', text='結束'),#幫用戶說一段指定訊息
                MessageAction(label='想要輸入星座再玩一次', text='開始')#幫用戶說一段指定訊息
            ])
        template_message = TemplateSendMessage(
            alt_text='請到手機版確認魔法師的箴言喔！', template=buttons_template) #alt_text為無法輸出時產生的字樣
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
