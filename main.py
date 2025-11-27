import os
import logging
from telegram.ext import Application, CommandHandler
from handlers.handlers import handlerhunter
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")
    
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN no configurado")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("hunter", handlerhunter))
    
    print("🚀 Bot HunterADS iniciado!")
    print(f"📱 Admin ID: {ADMIN_CHAT_ID}")
    application.run_polling()

if __name__ == "__main__":
    main()
