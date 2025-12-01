from tesorero_app import tesorero

async def afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Uso: /afiliado [producto]")
        return

    producto = " ".join(context.args)
    comision = 15.0  # ejemplo fijo

    # Registrar venta en tesorero
    tesorero.registrar_venta(producto, comision)

    await update.message.reply_text(
        f"🛍️ {producto}\n💰 Comisión: ${comision:.2f}\n✅ Venta registrada en tesorero"
    )

async def tesorero_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos = tesorero.estado()
    mensaje = (
        f"💰 **TESORERO ORION**\n\n"
        f"• Ingresos: ${datos['ingresos']:.2f}\n"
        f"• Gastos: ${datos['gastos']:.2f}\n"
        f"• Saldo: ${datos['saldo']:.2f}\n"
        f"• Ventas registradas: {datos['ventas_count']}"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")
