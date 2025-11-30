#!/usr/bin/env python3
import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

# Cargar variables desde .env
load_dotenv()

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Variables de entorno
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", None)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")       # ej. https://tu-app.up.railway.app
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")
PORT = int(os.getenv("PORT", "8000"))

if not TOKEN:
    logger.critical("❌ TELEGRAM_BOT_TOKEN no está definido en las variables de entorno. Abortando.")
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN")

# Handlers
async def start(update, context):
    await update.message.reply_text("🤖 BOT INICIALIZADO ✅")

async def afiliado(update, context):
    await update.message.reply_text("🔗 AFILIADOS ACTIVOS")

async def productos(update, context):
    await update.message.reply_text("🛍️ CATÁLOGO ACTIVO")

async def urgente(update, context):
    await update.message.reply_text("🚨 MARKETING ACTIVO")

async def estado(update, context):
    await update.message.reply_text("✅ SISTEMA ESTABLE ✅")

async def tesorero(update, context):
    await update.message.reply_text("🪙 TESORERO ACTIVO 🪙")

# Función para asegurar que el path tenga "/"
def ensure_path(p: str) -> str:
    if not p.startswith("/"):
        p = "/" + p
    return p

def main():
    logger.info("🚀 Iniciando bot...")

    app = Application.builder().token(TOKEN).build()

    # Registrar handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", productos))
    app.add_handler(CommandHandler("urgente", urgente))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("tesorero", tesorero))

    # Modo webhook (Railway) o fallback a polling
    if WEBHOOK_URL:
        path = ensure_path(WEBHOOK_PATH)
        full_webhook = WEBHOOK_URL.rstrip("/") + path
        logger.info(f"✅ Modo WEBHOOK activado en {full_webhook}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            path=path,          # ← parámetro correcto
            url=full_webhook,   # ← parámetro correcto
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"],
            stop_signals=None   # evita errores de señales en Railway
        )
    else:
        logger.info("⚠️ WEBHOOK_URL no definido: usando polling")
        app.run_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"],
            poll_interval=2.0,
            timeout=30,
            stop_signals=None   # evita errores de señales en Railway
        )

if __name__ == "__main__":
    main()
