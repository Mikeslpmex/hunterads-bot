from telegram import Update
from telegram.ext import ContextTypes
from modules.chat_engine import HunterADSChat

chat = HunterADSChat()

async def handlerhunter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    consulta = ' '.join(context.args)
    if not consulta:
        await update.message.reply_text("❌ Ejemplo: /hunter crear app para seguros")
        return

    resultado = chat.generar_respuesta(consulta)
    respuesta = f"🧠 {resultado['respuesta']}\n\nSiguientes pasos:\n" + '\n'.join([f"{i+1}. {p}" for i, p in enumerate(resultado['siguientes_pasos'])])
    await update.message.reply_text(respuesta)
