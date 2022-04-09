from xml.etree.ElementTree import TreeBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_config_keyboard(buttons, cells_only):

    CONFIG_BUTTONS = buttons[0][0].split(', ')

    CONFIG_KB = ReplyKeyboardMarkup(resize_keyboard=True)

    CONFIG_KB.row(
        KeyboardButton(CONFIG_BUTTONS[0].capitalize()),
        KeyboardButton(CONFIG_BUTTONS[1].capitalize()),
        KeyboardButton(CONFIG_BUTTONS[2].capitalize())
    )
    if cells_only == True:
        CONFIG_KB.row(KeyboardButton("Создать шаблон"))
    CONFIG_KB.row(KeyboardButton('Меню'))

    return CONFIG_KB