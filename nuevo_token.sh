#!/bin/bash

echo "🔑 CREANDO NUEVO BOT Y TOKEN"
echo "============================"

echo "🎯 INSTRUCCIONES:"
echo "1. Abre Telegram y busca @BotFather"
echo "2. Envía: /newbot"
echo "3. Elige nombre para tu bot"
echo "4. Elige username (debe terminar en 'bot')"
echo "5. Copia el NUEVO token que te dé"
echo ""
read -p "📝 Pega el NUEVO token aquí: " NUEVO_TOKEN

if [ -z "$NUEVO_TOKEN" ]; then
    echo "❌ No se ingresó token"
    exit 1
fi

# Crear bot con nuevo token
cat > bot_railway.py << 'BOT'
#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
import logging

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# NUEVO TOKEN
TOKEN = "$NUEVO_TOKEN"

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
BOT

# Reemplazar el token en el archivo
sed -i "s/\\$NUEVO_TOKEN/$NUEVO_TOKEN/g" bot_railway.py

echo "🚀 Subiendo nuevo token..."
git add .
git commit -m "NEW: Token recreado - Bot nuevo"
git push origin main

echo ""
echo "✅ NUEVO TOKEN CONFIGURADO"
echo "=========================="
echo "🔑 Token actualizado en código"
echo "⚙️ También configura en Railway Variables:"
echo "   TELEGRAM_BOT_TOKEN = $NUEVO_TOKEN"
echo "🚀 Deploy en 2-3 minutos..."
echo ""
echo "📱 Busca tu nuevo bot en Telegram con el username que elegiste"
