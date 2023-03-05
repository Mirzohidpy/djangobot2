from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

prime_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🎬Videos Prime"), KeyboardButton(text="⚖️Tests Prime")],
    ]
)
