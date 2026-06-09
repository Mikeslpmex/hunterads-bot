#!/usr/bin/env python3

import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask, request

# ==================== CONFIG ====================
load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PORT = int(os.getenv("PORT", 8000))

if not TOKEN:
    logger.critical("❌ TELEGRAM_BOT_TOKEN no está definido")
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN")

# ==================== FLASK ====================
flask_app = Flask(__name__)

# ==================== BOT HANDLERS ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 BOT INICIALIZADO [OK]")

async def afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 AFILIADOS ACTIVOS")

async def productos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛍️ CATÁLOGO ACTIVO")

async def urgente(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚨 MARKETING ACTIVO")

async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ SISTEMA ESTABLE ✅")

async def tesorero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🪙 TESORERO ACTIVO 🪙")

# ==================== MAIN BOT SETUP ====================
def create_application():
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("afiliado", afiliado))
    application.add_handler(CommandHandler("productos", productos))
    application.add_handler(CommandHandler("urgente", urgente))
    application.add_handler(CommandHandler("estado", estado))
    application.add_handler(CommandHandler("tesorero", tesorero))

    return application

# ==================== WEBHOOK ROUTE ====================
@flask_app.post("/webhook")   # ← Esta es la ruta que usará Telegram
async def webhook():
    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, application.bot)
        await application.process_update(update)
        return "OK", 200
    except Exception as e:
        logger.error(f"Error en webhook: {e}")
        return "ERROR", 500

# ==================== INICIO ====================
application = create_application()

if __name__ == "__main__":
    # Para desarrollo local (polling)
    logger.info("🚀 Iniciando en modo local (polling)")
    application.run_polling(drop_pending_updates=True)

# Esto se ejecuta cuando Render usa Gunicorn
else:
    # Configurar webhook al iniciar (solo una vez)
    import asyncio
    async def setup_webhook():
        webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/webhook"
        await application.bot.set_webhook(
            url=webhook_url,
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"]
        )
        logger.info(f"✅ Webhook configurado en: {webhook_url}")

    # Ejecutar setup
    asyncio.run(setup_webhook())
