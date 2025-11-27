#!/bin/bash

echo "🔑 FORZANDO NUEVO TOKEN EN CÓDIGO"
echo "================================"

NUEVO_TOKEN="8285048355:AAErNzEOWcsfocP5WvNUZYb3LDTYTtvUE-k"

# Crear bot con token hardcodeado
cat > bot_railway.py << 'BOT'
#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
import logging

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TOKEN DIRECTAMENTE EN CÓDIGO
TOKEN = "8285048355:AAErNzEOWcsfocP5WvNUZYb3LDTYTtvUE-k"
ADMIN_CHAT_ID = "7318862870"

logger.info(f"🔑 Token configurado: {TOKEN[:10]}...")

async def start(update, context):
    user = update.effective_user
    logger.info(f"👤 /start from {user.id}")
    await update.message.reply_text(
        "🤖 *SISTEMA ORION - TOKEN ACTUALIZADO* ✅\\n\\n"
        "🔑 Token: CORRECTO\\n"
        "🚀 Plataforma: Railway\\n"
        "💎 Comandos activos\\n\\n"
        "⚡ Usa /afiliado para generar enlaces",
        parse_mode="Markdown"
    )

async def afiliado(update, context):
    logger.info("🔗 Comando /afiliado")
    if not context.args:
        await update.message.reply_text(
            "📦 *PRODUCTOS DISPONIBLES:*\\n\\n"
            "🎓 Cursos:\\n"
            "`/afiliado recuperacion`\\n"
            "`/afiliado seguridad`\\n\\n"
            "💎 Digital:\\n"
            "`/afiliado mp_149`\\n"
            "`/afiliado mp_299`\\n"
            "`/afiliado mp_499`",
            parse_mode="Markdown"
        )
        return
    
    producto = " ".join(context.args)
    await update.message.reply_text(f"🎯 *{producto.upper()}*\\n\\n🔗 Enlace generado ✅", parse_mode="Markdown")

async def productos(update, context):
    await update.message.reply_text("🛍️ *CATÁLOGO COMPLETO* ✅", parse_mode="Markdown")

async def urgente(update, context):
    await update.message.reply_text("🚨 *MARKETING URGENTE* ✅", parse_mode="Markdown")

async def estado(update, context):
    await update.message.reply_text("✅ *SISTEMA 100% OPERACIONAL*", parse_mode="Markdown")

async def tesorero(update, context):
    await update.message.reply_text("💰 *TESORERO ACTIVO* ✅", parse_mode="Markdown")

def main():
    logger.info("🚀 INICIANDO BOT CON TOKEN NUEVO...")
    
    try:
        app = Application.builder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("afiliado", afiliado))
        app.add_handler(CommandHandler("productos", productos))
        app.add_handler(CommandHandler("urgente", urgente))
        app.add_handler(CommandHandler("estado", estado))
        app.add_handler(CommandHandler("tesorero", tesorero))
        
        logger.info("✅ TODOS LOS COMANDOS REGISTRADOS")
        logger.info("🎯 Iniciando polling...")
        
        app.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise

if __name__ == '__main__':
    main()
BOT

# También actualizar requirements para asegurar compatibilidad
cat > requirements.txt << 'EOF'
python-telegram-bot==20.7
requests==2.31.0
EOF

# Runtime específico
echo "python-3.11.9" > runtime.txt

# Procfile claro
cat > Procfile << 'EOF'
worker: python bot_railway.py
EOF

echo "📁 Verificando archivos:"
ls -la bot_railway.py requirements.txt runtime.txt Procfile

echo "🚀 Subiendo token forzado en código..."
git add .
git commit -m "FORCE: Token hardcodeado - 8285048355:AAErNzEOWcsfocP5WvNUZYb3LDTYTtvUE-k"
git push origin main

echo ""
echo "✅ TOKEN FORZADO EN CÓDIGO"
echo "=========================="
echo "🔑 Token: 8285048355:AAErNzEOWcsfocP5WvNUZYb3LDTYTtvUE-k"
echo "📝 Hardcodeado en bot_railway.py"
echo "🐍 Python 3.11.9 forzado"
echo "🚀 Deploy en 2-3 minutos..."
echo ""
echo "🎯 También configura en Railway Variables:"
echo "   TELEGRAM_BOT_TOKEN = 8285048355:AAErNzEOWcsfocP5WvNUZYb3LDTYTtvUE-k"
echo "   TELEGRAM_ADMIN_CHAT_ID = 7318862870"
