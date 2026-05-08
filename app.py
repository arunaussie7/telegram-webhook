from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8617804848:AAFP0g3mSC26uZ8awiCCtmH_giOE9VG70Xw"
CHAT_ID = "-1003802471292"

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    message = data.get("message", "New Signal")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, json=payload)

    return "ok"

app.run(host="0.0.0.0", port=5000)
