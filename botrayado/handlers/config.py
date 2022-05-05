from datetime import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
import botrayado.keyboards.config_kb as config_kb
from botrayado.schedule.sheethandler import print_full_schedule, print_schedule
import botrayado.keyboards.schedule_kb as schedule_kb
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler, fetch_commands
from botrayado.utils.logger import get_logger
import traceback


logger = get_logger(__name__)

btns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ячейка']


@database_handler(ret_cfg=True)
async def config_start(msg: types.Message, buttons: list) -> None:

    if buttons == []:
        CONFIG_KB = config_kb.create_config_keyboard(
            ['1 ячейка', '2 ячейка', '3 ячейка'], True, True)

    else:
        CONFIG_KB = config_kb.create_config_keyboard(buttons, True, False)

    message = 'Выберите шаблон или создайте новый.'
    await msg.answer(message,reply_markup=CONFIG_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))


@database_handler(ret_cfg=True)
async def create_blueprint_start(msg: types.Message,
                                 buttons: list) -> None:

    CONFIG_KB = config_kb.create_config_keyboard(buttons, False, False)

    message = 'Выберите ячейку для (пере-)записи.'
    await msg.answer(message, reply_markup=CONFIG_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))


@database_handler(ret_cfg=True)
async def choose_cells_handler(msg: types.Message, buttons: list) -> None:
    start_time = datetime.now()
    all_commands = await fetch_commands(msg)

    if all_commands[1][0].lower() == 'создать шаблон':
        message = 'Выберите последовательность шаблона'
        await msg.answer(message, reply_markup=schedule_kb.DAYS_OF_WEEK_CFG_KB)
        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))

    
    elif all_commands[0][0].lower() != '1 ячейка' and all_commands[0][0].lower() != '2 ячейка' and all_commands[0][0].lower() != '3 ячейка':
        res = all_commands[0][0].split(' ')
        if res[0] == 'СН':

            schedule = await print_full_schedule(msg.from_user.id,'следующая неделя', res[1].lower())
            if schedule == None:

                message = 'Непредвиденная ошибка'
                await msg.answer(message, reply_markup=START_KB)
                logger.error(f'Ошибка в выводе расписания в choose_cells_handler, config.py, {traceback.format_exc()}')

            else:
        
                await msg.answer(schedule, parse_mode="HTML")
                logger.info('Time of table out: ' + str(datetime.now() - start_time))
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

        elif res[0] == 'ТН':

            schedule = await print_full_schedule(msg.from_user.id,'текущая неделя', res[1].lower())
            if schedule == None:

                message = 'Непредвиденная ошибка'
                await msg.answer(message, reply_markup=START_KB)
                logger.error(f'Ошибка в выводе расписания в choose_cells_handler, config.py, {traceback.format_exc()}')

            else:

                await msg.answer(schedule, parse_mode="HTML")
                logger.info('Time of table out: ' + str(datetime.now() - start_time))
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

        else:
            schedule = await print_schedule(msg.from_user.id,res[0].lower(), res[1].lower())
            if schedule == None:

                message = 'Непредвиденная ошибка'
                await msg.answer(message, reply_markup=START_KB)
                logger.error(f'Ошибка в выводе расписания в choose_cells_handler, config.py, {traceback.format_exc()}')

            else:
                await msg.answer(schedule, parse_mode="HTML")
                logger.info('Time of table out: ' + str(datetime.now() - start_time))
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

    else:

        message = 'Ячейка пуста'
        await msg.answer(message, reply_markup=config_kb.create_config_keyboard(buttons, True, False))
        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))


def register_handler_config(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(config_start, filters.Text(
        equals='Шаблоны расписания', ignore_case=True))
    bot_dispatcher.register_message_handler(create_blueprint_start, filters.Text( 
        equals='Создать шаблон', ignore_case=True))
    bot_dispatcher.register_message_handler(choose_cells_handler, filters.Text(
        endswith=btns, ignore_case=True))
