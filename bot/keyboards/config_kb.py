from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''
*
Этот файл отвечает за генерацию клавиатуры с шаблонами
*
'''


async def create_config_keyboard(buttons, cells_only, first_time):

    CONFIG_BUTTONS = buttons if first_time else buttons[0][0].split(', ')
    # Если в первый раз то нужно взять просто стандартные значения кнопок, иначе из базы данных фильтруется
    
    CONFIG_KB = ReplyKeyboardMarkup(resize_keyboard=True)
    CONFIG_KB.row(
        KeyboardButton(CONFIG_BUTTONS[0]),
        KeyboardButton(CONFIG_BUTTONS[1]),
        KeyboardButton(CONFIG_BUTTONS[2])
    )
    # Создание клавиатуры

    if cells_only == True: CONFIG_KB.row(KeyboardButton("Создать шаблон"))
    CONFIG_KB.row(KeyboardButton('Меню'))
    # Добавление кнопок если для клавиатура для создания шаблона или для выбора
    # Зависит от единственной кнопки Создать шаблон и определяется передаваемым флагом

    return CONFIG_KB