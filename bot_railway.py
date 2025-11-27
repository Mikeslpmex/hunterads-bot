#!/usr/bin/env python3
import logging
import os
import time
from telegram.ext import Application, CommandHandler

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Leer token desde variable de entorno (no lo guardes en el repo)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID", None)

if not TOKEN:
    logger.critical("TELEGRAM_BOT_TOKEN no está definido en las variables de entorno. Abortando.")
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("🤖 BOT INICIALIZADO ✅")

a...