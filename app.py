#!/usr/bin/env python3
"""
HunterAds Bot - Telegram Bot para gestión de afiliados y tesorero
Soporta webhook (producción) y polling (desarrollo)
"""

import logging
import os
import sys
import json
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask, request

# ==================== IMPORTS DE HANDLERS ====================
from handlers import (
    start, afiliado, productos, urgente, estado, tesorero, error_handler
)

# ==================== CONFIGURACIÓN LOGGING ====================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ==================== VARIABLES DE ENTORNO ====================
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PORT = int(os.getenv("PORT", 8000))
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
WEBHOOK_PATH = "/webhook"

# Validación de token
if not TOKEN:
    logger.critical("❌ TELEGRAM_BOT_TOKEN no está definido en .env")
    sys.exit(1)

logger.info(f"✅ Token cargado correctamente")
logger.info(f"📍 Puerto: {PORT}")
if RENDER_EXTERNAL_HOSTNAME:
    logger.info(f"🌐 Hostname: {RENDER_EXTERNAL_HOSTNAME}")

# ==================== FLASK APP ====================
flask_app = Flask(__name__)

# Variables globales
application = None


# ==================== SETUP DEL BOT ====================
def create_application():
    """Crear y configurar la aplicación del bot"""
    global application
    
    try:
        app = Application.builder().token(TOKEN).build()
        
        # Registrar handlers de comandos
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("afiliado", afiliado))
        app.add_handler(CommandHandler("productos", productos))
        app.add_handler(CommandHandler("urgente", urgente))
        app.add_handler(CommandHandler("estado", estado))
        app.add_handler(CommandHandler("tesorero", tesorero))
        
        # Error handler
        app.add_error_handler(error_handler)
        
        logger.info("✅ Aplicación del bot configurada correctamente")
        return app
        
    except Exception as e:
        logger.error(f"❌ Error al crear la aplicación: {e}")
        raise


# ==================== WEBHOOK ENDPOINT ====================
@flask_app.post(WEBHOOK_PATH)
async def webhook_handler():
    """Endpoint webhook para Telegram"""
    try:
        data = request.get_json(force=True)
        
        logger.debug(f"📥 Webhook recibido")
        
        if not application:
            logger.error("❌ Application no inicializada")
            return {"ok": False, "error": "App not initialized"}, 500
        
        # Procesar update
        update = Update.de_json(data, application.bot)
        await application.process_update(update)
        
        logger.debug("✅ Update procesado correctamente")
        return {"ok": True}, 200
        
    except Exception as e:
        logger.error(f"❌ Error en webhook: {e}", exc_info=True)
        return {"ok": False, "error": str(e)}, 500


# ==================== HEALTH CHECK ====================
@flask_app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "bot": "running"}, 200


# ==================== SETUP WEBHOOK ====================
async def setup_webhook():
    """Configurar webhook en Telegram"""
    try:
        if not RENDER_EXTERNAL_HOSTNAME:
            logger.warning("⚠️ RENDER_EXTERNAL_HOSTNAME no configurado, webhook deshabilitado")
            return False
        
        webhook_url = f"https://{RENDER_EXTERNAL_HOSTNAME}{WEBHOOK_PATH}"
        
        logger.info(f"🔗 Configurando webhook en: {webhook_url}")
        
        await application.bot.set_webhook(
            url=webhook_url,
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"]
        )
        
        # Verificar webhook
        webhook_info = await application.bot.get_webhook_info()
        logger.info(f"✅ Webhook configurado correctamente")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error al configurar webhook: {e}")
        return False


# ==================== PUNTO DE ENTRADA ====================
if __name__ == "__main__":
    # Modo desarrollo: polling
    logger.info("🚀 Iniciando en modo DESARROLLO (polling)")
    application = create_application()
    application.run_polling(drop_pending_updates=True)

else:
    # Modo producción: webhook (gunicorn)
    logger.info("🚀 Iniciando en modo PRODUCCIÓN (webhook)")
    
    import asyncio
    
    # Inicializar aplicación
    application = create_application()
    
    # Configurar webhook
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(setup_webhook())
        loop.close()
        logger.info("✅ Bot HunterAds listo en modo producción")
    except Exception as e:
        logger.error(f"❌ Error durante la inicialización: {e}")
