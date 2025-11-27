#!/bin/bash

echo "🚨 REPARANDO ERROR DE BUILD EN RAILWAY"
echo "======================================="

# 1. Eliminar archivos problemáticos
echo "🗑️ Limpiando configuraciones anteriores..."
rm -f railway.json
rm -f railway.toml
rm -f nixpacks.toml

# 2. Crear configuración compatible con Nixpacks
echo "🔧 Creando railway.toml compatible..."
cat > railway.toml << 'EOF'
[build]
builder = "nixpacks"

[deploy]
startCommand = "python bot_railway.py"
restartPolicyType = "ON_FAILURE"
EOF

# 3. Crear nixpacks.toml específico
echo "🐍 Configurando entorno Python..."
cat > nixpacks.toml << 'EOF'
[phases.setup]
cmds = [
    "python --version",
    "pip install --upgrade pip"
]

[phases.install]
cmds = ["pip install -r requirements.txt"]

[start]
cmd = "python bot_railway.py"
EOF

# 4. Asegurar requirements.txt exactos
echo "📦 Configurando requirements exactos..."
cat > requirements.txt << 'EOF'
python-telegram-bot==20.7
groq==0.3.0
requests==2.31.0
EOF

# 5. Asegurar Procfile simple
echo "🎯 Configurando Procfile..."
cat > Procfile << 'EOF'
web: python bot_railway.py
EOF

# 6. Verificar que bot_railway.py existe
if [ ! -f "bot_railway.py" ]; then
    echo "❌ bot_railway.py no existe - creando básico..."
    cat > bot_railway.py << 'PYTHON'
from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
async def start(update, context):
    await update.message.reply_text("🤖 Bot funcionando en Railway ✅")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
PYTHON
fi

echo "📁 Estructura final:"
ls -la *.py *.toml *.txt Procfile 2>/dev/null

echo "🚀 Subiendo solución definitiva..."
git add .
git commit -m "FIX: Configuración Nixpacks compatible - Build estable"
git push origin main

echo ""
echo "✅ SOLUCIÓN APLICADA"
echo "===================="
echo "🔧 railway.toml con Nixpacks"
echo "🐍 nixpacks.toml específico"
echo "📦 requirements.txt exactos"
echo "🎯 Procfile simple"
echo ""
echo "🚀 Railway ahora usará Nixpacks y funcionará"
