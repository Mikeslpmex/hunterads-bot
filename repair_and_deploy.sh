#!/bin/bash
# ============================================
# Ritual Orion: Revisión y Reparación del Bot
# ============================================

echo "🔍 Verificando estado de Git..."
git status

# Si hay archivos eliminados, los añadimos al commit
echo "📦 Purificando cambios en Git..."
git add -u
git commit -m "FIX: Reparación ceremonial - Procfile y dependencias validadas" || echo "⚠️ No hay cambios que confirmar"

echo "🚀 Empujando cambios a GitHub..."
git push origin main

# Validar Procfile
echo "📑 Validando Procfile..."
if grep -q "bot_railway.py" Procfile; then
  echo "✅ Procfile apunta a bot_railway.py"
elif grep -q "bot_railway_backup.py" Procfile; then
  echo "✅ Procfile apunta a bot_railway_backup.py"
else
  echo "⚠️ Procfile no apunta a ningún bot válido. Corrigiendo..."
  echo "worker: python bot_railway.py" > Procfile
fi

# Validar requirements.txt
echo "📦 Validando requirements.txt..."
REQUIRED_PKGS=("httpx" "python-dotenv" "python-telegram-bot")
for pkg in "${REQUIRED_PKGS[@]}"; do
  if ! grep -q "$pkg" requirements.txt; then
    echo "$pkg" >> requirements.txt
    echo "➕ Añadido $pkg a requirements.txt"
  fi
done

# Railway login si es necesario
echo "🔐 Verificando sesión en Railway..."
railway whoami || railway login

# Vincular proyecto si no está ligado
echo "🔗 Vinculando proyecto Railway..."
railway link || echo "✅ Proyecto ya vinculado"

# Desplegar
echo "🚀 Desplegando en Railway..."
railway up

# Ver logs
echo "📜 Últimos logs del bot:"
railway logs --tail 10
