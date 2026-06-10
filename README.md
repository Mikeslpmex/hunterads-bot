# 🤖 HunterAds Bot - Telegram Bot for Affiliate Marketing

Bot de Telegram especializado en gestión de afiliados, productos y ventas con tesorero integrado.

## 📋 Características

- ✅ Gestión de afiliados
- ✅ Catálogo de productos
- ✅ Tesorero de ventas (comisiones y saldos)
- ✅ Marketing y urgentes
- ✅ Webhook de Telegram (webhooks)
- ✅ Polling para desarrollo local

## 🛠️ Requisitos

- Python 3.10+
- Telegram Bot Token
- Railway/Render (para producción)

## 📦 Instalación

```bash
# Clonar repositorio
git clone https://github.com/Mikeslpmex/hunterads-bot.git
cd hunterads-bot

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# o en Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu TELEGRAM_BOT_TOKEN
```

## 🚀 Uso

### Desarrollo Local (Polling)
```bash
python3 app.py
```

### Producción (Webhook en Railway)
```bash
# El Procfile ejecuta automáticamente:
gunicorn --worker-class aiohttp.worker.GunicornWebWorker app:flask_app
```

## 🔧 Comandos del Bot

| Comando | Descripción |
|---------|------------|
| `/start` | Inicializar bot |
| `/afiliado` | Registrar venta de afiliado |
| `/productos` | Ver catálogo |
| `/urgente` | Marketing urgente |
| `/estado` | Estado del sistema |
| `/tesorero` | Información tesorero |

## 📊 Variables de Entorno

```env
TELEGRAM_BOT_TOKEN=tu_token_aqui
PORT=8000
RENDER_EXTERNAL_HOSTNAME=tu-app.onrender.com
ADMIN_CHAT_ID=tu_chat_id
```

## 📁 Estructura del Proyecto

```
hunterads-bot/
├── app.py              # Aplicación principal (Flask + Telegram)
├── handlers.py         # Handlers de comandos
├── tesorero.py        # Módulo de tesorero
├── requirements.txt    # Dependencias Python
├── Procfile           # Configuración Railway/Render
├── runtime.txt        # Versión de Python
└── .env.example       # Variables de ejemplo
```

## ⚙️ Configuración en Railway

1. Conectar repositorio GitHub
2. Crear variables de entorno en Railway:
   - `TELEGRAM_BOT_TOKEN` = Tu token del bot
3. El Procfile se ejecuta automáticamente

## 🐛 Troubleshooting

### El bot no responde
- Verificar `TELEGRAM_BOT_TOKEN` en .env
- Verificar logs: `railway logs`
- Usar `/setwebhook` en BotFather de Telegram

### Error de webhook
- Asegurar que `RENDER_EXTERNAL_HOSTNAME` sea correcto
- Revisar logs de la aplicación

## 📝 Licencia

MIT

## 👤 Autor

Mikeslpmex

---

**Última actualización**: 2026-06-10
