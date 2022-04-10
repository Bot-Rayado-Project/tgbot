from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


SPECIAL_BLUEPRINTS_BUTTONS: list = ['rayadotd', 'rayadotmr', 'fuckmaryamtd', 'fuckmaryamtmr', 'ваня'] 

SPECIAL_BLUEPRINTS_KB = ReplyKeyboardMarkup(resize_keyboard=True)

SPECIAL_BLUEPRINTS_KB.row(
    KeyboardButton(SPECIAL_BLUEPRINTS_BUTTONS[0]),
    KeyboardButton(SPECIAL_BLUEPRINTS_BUTTONS[1]),
    KeyboardButton(SPECIAL_BLUEPRINTS_BUTTONS[2])
)

SPECIAL_BLUEPRINTS_KB.row(
    KeyboardButton(SPECIAL_BLUEPRINTS_BUTTONS[3]),
    KeyboardButton(SPECIAL_BLUEPRINTS_BUTTONS[4])
)

SPECIAL_BLUEPRINTS_KB.row(KeyboardButton('Меню'))