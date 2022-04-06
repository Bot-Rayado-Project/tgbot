from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


START_BUTTONS: list = ['расписание', 'шаблоны расписания', 'анекдот', 'донат', 'помощь']
START_KB = ReplyKeyboardMarkup(resize_keyboard=True)


START_KB.row(
    KeyboardButton(START_BUTTONS[0].capitalize()),
    KeyboardButton(START_BUTTONS[1].capitalize()))
START_KB.row(
    KeyboardButton(START_BUTTONS[2].capitalize()),
    KeyboardButton(START_BUTTONS[3].capitalize()),
    KeyboardButton(START_BUTTONS[4].capitalize())
)

