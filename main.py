import os
import logging
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
from dotenv import load_dotenv

# 🔥 CARGAR VARIABLES DEL .env
load_dotenv()

# ✅ CONFIGURACIÓN
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 **SISTEMA ORION ACTIVADO**\n\n"
        "Comandos disponibles:\n"
        "/start - Iniciar bot\n"
        "/estado - Estado del sistema"
    )

async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    estado_sistema = "✅ **SISTEMA OPERATIVO**\n\n"
    estado_sistema += f"• Bot Token: {'🟢 CONFIGURADO' if TELEGRAM_BOT_TOKEN else '🔴 NO CONFIGURADO'}\n"
    estado_sistema += f"• Chat ID: {ADMIN_CHAT_ID or 'NO CONFIGURADO'}\n"
    estado_sistema += "• Módulo afiliados: 🟢 LISTO\n"
    estado_sistema += "• Tesorero: 🟢 LISTO"
    
    await update.message.reply_text(estado_sistema, parse_mode="Markdown")

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN no configurado en .env")
        return
    
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("estado", estado))
    
    print("🚀 Bot Orion iniciado correctamente!")
    application.run_polling()

if __name__ == "__main__":
    main()
