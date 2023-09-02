from telegram import ReplyKeyboardMarkup

import messages

buttons = ReplyKeyboardMarkup(
    keyboard=[[messages.HOME]],
    resize_keyboard=True
)
