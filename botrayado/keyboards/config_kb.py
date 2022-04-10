from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_config_keyboard(buttons, cells_only, first_time):
    if first_time:
        CONFIG_BUTTONS = buttons
    else:
        CONFIG_BUTTONS = buttons[0][0].split(', ')
    
    CONFIG_KB = ReplyKeyboardMarkup(resize_keyboard=True)
    CONFIG_KB.row(
        KeyboardButton(CONFIG_BUTTONS[0]),
        KeyboardButton(CONFIG_BUTTONS[1]),
        KeyboardButton(CONFIG_BUTTONS[2])
    )
    if cells_only == True:
        CONFIG_KB.row(KeyboardButton("Создать шаблон"))
    CONFIG_KB.row(KeyboardButton('Меню'))

    return CONFIG_KB