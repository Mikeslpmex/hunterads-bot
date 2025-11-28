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

# Variables de entorno
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID", None)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")       # e.g. https://my-app.up.railway.app
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/webhook")  # e.g. /webhook or /tgbot/secret
PORT = int(os.environ.get("PORT", "8000"))

if not TOKEN:
    logger.critical("TELEGRAM_BOT_TOKEN no está definido en las variables de entorno. Abortando.")
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
    await update.message.reply_text("✅ SISTEMA ESTABLE")

async def tesorero(update, context):
    await update.message.reply_text("💰 TESORERO ACTIVO")


def ensure_path(p: str) -> str:
    if not p.startswith("/"):
        p = "/" + p
    return p


def main():
    logger.info("🚀 Iniciando bot (webhook/polling automático)...")

    while True:
        try:
            app = Application.builder().token(TOKEN).build()

            # Registrar handlers
            app.add_handler(CommandHandler("start", start))
            app.add_handler(CommandHandler("afiliado", afiliado))
            app.add_handler(CommandHandler("productos", productos))
            app.add_handler(CommandHandler("urgente", urgente))
            app.add_handler(CommandHandler("estado", estado))
            app.add_handler(CommandHandler("tesorero", tesorero))

            # Si hay WEBHOOK_URL usamos webhook (recomendado en Railway)
            if WEBHOOK_URL:
                path = ensure_path(WEBHOOK_PATH)
                full_webhook = WEBHOOK_URL.rstrip("/") + path
                logger.info(f"✅ Modo WEBHOOK activado. Listening on 0.0.0.0:{PORT}, webhook URL: {full_webhook}")
                # run_webhook abrirá un servidor HTTP interno (aiohttp) y registrará el webhook en Telegram
                app.run_webhook(
                    listen="0.0.0.0",
                    port=PORT,
                    webhook_path=path,
                    webhook_url=full_webhook,
                    drop_pending_updates=True,
                    allowed_updates=["message", "callback_query"]
                )
                # si run_webhook retorna, lo reiniciamos
                logger.warning("run_webhook finalizó; reiniciando en 5 segundos...")
                time.sleep(5)
            else:
                # Fallback a polling si no se proporcionó WEBHOOK_URL
                logger.info("⚠️ WEBHOOK_URL no definido: usando polling (útil solo para pruebas).")
                app.run_polling(
                    drop_pending_updates=True,
                    allowed_updates=["message", "callback_query"],
                    poll_interval=2.0,
                    timeout=30
                )
                logger.warning("run_polling finalizó; reiniciando en 5 segundos...")
                time.sleep(5)

        except Exception as e:
            logger.exception(f"❌ Error crítico en el bot: {e}. Reintentando en 10 segundos...")
            time.sleep(10)

if __name__ == "__main__":
    main()
