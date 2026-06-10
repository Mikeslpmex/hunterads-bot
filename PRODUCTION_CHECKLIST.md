# ✅ Checklist de Producción - HunterAds Bot

## Pre-Deployment

- [ ] **Token de Telegram**
  - [ ] Bot token generado en @BotFather
  - [ ] Token guardado en `TELEGRAM_BOT_TOKEN` de Railway
  - [ ] Token NO está en el repositorio (verificar .gitignore)

- [ ] **Código**
  - [ ] `git push` a main completado
  - [ ] No hay errores en `python -m py_compile app.py`
  - [ ] `pip install -r requirements.txt` funciona sin errores
  - [ ] Verificar sintaxis de todos los archivos `.py`

- [ ] **Variables de Entorno en Railway**
  ```
  TELEGRAM_BOT_TOKEN = tu_token_aqui
  RENDER_EXTERNAL_HOSTNAME = tu-app.onrender.com (o .up.railway.app)
  PORT = 8000 (Railway lo asigna automáticamente)
  ```

## Deployment en Railway

### 1. Conectar Repositorio
```bash
# En Railway:
# 1. Crear nuevo proyecto
# 2. GitHub → Conectar repositorio
# 3. Seleccionar rama: main
```

### 2. Configurar Variables
```bash
# En Railway → Variables
TELEGRAM_BOT_TOKEN = tu_token
RENDER_EXTERNAL_HOSTNAME = {project_name}.up.railway.app
```

### 3. Deploy
```bash
# Railway detecta Procfile y requirements.txt automáticamente
# Deploy inicia automáticamente
```

## Verificación Post-Deploy

### 1. Verificar Logs
```bash
# Railway → Deployments → Logs
# Buscar: "✅ Webhook configurado"
```

### 2. Verificar Health
```bash
curl https://{tu-app}.up.railway.app/health
# Respuesta esperada: {"status": "ok", "bot": "running"}
```

### 3. Probar Bot
```bash
# En Telegram:
# Buscar tu bot por nombre
# /start
# Debe responder: "🤖 BOT HUNTERADS INICIALIZADO [OK]"
```

### 4. Verificar Webhook
```bash
# En BotFather:
# /mybots → Tu bot → Bot Settings → Commands
# Verificar que webhook está activo
```

## Troubleshooting

### El bot no responde
```bash
# 1. Verificar token
railway logs | grep TOKEN

# 2. Verificar webhook
railway logs | grep webhook

# 3. Revisar errores
railway logs | grep ERROR

# 4. Reiniciar
railway redeploy
```

### Error 502/503
```bash
# 1. Verificar Procfile
cat Procfile  # Debe tener: web: gunicorn --bind 0.0.0.0:$PORT app:flask_app

# 2. Verificar requirements.txt
pip install -r requirements.txt

# 3. Test local
python app.py  # Debe funcionar en modo polling
```

### Webhook no configurado
```bash
# 1. Verificar RENDER_EXTERNAL_HOSTNAME
railway variables  # Debe estar presente

# 2. Forzar redeployment
railway redeploy --force

# 3. Revisar logs
railway logs | grep "Configurando webhook"
```

## Monitoreo

### Health Check
```bash
# Configurar en Railway: /health cada 5 minutos
```

### Logs
```bash
# Ver logs en tiempo real
railway logs --follow

# Buscar errores
railway logs | grep ERROR
```

### Métricas
```bash
# Railway → Metrics
# Monitorar:
# - CPU usage
# - Memory usage
# - Requests/segundo
```

## Mantenimiento

### Actualizar Dependencias
```bash
pip list --outdated
# Actualizar manualmente en requirements.txt
git add requirements.txt
git commit -m "chore: Update dependencies"
git push origin main
# Railway redeploy automático
```

### Cambios de Código
```bash
# 1. Desarrollo local
python app.py  # Test con polling

# 2. Commit y push
git add .
git commit -m "feature: descripción"
git push origin main

# 3. Railway redeploy automático
# (ver en Railway → Deployments)
```

## Contacto & Soporte

- **Telegram Bot**: @hunterads_bot
- **Maintainer**: Mikeslpmex
- **Issues**: GitHub Issues

---

**Última actualización**: 2026-06-10
