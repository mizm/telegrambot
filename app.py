import os
import requests
from flask import Flask,request
app = Flask(__name__)

token = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route(f"/{token}", methods=['POST'])
def telegram():
    #token = os.getenv("TELEGRAM_BOT_TOKEN")
    from_telegram = request.get_json()
    if from_telegram.get('message') is not None:
        chat_id = from_telegram['message']['from']['id']
        text = from_telegram['message']['text']
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '',200
    
    
if __name__ == '__main__' :
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))