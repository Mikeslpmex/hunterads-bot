#!/bin/bash

echo "🔑 CONFIGURANDO TOKEN EN CÓDIGO"
echo "================================"

# Actualizar el bot con token por defecto
cat > bot_railway.py << 'BOTFIX'
#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
from telegram import Update
import os
import logging

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Token por defecto - funciona incluso si no hay variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8285048355:AAHTuCMOj5w5Ox2pZ5sUR_ofYmQpPG_jRvw")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "7318862870")

logger.info(f"🔑 Token: {TOKEN[:10]}...")
logger.info(f"👤 Admin: {ADMIN_CHAT_ID}")

async def start(update: Update, context):
    await update.message.reply_text(
        "🤖 *SISTEMA ORION - TOKEN CONFIGURADO* ✅\\n\\n"
        "💎 Comandos: /start /afiliado /productos /urgente /estado /tesorero",
        parse_mode="Markdown"
    )

async def afiliado(update: Update, context):
    if not context.args:
        await update.message.reply_text(
            "📦 *PRODUCTOS:*\\n`/afiliado recuperacion`\\n`/afiliado seguridad`\\n`/afiliado mp_149`",
            parse_mode="Markdown"
        )
        return
    
    producto = " ".join(context.args).lower()
    enlaces = {
        "recuperacion": "🔗 https://pay.hotmart.com/B12345678",
        "seguridad": "🔗 https://pay.hotmart.com/B87654321", 
        "mp_149": "🔗 https://mpago.li/1wbjMgo",
        "mp_299": "🔗 https://mpago.li/1ufHHLw",
        "mp_499": "🔗 https://mpago.li/1yg93jr"
    }
    
    enlace = enlaces.get(producto, "🔗 https://mercadolibre.com")
    await update.message.reply_text(f"🎯 *{producto.upper()}*\\n\\n{enlace}", parse_mode="Markdown")

async def productos(update: Update, context):
    await update.message.reply_text(
        "🛍️ *CATÁLOGO*\\n\\n"
        "🎓 Cursos:\\n`/afiliado recuperacion`\\n`/afiliado seguridad`\\n\\n"
        "💎 Digital:\\n`/afiliado mp_149`\\n`/afiliado mp_299`\\n`/afiliado mp_499`",
        parse_mode="Markdown"
    )

async def urgente(update: Update, context):
    await update.message.reply_text(
        "🚨 *¡OFERTA URGENTE!* 🔥\\n\\n"
        "💥 Curso Recuperación de Cuentas\\n💰 $39.99 | 🎯 $19.99 comisión\\n\\n"
        "🔗 Usa `/afiliado recuperacion`",
        parse_mode="Markdown"
    )

async def estado(update: Update, context):
    await update.message.reply_text("✅ *SISTEMA ACTIVO* 🤖", parse_mode="Markdown")

async def tesorero(update: Update, context):
    await update.message.reply_text("💰 *TESORERO ACTIVO* 🏦", parse_mode="Markdown")

def main():
    logger.info("🚀 INICIANDO BOT CON TOKEN...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", productos))
    app.add_handler(CommandHandler("urgente", urgente))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("tesorero", tesorero))
    
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
BOTFIX

echo "🚀 Subiendo fix del token..."
git add .
git commit -m "FIX: Token por defecto en código - Variables Railway"
git push origin main

echo ""
echo "✅ TOKEN CONFIGURADO"
echo "===================="
echo "🔑 Token incluido en código"
echo "⚙️ También configura en Railway Variables:"
echo "   TELEGRAM_BOT_TOKEN = 8285048355:AAHTuCMOj5w5Ox2pZ5sUR_ofYmQpPG_jRvw"
echo "   TELEGRAM_ADMIN_CHAT_ID = 7318862870"
