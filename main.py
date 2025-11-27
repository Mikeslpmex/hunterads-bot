import os
import logging
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
from dotenv import load_dotenv
from orion_core_afiliados import generar_enlace_mejorado
import requests

# 🔥 CARGAR VARIABLES DEL .env
load_dotenv()

# ✅ CONFIGURACIÓN
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TESORERO_URL = os.getenv("TESORERO_URL", "")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Función para reportar al tesorero
def reportar_venta_tesorero(producto, comision):
    if not TESORERO_URL:
        return
    
    try:
        requests.post(f"{TESORERO_URL}/reporte", json={
            "nodo": "afiliados_telegram",
            "ingresos": comision,
            "gastos": 0,
            "producto": producto
        }, timeout=5)
    except Exception as e:
        print(f"⚠️ Tesorero no disponible: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 **SISTEMA ORION ACTIVADO**\n\n"
        "Comandos disponibles:\n"
        "/afiliado [producto] - Generar enlace de afiliado\n"
        "/estado - Estado del sistema\n"
        "/tesorero - Info financiera"
    )

async def afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Uso: /afiliado [producto]\n"
            "Ejemplo: /afiliado iPhone 15 Pro"
        )
        return
    
    producto = " ".join(context.args)
    
    try:
        # Generar enlace mejorado
        enlace_info = generar_enlace_mejorado(producto)
        
        # Simular comisión (en producción sería real)
        comision = 15.0  # $15 de comisión ejemplo
        
        # Reportar al tesorero
        reportar_venta_tesorero(producto, comision)
        
        mensaje = (
            f"🛍️ **{producto.upper()}**\n\n"
            f"💰 Comisión estimada: ${comision:.2f}\n"
            f"🔗 [COMPRAR AQUÍ]({enlace_info['url']})\n\n"
            f"📦 {enlace_info['descripcion']}\n"
            f"🏪 Plataforma: {enlace_info['plataforma']}"
        )
        
        await update.message.reply_text(mensaje, parse_mode="Markdown")
        
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    estado_sistema = "✅ **SISTEMA OPERATIVO**\n\n"
    estado_sistema += f"• Bot Token: {'🟢 CONFIGURADO' if TELEGRAM_BOT_TOKEN else '🔴 NO CONFIGURADO'}\n"
    estado_sistema += f"• Chat ID: {ADMIN_CHAT_ID or 'NO CONFIGURADO'}\n"
    estado_sistema += "• Módulo afiliados: 🟢 ACTIVO\n"
    estado_sistema += "• Tesorero: 🟢 CONECTADO\n" if TESORERO_URL else "• Tesorero: 🟡 NO CONFIGURADO\n"
    
    await update.message.reply_text(estado_sistema, parse_mode="Markdown")

async def tesorero_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not TESORERO_URL:
        await update.message.reply_text("❌ Tesorero no configurado - Agrega TESORERO_URL en .env")
        return
    
    try:
        response = requests.get(f"{TESORERO_URL}/estado", timeout=5)
        datos = response.json()
        
        info = (
            f"💰 **TESORERO ORION**\n\n"
            f"• Ingresos totales: ${datos.get('ingresos', 0):.2f}\n"
            f"• Gastos totales: ${datos.get('gastos', 0):.2f}\n"
            f"• Saldo actual: ${datos.get('saldo', 0):.2f}\n"
            f"• Ventas registradas: {datos.get('ventas_count', 0)}"
        )
        
        await update.message.reply_text(info, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error conectando al tesorero: {str(e)}")

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN no configurado")
        return
    
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Handlers COMPLETOS
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("afiliado", afiliado))
    application.add_handler(CommandHandler("estado", estado))
    application.add_handler(CommandHandler("tesorero", tesorero_info))
    
    print("🚀 Sistema Orion COMPLETO - Afiliados + Tesorero activados!")
    application.run_polling()

if __name__ == "__main__":
    main()
