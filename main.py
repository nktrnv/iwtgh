import os

from telegram.ext import CommandHandler, ApplicationBuilder, MessageHandler
from telegram.ext.filters import Regex

import handlers
import messages


def main():
    token = os.getenv("TOKEN")
    application = ApplicationBuilder().token(token).build()
    application.add_handler(
        CommandHandler("start", handlers.start)
    )
    application.add_handler(
        MessageHandler(Regex(messages.HOME), handlers.home)
    )
    application.run_polling()


if __name__ == "__main__":
    main()
