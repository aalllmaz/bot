from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b0 = KeyboardButton("0")
b1 = KeyboardButton("1")
b2 = KeyboardButton("2")
b3 = KeyboardButton("3")
b4 = KeyboardButton("4")
b5 = KeyboardButton("5")
b6 = KeyboardButton("6")

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(b0).row(b1, b2, b3).row(b4, b5, b6)
