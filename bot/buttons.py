from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from api import level_category

phone_number_btn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Raqam bilan ulashish 📱", request_contact=True)],
    ]
)

main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🎬Videos"), KeyboardButton(text="📖About")],
        [KeyboardButton(text="⚖️Tests"), KeyboardButton(text="📞Contact")],
    ]
)

video_levels = ReplyKeyboardMarkup(
    row_width=2,
)
for level in level_category():
    video_levels.insert(KeyboardButton(text=level['level'] + ' videos'))
video_levels.insert(KeyboardButton(text='⬅Main menu'))

test_levels = ReplyKeyboardMarkup(
    row_width=2,
)
for level in level_category():
    test_levels.insert(KeyboardButton(text=level['level'] + ' tests'))
test_levels.insert(KeyboardButton(text='⬅Main menu'))

about_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🗂Version"), KeyboardButton(text="📞Contact")],
        [KeyboardButton(text="⬅Main menu")],
    ]
)

versions_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🔵Standard"), KeyboardButton(text="🟡Premium")],
        [KeyboardButton(text="⬅About")],
    ]
)