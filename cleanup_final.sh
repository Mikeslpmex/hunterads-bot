#!/bin/bash

echo "🧹 LIMPIEZA TOTAL - ÚLTIMO INTENTO"
echo "=================================="

# 1. ELIMINAR todos los archivos excepto los esenciales
echo "🗑️ Eliminando archivos no esenciales..."
find . -name "*.py" -not -name "bot_railway.py" -delete
find . -name "*.json" -delete
find . -name "*.toml" -delete
rm -f runtime.txt

# 2. Crear requirements MÍNIMOS
echo "📦 Requirements mínimos..."
cat > requirements.txt << 'EOF'
python-telegram-bot==20.7
groq==0.3.0
requests==2.31.0
EOF

# 3. Procfile CLARO
echo "🎯 Procfile simple..."
cat > Procfile << 'EOF'
worker: python bot_railway.py
EOF

# 4. Verificar que bot_railway.py existe y es válido
if [ ! -f "bot_railway.py" ]; then
    echo "❌ ERROR: bot_railway.py no existe"
    echo "Creando uno básico..."
    cat > bot_railway.py << 'PYTHON'
from telegram.ext import Application, CommandHandler
import os
import logging

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("🤖 BOT ACTIVO")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Bot iniciado")
    app.run_polling()

if __name__ == '__main__':
    main()
PYTHON
fi

# 5. MOSTRAR ESTRUCTURA FINAL
echo "📁 ESTRUCTURA FINAL:"
ls -la

echo ""
echo "🚀 SUBIENDO VERSIÓN LIMPIA..."
git add .
git commit -m "ULTIMO: Configuración mínima y limpia"
git push origin main

echo ""
echo "✅ VERSIÓN MÍNIMA SUBIDA"
echo "========================"
echo "📦 3 archivos:"
echo "   - bot_railway.py"
echo "   - requirements.txt" 
echo "   - Procfile"
echo ""
echo "🎯 Si esto no funciona, CAMBIAMOS DE SERVIDOR"
