from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Tu bot normal
application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

# ... agrega tus handlers ...

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    # Para polling local
    application.run_polling()
