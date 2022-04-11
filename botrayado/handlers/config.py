from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
import botrayado.keyboards.config_kb as config_kb
from botrayado.schedule.sheethandler import print_full_schedule, print_schedule
import botrayado.keyboards.schedule_kb as schedule_kb
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler


COMMANDS = []
COMMANDS_2 = []
btns = ['1', '2', '3', 'С', 'З', 'Т']


@database_handler(ret_cfg=True)
async def config_start(msg: types.Message, buttons: list) -> None:

    if buttons == []:
        CONFIG_KB = config_kb.create_config_keyboard(
            ['1 ячейка', '2 ячейка', '3 ячейка'], True, True)

    else:
        CONFIG_KB = config_kb.create_config_keyboard(buttons, True, False)

    await msg.answer('Выберите шаблон или создайте новый.',
                     reply_markup=CONFIG_KB)


@database_handler(ret_cfg=True)
async def create_blueprint_start(msg: types.Message,
                                 buttons: list) -> None:
                                 
    COMMANDS.append(msg.text)
    COMMANDS_2.append(msg.text)

    CONFIG_KB = config_kb.create_config_keyboard(buttons, False, False)

    await msg.answer('Выберите ячейку для (пере-)записи.',
                reply_markup=CONFIG_KB)


@database_handler(ret_cfg=True)
async def choose_cells_handler(msg: types.Message, buttons: list) -> None:
    COMMANDS.append(msg.text)
    COMMANDS_2.append(msg.text)

    if 'Создать шаблон' in COMMANDS:
        await msg.answer('Выберите последовательность шаблона', reply_markup=schedule_kb.DAYS_OF_WEEK_KB)

    
    if '1 ячейка' not in COMMANDS and '2 ячейка' not in COMMANDS and '3 ячейка' not in COMMANDS:
        res = COMMANDS[0].split(' ')
        if res[0] == 'СН':
            await msg.answer(await print_full_schedule('следующая неделя', res[1].lower()))
        elif res[0] == 'ТН':
            await msg.answer(await print_full_schedule('текущая неделя', res[1].lower()))
        else:
            await msg.answer(await print_schedule(res[0].lower(), res[1].lower()))
    else:
        await msg.answer('Ячейка пуста', reply_markup=config_kb.create_config_keyboard(buttons, True, False))
    
        
    COMMANDS.clear()


def register_handler_config(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(config_start, filters.Text(
        contains='Шаблоны расписания', ignore_case=True))
    bot_dispatcher.register_message_handler(create_blueprint_start, filters.Text(
        contains='Создать шаблон', ignore_case=True))
    bot_dispatcher.register_message_handler(choose_cells_handler, filters.Text(
        startswith=btns, ignore_case=True))
