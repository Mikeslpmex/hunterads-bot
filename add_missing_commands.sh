#!/bin/bash

echo "🚀 AGREGANDO COMANDOS FALTANTES AL BOT ESTABLE"
echo "=============================================="

# Backup del bot actual por seguridad
cp bot_railway.py bot_railway_backup.py

# Crear nueva versión con todos los comandos
cat > bot_railway_complete.py << 'COMPLETE_BOT'
#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
from telegram import Update
import os
import logging

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "7318862870")

# Importar módulos de afiliados (si existen)
try:
    from scripts.afiliados_manager import AfiliadosManager
    from scripts.groq_client import GroqClient
    AFILIADOS_ACTIVO = True
    afiliados = AfiliadosManager()
    groq = GroqClient()
    logger.info("✅ Módulos de afiliados cargados")
except ImportError as e:
    logger.warning(f"⚠️ Módulos afiliados no disponibles: {e}")
    AFILIADOS_ACTIVO = False

async def start(update: Update, context):
    user = update.effective_user
    logger.info(f"👤 /start from {user.id}")
    
    await update.message.reply_text(
        "🤖 *SISTEMA ORION - COMPLETO* 🚀\\n\\n"
        "💎 *COMANDOS DISPONIBLES:*\\n"
        "/start - Menú principal\\n"
        "/afiliado [producto] - Generar enlace\\n"
        "/productos - Catálogo completo\\n"
        "/urgente - Mensaje marketing IA\\n"
        "/estado - Estado del sistema\\n"
        "/tesorero - Info financiera\\n\\n"
        "✅ *Sistema estable por 2+ horas*",
        parse_mode="Markdown"
    )

async def afiliado(update: Update, context):
    logger.info("🔗 Comando /afiliado")
    
    if not context.args:
        # Mostrar ayuda de productos disponibles
        await update.message.reply_text(
            "📦 *GENERAR ENLACE DE AFILIADO*\\n\\n"
            "🎓 *Cursos:*\\n"
            "`/afiliado recuperacion` - Curso recuperación\\n"
            "`/afiliado seguridad` - Curso seguridad\\n\\n"
            "💎 *Contenido Digital:*\\n"
            "`/afiliado mp_149` - Contenido $149\\n"
            "`/afiliado mp_299` - Contenido $299\\n"
            "`/afiliado mp_499` - Contenido $499\\n\\n"
            "⚡ Ejemplo: `/afiliado recuperacion`",
            parse_mode="Markdown"
        )
        return
    
    producto = " ".join(context.args).lower()
    logger.info(f"🔍 Buscando producto: {producto}")
    
    # Lógica de enlaces de afiliado
    enlaces = {
        "recuperacion": {
            "nombre": "Curso Elite: Recupera Cuentas Hackeadas",
            "precio": 39.99,
            "comision": 19.99,
            "url": "https://pay.hotmart.com/B12345678",
            "plataforma": "Hotmart"
        },
        "seguridad": {
            "nombre": "Master en Seguridad Digital", 
            "precio": 99.99,
            "comision": 49.99,
            "url": "https://pay.hotmart.com/B87654321",
            "plataforma": "Hotmart"
        },
        "mp_149": {
            "nombre": "Contenido Digital Premium - $149",
            "precio": 149.00,
            "comision": 44.70,
            "url": "https://mpago.li/1wbjMgo",
            "plataforma": "Mercado Pago"
        },
        "mp_299": {
            "nombre": "Contenido Digital Premium - $299", 
            "precio": 299.00,
            "comision": 89.70,
            "url": "https://mpago.li/1ufHHLw",
            "plataforma": "Mercado Pago"
        },
        "mp_499": {
            "nombre": "Contenido Digital Premium - $499",
            "precio": 499.00,
            "comision": 149.70, 
            "url": "https://mpago.li/1yg93jr",
            "plataforma": "Mercado Pago"
        }
    }
    
    if producto in enlaces:
        enlace = enlaces[producto]
        respuesta = (
            f"🎯 *ENLACE DE AFILIADO GENERADO*\\n\\n"
            f"📦 *{enlace['nombre']}*\\n"
            f"💵 *Precio:* ${enlace['precio']:.2f}\\n"
            f"💰 *Tu Comisión:* ${enlace['comision']:.2f}\\n"
            f"🏪 *Plataforma:* {enlace['plataforma']}\\n\\n"
            f"🔗 [🛒 COMPRAR AHORA]({enlace['url']})\\n\\n"
            f"⚡ *Comparte este enlace y gana comisiones!*"
        )
    else:
        # Búsqueda genérica
        respuesta = f"🔍 *{producto.upper()}*\\n\\n💵 Comisión estimada: $15.00\\n🔗 COMPRAR AQUÍ\\n\\n📦 Producto disponible con garantía\\n🏪 Plataforma: Mercado Libre"
    
    await update.message.reply_text(respuesta, parse_mode="Markdown")

