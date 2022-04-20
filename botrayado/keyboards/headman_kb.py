from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


CHOOSE_WEEK_BUTTONS: list = ['четная', 'нечетная', 'обе']
CHOOSE_PAIR_BUTTONS: list = ['1 пара', '2 пара', '3 пара', '4 пара', '5 пара', 'весь день']
CHOOSE_MOVE_BUTTONS: list = ['перезаписать', 'удалить']
CHOOSE_DAY_OF_WEEK_BUTTONS: list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']


CHOOSE_WEEK_KB = ReplyKeyboardMarkup(resize_keyboard=True)
CHOOSE_PAIR_KB = ReplyKeyboardMarkup(resize_keyboard=True)
CHOOSE_MOVE_KB = ReplyKeyboardMarkup(resize_keyboard=True)
CHOOSE_DAY_OF_WEEK_KB = ReplyKeyboardMarkup(resize_keyboard=True)


CHOOSE_WEEK_KB.row(
    KeyboardButton(CHOOSE_WEEK_BUTTONS[0].capitalize()),
    KeyboardButton(CHOOSE_WEEK_BUTTONS[1].capitalize()),
    KeyboardButton(CHOOSE_WEEK_BUTTONS[2].capitalize())
)
CHOOSE_WEEK_KB.row(KeyboardButton('Меню'))


CHOOSE_PAIR_KB.row(
    KeyboardButton(CHOOSE_PAIR_BUTTONS[0].capitalize()),
    KeyboardButton(CHOOSE_PAIR_BUTTONS[1].capitalize()),
    KeyboardButton(CHOOSE_PAIR_BUTTONS[2].capitalize())
)
CHOOSE_PAIR_KB.row(
    KeyboardButton(CHOOSE_PAIR_BUTTONS[3].capitalize()),
    KeyboardButton(CHOOSE_PAIR_BUTTONS[4].capitalize()),
    KeyboardButton(CHOOSE_PAIR_BUTTONS[5].capitalize())
)
CHOOSE_PAIR_KB.row(KeyboardButton('Меню'))


CHOOSE_MOVE_KB.row(
    KeyboardButton(CHOOSE_MOVE_BUTTONS[0].capitalize()),
    KeyboardButton(CHOOSE_MOVE_BUTTONS[1].capitalize())
)
CHOOSE_MOVE_KB.row(KeyboardButton('Меню'))


CHOOSE_DAY_OF_WEEK_KB.row(
    KeyboardButton(CHOOSE_DAY_OF_WEEK_BUTTONS[0].capitalize()),
    KeyboardButton(CHOOSE_DAY_OF_WEEK_BUTTONS[1].capitalize()),
    KeyboardButton(CHOOSE_DAY_OF_WEEK_BUTTONS[2].capitalize())
)
CHOOSE_DAY_OF_WEEK_KB.row(
    KeyboardButton(CHOOSE_DAY_OF_WEEK_BUTTONS[3].capitalize()),
    KeyboardButton(CHOOSE_DAY_OF_WEEK_BUTTONS[4].capitalize()),
    KeyboardButton(CHOOSE_DAY_OF_WEEK_BUTTONS[5].capitalize())
)
CHOOSE_DAY_OF_WEEK_KB.row(KeyboardButton('Меню'))