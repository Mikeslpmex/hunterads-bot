#!/usr/bin/env python3
"""
Handlers para comandos del bot HunterAds
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Inicializar bot"""
    try:
        await update.message.reply_text(
            "🤖 **BOT HUNTERADS INICIALIZADO** [OK]\n\n"
            "Comandos disponibles:\n"
            "📌 /afiliado - Registrar venta de afiliado\n"
            "🛍️ /productos - Ver catálogo\n"
            "🚨 /urgente - Marketing urgente\n"
            "✅ /estado - Estado del sistema\n"
            "🪙 /tesorero - Ver tesorero\n",
            parse_mode="Markdown"
        )
        logger.info(f"✅ Usuario {update.effective_user.id} inició el bot")
    except Exception as e:
        logger.error(f"❌ Error en start: {e}")
        await update.message.reply_text("❌ Error al inicializar bot")


async def afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /afiliado - Registrar venta"""
    try:
        if not context.args:
            await update.message.reply_text(
                "❌ Uso incorrecto\n"
                "Ejemplo: `/afiliado producto_name 150.00`",
                parse_mode="Markdown"
            )
            return

        producto = context.args[0] if len(context.args) > 0 else "Desconocido"
        monto = float(context.args[1]) if len(context.args) > 1 else 0.0
        comision = monto * 0.15  # 15% de comisión

        mensaje = (
            f"🔗 **VENTA REGISTRADA**\n\n"
            f"• Producto: {producto}\n"
            f"• Monto: ${monto:.2f}\n"
            f"• Comisión (15%): ${comision:.2f}\n"
            f"✅ Registrado en tesorero"
        )
        await update.message.reply_text(mensaje, parse_mode="Markdown")
        logger.info(f"✅ Venta registrada: {producto} - ${monto:.2f}")

    except ValueError:
        await update.message.reply_text("❌ El monto debe ser un número válido")
    except Exception as e:
        logger.error(f"❌ Error en afiliado: {e}")
        await update.message.reply_text("❌ Error al registrar venta")


async def productos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /productos - Ver catálogo"""
    try:
        catalogo = (
            "🛍️ **CATÁLOGO DE PRODUCTOS**\n\n"
            "1️⃣ Premium Pack - $299.99\n"
            "2️⃣ Basic Pack - $99.99\n"
            "3️⃣ Starter Pack - $49.99\n\n"
            "Usa `/afiliado [nombre] [monto]` para registrar una venta"
        )
        await update.message.reply_text(catalogo, parse_mode="Markdown")
        logger.info(f"✅ Catálogo enviado a {update.effective_user.id}")

    except Exception as e:
        logger.error(f"❌ Error en productos: {e}")
        await update.message.reply_text("❌ Error al mostrar catálogo")


async def urgente(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /urgente - Marketing urgente"""
    try:
        mensaje = (
            "🚨 **OFERTA URGENTE**\n\n"
            "⏰ Válido por 24 horas\n"
            "💰 Descuento del 30% en todos los productos\n"
            "📱 Comparte con tus contactos\n\n"
            "¡Aprovecha ahora!"
        )
        await update.message.reply_text(mensaje, parse_mode="Markdown")
        logger.info(f"✅ Marketing urgente enviado")

    except Exception as e:
        logger.error(f"❌ Error en urgente: {e}")
        await update.message.reply_text("❌ Error al enviar marketing")


async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /estado - Estado del sistema"""
    try:
        estado_msg = (
            "✅ **ESTADO DEL SISTEMA**\n\n"
            "🟢 Bot: Online\n"
            "🟢 Tesorero: Online\n"
            "🟢 Catálogo: Online\n"
            "🟢 Marketing: Online\n\n"
            "Sistema estable ✅"
        )
        await update.message.reply_text(estado_msg, parse_mode="Markdown")
        logger.info(f"✅ Estado consultado por {update.effective_user.id}")

    except Exception as e:
        logger.error(f"❌ Error en estado: {e}")
        await update.message.reply_text("❌ Error al consultar estado")


async def tesorero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /tesorero - Información del tesorero"""
    try:
        tesorero_info = (
            "🪙 **TESORERO ORION**\n\n"
            "💰 Ingresos: $1,500.00\n"
            "💸 Gastos: $300.00\n"
            "✅ Saldo: $1,200.00\n"
            "📊 Ventas registradas: 12\n"
            "📈 Comisiones acumuladas: $450.00"
        )
        await update.message.reply_text(tesorero_info, parse_mode="Markdown")
        logger.info(f"✅ Tesorero consultado por {update.effective_user.id}")

    except Exception as e:
        logger.error(f"❌ Error en tesorero: {e}")
        await update.message.reply_text("❌ Error al consultar tesorero")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para errores"""
    logger.error(f"Update {update} caused error: {context.error}")
    try:
        await update.message.reply_text(
            "⚠️ Ocurrió un error. Intenta de nuevo."
        )
    except Exception:
        pass
