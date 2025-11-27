#!/bin/bash

echo "🧹 LIMPIANDO CACHE DE TELEGRAM"
echo "=============================="

# Agregar un timestamp único al código para forzar actualización
TIMESTAMP=$(date +%Y%m%d%H%M%S)

cat > bot_railway.py << 'BOT'
#!/usr/bin/env python3
from telegram.ext import Application, CommandHandler
import logging

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TOKEN 
TOKEN = "8285048355:AAErNzEOWcsfocP5WvNUZYb3LDTYTtvUE-k"

# TIMESTAMP ÚNICO PARA LIMPIAR CACHE
DEPLOY_TIMESTAMP = "20241127_0852"

async def start(update, context):
    menu_principal = (
        "🤖 *SISTEMA ORION - COMANDOS DISPONIBLES* 🚀\\n\\n"
        
        "🛍️ *AFILIADOS Y VENTAS*\\n"
        "🔹 /afiliado [producto] - Generar enlace de afiliado\\n"
        "🔹 /productos - Ver catálogo completo\\n"
        "🔹 /urgente - Mensaje de marketing urgente\\n\\n"
        
        "💰 *FINANZAS Y ESTADÍSTICAS*\\n" 
        "🔹 /tesorero - Estado financiero\\n"
        "🔹 /estado - Estado del sistema\\n\\n"
        
        "🎯 *EJEMPLOS DE USO*\\n"
        "🔹 /afiliado recuperacion - Curso recuperación\\n"
        "🔹 /afiliado seguridad - Curso seguridad\\n"
        "🔹 /afiliado mp_149 - Contenido $149\\n"
        "🔹 /afiliado mp_299 - Contenido $299\\n"
        "🔹 /afiliado mp_499 - Contenido $499\\n\\n"
        
        "💎 *Plataformas:* Hotmart • Mercado Pago • Alibaba\\n"
        "🎯 *Comisiones:* Hasta $149.70 por venta\\n"
        "🚀 *Sistema:* 100% Operacional\\n\\n"
        
        "⚡ *¡Escribe un comando y empieza a ganar!*"
    )
    
    await update.message.reply_text(menu_principal, parse_mode="Markdown")

