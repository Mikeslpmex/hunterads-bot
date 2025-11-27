import os
import logging
from telegram.ext import Application, CommandHandler
from handlers.handlers import handlerhunter

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("❌ Configura TELEGRAM_BOT_TOKEN en Railway")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("hunter", handlerhunter))
    
    print("🚀 Bot iniciado!")
    application.run_polling()

if __name__ == "__main__":
    main()
