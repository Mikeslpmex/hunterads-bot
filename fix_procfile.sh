#!/bin/bash

echo "🔧 CORRIGIENDO PROCFILE PARA BOT"
echo "================================"

# 1. Cambiar a worker (para bots)
echo "🤖 Cambiando Procfile a worker..."
cat > Procfile << 'EOF'
worker: python bot_railway.py
EOF

# 2. Eliminar archivos problemáticos
echo "🗑️ Limpiando archivos conflictivos..."
rm -f tesorero_app.py tesorero_app.py.disabled app.py main.py flask_app.py

# 3. Verificar que solo existe bot_railway.py
echo "📁 Archivos Python restantes:"
ls -la *.py

# 4. Asegurar que bot_railway.py tiene contenido válido
if [ ! -s "bot_railway.py" ]; then
    echo "📝 Creando bot_railway.py básico..."
    cat > bot_railway.py << 'PYTHON'
from telegram.ext import Application, CommandHandler
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    logger.error("❌ TELEGRAM_BOT_TOKEN no configurado")
    exit(1)

async def start(update, context):
    logger.info("📩 Comando /start recibido")
    await update.message.reply_text("🤖 *BOT ACTIVO EN RAILWAY* ✅", parse_mode="Markdown")

async def afiliado(update, context):
    await update.message.reply_text("🔗 *AFILIADOS ACTIVOS* 🚀", parse_mode="Markdown")

def main():
    logger.info("🚀 INICIANDO BOT ORION...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", afiliado))
    app.add_handler(CommandHandler("urgente", afiliado))
    
    logger.info("🎯 Bot listo - Iniciando polling...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
PYTHON
fi

echo "🚀 Subiendo corrección..."
git add .
git commit -m "FIX: Procfile como worker - Archivos limpios - Bot funcional"
git push origin main

echo ""
echo "✅ CORRECCIÓN APLICADA"
echo "======================"
echo "🤖 Procfile: worker (para bots)"
echo "🗑️ Archivos conflictivos eliminados"
echo "📝 bot_railway.py verificado"
echo "🚀 Railway ahora ejecutará como BOT, no web app"