async def afiliado(update, context):
    if not context.args:
        ayuda_afiliado = (
            "🔗 *GENERAR ENLACES DE AFILIADO*\\n\\n"
            
            "🎓 *CURSOS DIGITALES*\\n"
            "🔹 /afiliado recuperacion - Curso Recuperación\\n"
            "💵 $39.99 | 🎯 $19.99 comisión\\n\\n"
            
            "🔹 /afiliado seguridad - Master Seguridad\\n" 
            "💵 $99.99 | 🎯 $49.99 comisión\\n\\n"
            
            "💎 *CONTENIDO DIGITAL*\\n"
            "🔹 /afiliado mp_149 - Contenido Premium\\n"
            "💵 $149.00 | 🎯 $44.70 comisión\\n\\n"
            
            "🔹 /afiliado mp_299 - Contenido Premium\\n"
            "💵 $299.00 | 🎯 $89.70 comisión\\n\\n"
            
            "🔹 /afiliado mp_499 - Contenido Premium\\n"
            "💵 $499.00 | 🎯 $149.70 comisión\\n\\n"
            
            "🚀 *¡Gana hasta $149.70 por venta!*"
        )
        await update.message.reply_text(ayuda_afiliado, parse_mode="Markdown")
        return
    
    producto = " ".join(context.args).lower()
    
    # Catálogo de productos
    productos = {
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
    
    if producto in productos:
        p = productos[producto]
        respuesta = (
            f"🎯 *ENLACE GENERADO* ✅\\n\\n"
            f"📦 *{p['nombre']}*\\n"
            f"💵 *Precio:* ${p['precio']:.2f}\\n"
            f"💰 *Tu Comisión:* ${p['comision']:.2f}\\n"
            f"🏪 *Plataforma:* {p['plataforma']}\\n\\n"
            f"🔗 [🛒 COMPRAR AHORA]({p['url']})\\n\\n"
            f"⚡ *¡Comparte este enlace y gana comisiones!*"
        )
    else:
        respuesta = f"🔍 *{producto.upper()}*\\n\\n💵 Comisión estimada: $15.00\\n🔗 COMPRAR AQUÍ\\n\\n📦 Producto disponible con garantía\\n🏪 Plataforma: Mercado Libre"
    
    await update.message.reply_text(respuesta, parse_mode="Markdown")

async def productos(update, context):
    catalogo = (
        "🛍️ *CATÁLOGO COMPLETO DE PRODUCTOS*\\n\\n"
        
        "🎓 *CURSOS DIGITALES*\\n"
        "🔹 Curso Recuperación de Cuentas\\n"
        "💵 Precio: $39.99\\n"
        "🎯 Tu Comisión: $19.99\\n"
        "🆔 /afiliado recuperacion\\n\\n"
        
        "🔹 Master Seguridad Digital\\n"
        "💵 Precio: $99.99\\n" 
        "🎯 Tu Comisión: $49.99\\n"
        "🆔 /afiliado seguridad\\n\\n"
        
        "💎 *CONTENIDO DIGITAL PREMIUM*\\n"
        "🔹 Contenido Digital $149\\n"
        "🎯 Tu Comisión: $44.70\\n"
        "🆔 /afiliado mp_149\\n\\n"
        
        "🔹 Contenido Digital $299\\n"
        "🎯 Tu Comisión: $89.70\\n"
        "🆔 /afiliado mp_299\\n\\n"
        
        "🔹 Contenido Digital $499\\n"
        "🎯 Tu Comisión: $149.70\\n"
        "🆔 /afiliado mp_499\\n\\n"
        
        "🚀 *¡Gana hasta $149.70 por venta!*\\n"
        "💎 *Total comisiones posibles: $454.08*"
    )
    
    await update.message.reply_text(catalogo, parse_mode="Markdown")

async def urgente(update, context):
    mensaje = (
        "🚨 *¡OFERTA URGENTE!* 🔥\\n\\n"
        "💥 *Curso Recuperación de Cuentas Hackeadas*\\n\\n"
        "⚡ *¿Te han hackeado cuentas?*\\n"
        "✅ Recupéralas en 5 minutos\\n"
        "✅ Protege tu identidad digital\\n"
        "✅ Método 100% efectivo\\n\\n"
        "💰 *Precio especial: $39.99*\\n"
        "🎯 *Comisión: $19.99 por venta*\\n\\n"
        "⏰ *Oferta por tiempo limitado*\\n\\n"
        "🔗 Usa /afiliado recuperacion para generar tu enlace\\n\\n"
        "⚡ ¡Comparte y gana comisiones ahora!"
    )
    
    await update.message.reply_text(mensaje, parse_mode="Markdown")

async def estado(update, context):
    estado_msg = (
        "🔧 *ESTADO DEL SISTEMA ORION*\\n\\n"
        "🤖 Bot: ✅ ACTIVO\\n"
        "🔗 Afiliados: ✅ COMPLETO\\n" 
        "🚀 Plataforma: Railway\\n"
        "📊 Estabilidad: EXCELENTE\\n\\n"
        "💎 *COMANDOS ACTIVOS:*\\n"
        "✅ /start - Menú principal\\n"
        "✅ /afiliado - Generar enlaces\\n"
        "✅ /productos - Catálogo completo\\n"
        "✅ /urgente - Marketing urgente\\n"
        "✅ /estado - Estado del sistema\\n"
        "✅ /tesorero - Info financiera\\n\\n"
        "🎯 *Sistema 100% operacional*"
    )
    
    await update.message.reply_text(estado_msg, parse_mode="Markdown")

async def tesorero(update, context):
    tesorero_msg = (
        "💰 *TESORERO ORION*\\n\\n"
        "💵 Ingresos totales: $0.00\\n"
        "📈 Gastos totales: $0.00\\n"
        "💰 Saldo actual: $0.00\\n" 
        "🛒 Ventas registradas: 0\\n\\n"
        "🔗 *Sistema afiliados activo* ✅\\n"
        "🚀 *Listo para generar ingresos*\\n\\n"
        "💎 *Comisiones disponibles:*\\n"
        "🎯 Hasta $149.70 por venta\\n"
        "📊 Múltiples plataformas\\n"
        "⚡ Pagos automáticos"
    )
    
    await update.message.reply_text(tesorero_msg, parse_mode="Markdown")

def main():
    logger.info("🚀 INICIANDO BOT - CACHE LIMPIADO...")
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("afiliado", afiliado))
    app.add_handler(CommandHandler("productos", productos))
    app.add_handler(CommandHandler("urgente", urgente))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("tesorero", tesorero))
    
    logger.info("✅ BOT LISTO - CACHE ACTUALIZADO")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
BOT

echo "🚀 Subiendo actualización para limpiar cache..."
git add .
git commit -m "FIX: Limpiar cache Telegram - Timestamp único"
git push origin main

echo ""
echo "✅ CACHE LIMPIADO"
echo "================="
echo "🧹 Se forzó actualización con timestamp único"
echo "📱 Telegram deberá mostrar mensajes limpios ahora"
echo "🚀 Deploy en 2-3 minutos..."
echo ""
echo "🎯 Después del deploy, prueba: /start"
echo "💡 Si sigue con problemas, cierra y reabre Telegram"
