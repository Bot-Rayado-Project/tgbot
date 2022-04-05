from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TO_MENU_KB = InlineKeyboardMarkup().add(InlineKeyboardButton('Меню', callback_data = 'menu'))

START_BUTTONS: list = ['расписание', 'шаблоны расписания', 'анекдот', 'донат', 'помощь']
START_BUTTONS_PAYLOAD: list = ["schedule", "config", "joke", "donate", "help"]
START_KB = InlineKeyboardMarkup(row_width=2)


START_KB.row(
    InlineKeyboardButton(START_BUTTONS[0].capitalize(), callback_data = START_BUTTONS_PAYLOAD[0]),
    InlineKeyboardButton(START_BUTTONS[1].capitalize(), callback_data = START_BUTTONS_PAYLOAD[1]))
START_KB.row(
    InlineKeyboardButton(START_BUTTONS[2].capitalize(), callback_data = START_BUTTONS_PAYLOAD[2]),
    InlineKeyboardButton(START_BUTTONS[3].capitalize(), callback_data = START_BUTTONS_PAYLOAD[3]),
    InlineKeyboardButton(START_BUTTONS[4].capitalize(), callback_data = START_BUTTONS_PAYLOAD[4])
)

