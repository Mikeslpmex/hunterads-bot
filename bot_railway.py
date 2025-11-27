#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
import logging
import asyncio
import os

# Configuración robusta
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token - con verificación
TOKEN = "8285048355:AAGtD1LVGsmP6U4CTUIHgTOujv-fWPOria4"

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

def main():
    logger.info("🚀 INICIANDO BOT CON INICIALIZACIÓN ROBUSTA...")
    
    try:
        # Crear aplicación con timeout
        app = Application.builder().token(TOKEN).build()
        
        # Registrar handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("afiliado", afiliado))
        app.add_handler(CommandHandler("productos", productos))
        app.add_handler(CommandHandler("urgente", urgente))
        app.add_handler(CommandHandler("estado", estado))
        app.add_handler(CommandHandler("tesorero", tesorero))
        
        logger.info("✅ HANDLERS REGISTRADOS")
        
        # Iniciar polling con manejo de errores
        logger.info("🎯 INICIANDO POLLING...")
        app.run_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"],
            poll_interval=2.0,
            timeout=30
        )
        
    except Exception as e:
        logger.error(f"❌ ERROR CRÍTICO: {e}")
        logger.info("🔄 REINICIANDO EN 10 SEGUNDOS...")
        import time
        time.sleep(10)
        main()

if __name__ == '__main__':
    main()
