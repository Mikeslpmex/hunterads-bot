#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
import logging

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# NUEVO TOKEN
TOKEN = "8285048355:AAGtD1LVGsmP6U4CTUIHgTOujv-fWPOria4"

async def start(update, context):
    await update.message.reply_text(
        "🤖 *BOT RECREADO - TOKEN NUEVO* ✅\\n\\n"
        "🔑 Token: ACTIVO\\n"
        "🚀 Sistema: OPERACIONAL\\n\\n"
        "💎 Usa /afiliado para empezar",
        parse_mode="Markdown"
    )

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
    logger.info("🚀 INICIANDO BOT CON NUEVO TOKEN...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", productos))
    app.add_handler(CommandHandler("urgente", urgente))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("tesorero", tesorero))
    
    logger.info("✅ BOT LISTO CON NUEVO TOKEN")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
