from flask import Flask
import os
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is Running!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Start Flask in a separate thread
Thread(target=run_flask).start()

# Your Telegram bot code starts here
from telegram.ext import Updater
updater = Updater("YOUR_BOT_TOKEN", use_context=True)
updater.start_polling()
updater.idle()
