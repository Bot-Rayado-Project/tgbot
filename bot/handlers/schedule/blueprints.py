from datetime import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.keyboards.config_kb import create_config_keyboard
from bot.schedule.schedule import print_full_schedule, print_schedule
from bot.keyboards.schedule_kb import DAYS_OF_WEEK_KB
from bot.keyboards.menu_kb import START_KB
from bot.constants.schedule import BTNS_TO_CHOOSE_CELLS
from bot.db.db import database_handler, database_fetch_all_commands, database_get_blueprints_buttons
from bot.logger.logger import get_logger
import traceback


logger = get_logger(__name__)


@database_handler()
async def config_start(message_from_user: types.Message) -> None:
    logger.info('start cfg')
    buttons = await database_get_blueprints_buttons(message_from_user)
    if buttons == []:
        CONFIG_KB = await create_config_keyboard(
            ['1 ячейка', '2 ячейка', '3 ячейка'], True, True)

    else:
        CONFIG_KB = await create_config_keyboard(buttons, True, False)

    message_for_user = 'Выберите шаблон или создайте новый.'
    await message_from_user.answer(message_for_user,reply_markup=CONFIG_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(message_for_user))


@database_handler()
async def create_blueprint_start(message_from_user: types.Message) -> None:
    logger.info('create')
    buttons = await database_get_blueprints_buttons(message_from_user)
    CONFIG_KB = await create_config_keyboard(buttons, False, False)

    message_for_user = 'Выберите ячейку для (пере-)записи.'
    await message_from_user.answer(message_for_user, reply_markup=CONFIG_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(message_for_user))


@database_handler()
async def choose_config_cells(message_from_user: types.Message) -> None:
    logger.info('choose')
    buttons = await database_get_blueprints_buttons(message_from_user)
    start_time = datetime.now()
    all_commands = await database_fetch_all_commands(message_from_user)
    print(all_commands)

    if all_commands[1][0].lower() == 'создать шаблон':
        message_for_user = 'Выберите последовательность шаблона'
        await message_from_user.answer(message_for_user, reply_markup=DAYS_OF_WEEK_KB)
        logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(message_for_user))
    
    elif all_commands[0][0].lower() != '1 ячейка' and all_commands[0][0].lower() != '2 ячейка' and all_commands[0][0].lower() != '3 ячейка':
        first_half_last_command = all_commands[0][0].split(' ')
        if first_half_last_command[0] == 'СН':

            schedule = await print_full_schedule(message_from_user.from_user.id,'следующая неделя', first_half_last_command[1].lower())
            if schedule == None:

                message_for_user = 'Непредвиденная ошибка'
                await message_from_user.answer(message_for_user, reply_markup=START_KB)
                logger.error(f'Ошибка в выводе расписания в choose_cells_handler, config.py, {traceback.format_exc()}')

            else:
        
                await message_from_user.answer(schedule, parse_mode="HTML")
                logger.info('Time of table out: ' + str(datetime.now() - start_time))
                logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(schedule))

        elif first_half_last_command[0] == 'ТН':

            schedule = await print_full_schedule(message_from_user.from_user.id,'текущая неделя', first_half_last_command[1].lower())
            if schedule == None:

                message_for_user = 'Непредвиденная ошибка'
                await message_from_user.answer(message_for_user, reply_markup=START_KB)
                logger.error(f'Ошибка в выводе расписания в choose_cells_handler, config.py, {traceback.format_exc()}')

            else:

                await message_from_user.answer(schedule, parse_mode="HTML")
                logger.info('Time of table out: ' + str(datetime.now() - start_time))
                logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(schedule))

        else:
            schedule = await print_schedule(message_from_user.from_user.id,first_half_last_command[0].lower(), first_half_last_command[1].lower())
            if schedule == None:

                message_for_user = 'Непредвиденная ошибка'
                await message_from_user.answer(message_for_user, reply_markup=START_KB)
                logger.error(f'Ошибка в выводе расписания в choose_cells_handler, config.py, {traceback.format_exc()}')

            else:
                await message_from_user.answer(schedule, parse_mode="HTML")
                logger.info('Time of table out: ' + str(datetime.now() - start_time))
                logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(schedule))

    else:
        message_for_user = 'Ячейка пуста'
        CONFIG_KB = await create_config_keyboard(buttons, True, False)
        await message_from_user.answer(message_for_user, reply_markup=CONFIG_KB)
        logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(message_for_user))


def register_handler_config(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(config_start, filters.Text(equals='Шаблоны расписания', ignore_case=True))
    bot_dispatcher.register_message_handler(create_blueprint_start, filters.Text(equals='Создать шаблон', ignore_case=True))
    bot_dispatcher.register_message_handler(choose_config_cells, filters.Text(startswith=BTNS_TO_CHOOSE_CELLS))