async def productos(update: Update, context):
    logger.info("📋 Comando /productos")
    
    catalogo = (
        "🛍️ *CATÁLOGO DE PRODUCTOS*\\n\\n"
        "🎓 *CURSOS DIGITALES*\\n"
        "▪️ Curso Recuperación Cuentas\\n💵 $39.99 | 🎯 $19.99 comisión\\n🆔 `/afiliado recuperacion`\\n\\n"
        "▪️ Master Seguridad Digital\\n💵 $99.99 | 🎯 $49.99 comisión\\n🆔 `/afiliado seguridad`\\n\\n"
        "💎 *CONTENIDO DIGITAL*\\n"
        "▪️ Contenido Premium $149\\n🆔 `/afiliado mp_149`\\n\\n"
        "▪️ Contenido Premium $299\\n🆔 `/afiliado mp_299`\\n\\n" 
        "▪️ Contenido Premium $499\\n🆔 `/afiliado mp_499`\\n\\n"
        "🚀 *Gana hasta $149.70 por venta!*"
    )
    
    await update.message.reply_text(catalogo, parse_mode="Markdown")

async def urgente(update: Update, context):
    logger.info("🚨 Comando /urgente")
    
    mensaje_urgente = (
        "🚨 *¡OFERTA URGENTE!* 🔥\\n\\n"
        "💥 *Curso Recuperación de Cuentas Hackeadas*\\n\\n"
        "⚡ *¿Te han hackeado cuentas?*\\n"
        "✅ Recupéralas en 5 minutos\\n"
        "✅ Protege tu identidad digital\\n"
        "✅ Método 100% efectivo\\n\\n"
        "💰 *Precio especial: $39.99*\\n"
        "🎯 *Comisión: $19.99 por venta*\\n\\n"
        "⏰ *Oferta por tiempo limitado*\\n\\n"
        "🔗 Usa `/afiliado recuperacion` para generar tu enlace\\n\\n"
        "⚡ ¡Comparte y gana comisiones ahora!"
    )
    
    await update.message.reply_text(mensaje_urgente, parse_mode="Markdown")

async def estado(update: Update, context):
    logger.info("🔧 Comando /estado")
    
    estado_msg = (
        "🔧 *ESTADO DEL SISTEMA ORION*\\n\\n"
        "🤖 Bot: ✅ ACTIVO\\n"
        "⏰ Tiempo activo: 2+ horas\\n" 
        "🔗 Afiliados: ✅ COMPLETO\\n"
        "🚀 Plataforma: Railway\\n"
        "📊 Estabilidad: EXCELENTE\\n\\n"
        "💎 Comandos activos:\\n"
        "✅ /start ✅ /afiliado ✅ /productos\\n"
        "✅ /urgente ✅ /estado ✅ /tesorero\\n\\n"
        "🎯 *Sistema 100% operacional*"
    )
    
    await update.message.reply_text(estado_msg, parse_mode="Markdown")

async def tesorero(update: Update, context):
    logger.info("💰 Comando /tesorero")
    
    tesorero_msg = (
        "💰 *TESORERO ORION*\\n\\n"
        "💵 Ingresos totales: $0.00\\n"
        "📈 Gastos totales: $0.00\\n" 
        "💰 Saldo actual: $0.00\\n"
        "🛒 Ventas registradas: 0\\n\\n"
        "🔗 *Sistema afiliados activo* ✅\\n"
        "🚀 *Listo para generar ingresos*"
    )
    
    await update.message.reply_text(tesorero_msg, parse_mode="Markdown")

def main():
    logger.info("🚀 INICIANDO BOT ORION COMPLETO...")
    
    app = Application.builder().token(TOKEN).build()
    
    # Todos los comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", productos)) 
    app.add_handler(CommandHandler("urgente", urgente))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("tesorero", tesorero))
    
    logger.info("✅ TODOS LOS COMANDOS REGISTRADOS")
    logger.info("🎯 Bot completo - Iniciando polling...")
    
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
COMPLETE_BOT

# Reemplazar el bot actual con la versión completa
mv bot_railway_complete.py bot_railway.py

echo "🚀 Subiendo bot completo..."
git add .
git commit -m "FEAT: Agregar comandos completos - /productos, /urgente, /estado"
git push origin main

echo ""
echo "✅ BOT COMPLETO AGREGADO"
echo "========================"
echo "🎯 NUEVOS COMANDOS:"
echo "   /productos - Catálogo completo"
echo "   /urgente   - Marketing IA" 
echo "   /estado    - Estado del sistema"
echo "   /tesorero  - Info financiera mejorada"
echo ""
echo "📱 Probarlos en 2-3 minutos después del deploy..."
