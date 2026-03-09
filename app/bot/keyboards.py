from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def credits_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="6"), KeyboardButton(text="8")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

def grades_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A"), KeyboardButton(text="A-"), KeyboardButton(text="B+")],
            [KeyboardButton(text="B"), KeyboardButton(text="B-"), KeyboardButton(text="C+")],
            [KeyboardButton(text="C"), KeyboardButton(text="C-"), KeyboardButton(text="D+")],
            [KeyboardButton(text="D"), KeyboardButton(text="F")],
        ],
        resize_keyboard=True
    )
    return keyboard

def choice_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Add new course"), KeyboardButton(text="Evaluate the GPA")],
        ],
        resize_keyboard=True
    )
    return keyboard