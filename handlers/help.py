from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Commands:\n"
        "/start — start bot\n"
        "/clear — clear conversation memory\n"
        "Just send any message to chat."
    )
