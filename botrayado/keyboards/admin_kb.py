from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ADMIN_BUTTONS: list = ['SP Шаблоны', 'Логи']

ADMIN_KB = ReplyKeyboardMarkup(resize_keyboard=True)

ADMIN_KB.row(
    KeyboardButton(ADMIN_BUTTONS[0]),
    KeyboardButton(ADMIN_BUTTONS[1]))
    
ADMIN_KB.row(
    KeyboardButton('Меню')
)