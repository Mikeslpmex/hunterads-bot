#!/bin/bash

echo "🤖 CONFIGURANDO COMO BOT DE TELEGRAM"
echo "===================================="

# 1. Eliminar archivos de web apps que confunden a Railway
echo "🗑️ Eliminando archivos de web apps..."
rm -f app.py main.py flask_app.py wsgi.py

# 2. Crear configuración específica para BOT
echo "🔧 Configurando Railway para bot..."
cat > railway.json << 'EOF'
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python bot_railway.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
EOF

# 3. Procfile como WORKER, no web
echo "🎯 Configurando Procfile como worker..."
cat > Procfile << 'EOF'
worker: python bot_railway.py
EOF

# 4. Requirements SIN Flask
echo "📦 Requirements sin Flask..."
cat > requirements.txt << 'EOF'
python-telegram-bot==20.7
groq==0.4.1
requests==2.31.0
EOF

# 5. Asegurar que bot_railway.py es claro
echo "🤖 Verificando bot_railway.py..."
if grep -q "Flask\|flask\|app.run\|0.0.0.0" bot_railway.py; then
    echo "⚠️  Eliminando código Flask de bot_railway.py"
    grep -v "Flask\|flask\|app.run\|0.0.0.0" bot_railway.py > bot_railway_temp.py
    mv bot_railway_temp.py bot_railway.py
fi

# 6. Agregar comentario claro al inicio del bot
echo "# 🤖 BOT DE TELEGRAM - NO ES UNA WEB APP" > bot_header.txt
echo "# Ejecutar con: python bot_railway.py" >> bot_header.txt
echo "" >> bot_header.txt
cat bot_header.txt bot_railway.py > bot_final.py
mv bot_final.py bot_railway.py
rm bot_header.txt

echo "📁 Estructura final:"
ls -la *.py *.json *.txt Procfile

echo "🚀 Subiendo configuración de BOT..."
git add .
git commit -m "CONFIG: Especificar como BOT Telegram - No web app - Sin Flask"
git push origin main

echo ""
echo "✅ CONFIGURADO COMO BOT"
echo "======================"
echo "🤖 Tipo: Telegram Bot (worker)"
echo "🚫 Eliminado: Flask y web apps"
echo "🎯 Archivo: bot_railway.py"
echo "📋 Railway ahora lo tratará como BOT, no web app"
