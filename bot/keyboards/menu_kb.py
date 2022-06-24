from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''
*
Этот файл отвечает за создание клавиатуры меню
*
'''


START_BUTTONS: list = ['расписание', 'шаблоны расписания', 'анекдот', 'донат', 'помощь']
# Лист с кнопками клавиатуры

START_KB = ReplyKeyboardMarkup(resize_keyboard=True)

START_KB.row(
    KeyboardButton(START_BUTTONS[0].capitalize()),
    KeyboardButton(START_BUTTONS[1].capitalize()))
START_KB.row(
    KeyboardButton(START_BUTTONS[2].capitalize()),
    KeyboardButton(START_BUTTONS[3].capitalize()),
    KeyboardButton(START_BUTTONS[4].capitalize())
)
# Генерация клавиатуры

