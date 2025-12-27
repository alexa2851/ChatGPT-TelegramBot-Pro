from telegram import Update
from telegram.ext import ContextTypes
from services.memory_store import MemoryStore

memory = MemoryStore()

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    memory.clear(user_id)
    await update.message.reply_text("🧹 Conversation memory cleared.")
