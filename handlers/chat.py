from telegram import Update
from telegram.ext import ContextTypes
from services.memory_store import MemoryStore
from services.openai_client import generate_reply

memory = MemoryStore()

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text

    memory.add_user_message(user_id, user_text)

    await update.message.chat.send_action("typing")

    reply = generate_reply(memory.get_messages(user_id))

    memory.add_assistant_message(user_id, reply)
    await update.message.reply_text(reply)
