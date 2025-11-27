#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Token por defecto
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8285048355:AAHTuCMOj5w5Ox2pZ5sUR_ofYmQpPG_jRvw")

async def start(update, context):
    await update.message.reply_text("🤖 BOT ACTIVO - Python 3.11 ✅")

async def afiliado(update, context):
    await update.message.reply_text("🔗 SISTEMA AFILIADOS ACTIVO")

async def productos(update, context):
    await update.message.reply_text("🛍️ CATÁLOGO ACTIVO")

async def urgente(update, context):
    await update.message.reply_text("🚨 MARKETING ACTIVO")

async def estado(update, context):
    await update.message.reply_text("✅ SISTEMA ESTABLE")

async def tesorero(update, context):
    await update.message.reply_text("💰 TESORERO ACTIVO")

def main():
    logger.info("🚀 INICIANDO BOT PYTHON 3.11...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", productos))
    app.add_handler(CommandHandler("urgente", urgente))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("tesorero", tesorero))
    
    logger.info("✅ BOT LISTO - INICIANDO...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
