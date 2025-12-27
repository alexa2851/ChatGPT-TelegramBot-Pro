from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm ChatGPT-TelegramBot-Pro.\n\n"
        "Just send me a message and I'll reply.\n"
        "Commands:\n"
        "/help — help\n"
        "/clear — reset conversation"
    )
