from telegram import Update
from telegram.ext import ContextTypes

import markup
import messages


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=messages.GREETING,
        reply_markup=markup.buttons
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Home",
        reply_markup=markup.buttons
    )
