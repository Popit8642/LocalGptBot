from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start dialogue")],
                                     [KeyboardButton(text="About bot")]],
                           resize_keyboard=True)

cancel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Exit mode", callback_data="cancel")]])
