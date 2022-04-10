from botrayado.keyboards.admin_kb import ADMIN_KB
from botrayado.keyboards.menu_kb import START_KB
from botrayado.schedule.sheethandler import print_full_schedule, print_schedule
from botrayado.database.db import database_handler
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.database.db import database_handler
from botrayado.utils.constants import USERSIDS
from botrayado.utils.logger import get_logger
import traceback


logger = get_logger(__name__)


@database_handler()
async def rayadotd(msg: types.Message) -> None:
    if str(msg.from_user.id) in USERSIDS:
        try:
            await msg.answer(await print_schedule("сегодня", "бвт2103"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("сегодня", "бст2103"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("сегодня", "бст2106"), reply_markup=ADMIN_KB)

        except Exception as e:
            logger.error(f'Ошибка в обращении к выводу одного дня, rayadotd, aliases.py{e}, {traceback.format_exc()}')
            await msg.answer('Непредвиденная ошибка, отправьте информацию запросов, с последнего вывода, разработчикам', reply_markup=START_KB)
    else:
        await msg.answer('Неправильная команда', reply_markup=START_KB)


@database_handler()
async def rayadotmr(msg: types.Message) -> None:
    if str(msg.from_user.id) in USERSIDS:
        try:
            await msg.answer(await print_schedule("завтра", "бвт2103"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("завтра", "бст2103"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("завтра", "бст2106"), reply_markup=ADMIN_KB)
        
        except Exception as e:
            logger.error(f'Ошибка в обращении к выводу одного дня, rayadotmr, aliases.py{e}, {traceback.format_exc()}')
            await msg.answer('Непредвиденная ошибка, отправьте информацию запросов, с последнего вывода, разработчикам', reply_markup=START_KB)
    else:
        await msg.answer('Неправильная команда', reply_markup=START_KB)


@database_handler()
async def fuckmaryamtd(msg: types.Message) -> None:
    if str(msg.from_user.id) in USERSIDS:
        try:
            await msg.answer(await print_schedule("сегодня", "бст2103"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("сегодня", "брт2101"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("сегодня", "бин2102"), reply_markup=ADMIN_KB)
        
        except Exception as e:
            logger.error(f'Ошибка в обращении к выводу одного дня, fuckmaryamtd, aliases.py{e}, {traceback.format_exc()}')
            await msg.answer('Непредвиденная ошибка, отправьте информацию запросов, с последнего вывода, разработчикам', reply_markup=START_KB)
    else:
        await msg.answer('Неправильная команда', reply_markup=START_KB)


@database_handler()
async def fuckmaryamtmr(msg: types.Message) -> None:
    if str(msg.from_user.id) in USERSIDS:
        try:
            await msg.answer(await print_schedule("завтра", "бст2103"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("завтра", "брт2101"), reply_markup=ADMIN_KB)
            await msg.answer(await print_schedule("завтра", "бин2102"), reply_markup=ADMIN_KB)
        
        except Exception as e:
            logger.error(f'Ошибка в обращении к выводу одного дня, fuckmaryamtmr, aliases.py{e}, {traceback.format_exc()}')
            await msg.answer('Непредвиденная ошибка, отправьте информацию запросов, с последнего вывода, разработчикам', reply_markup=START_KB)
    else:
        await msg.answer('Неправильная команда', reply_markup=START_KB)


@database_handler()
async def vanya(msg: types.Message) -> None:
    if str(msg.from_user.id) in USERSIDS:
        try:
            await msg.answer(await print_full_schedule("следующая неделя", "бвт2103"), reply_markup=ADMIN_KB)
        
        except Exception as e:
            logger.error(f'Ошибка в обращении к выводу всей недели, vanya, aliases.py{e}, {traceback.format_exc()}')
            await msg.answer('Непредвиденная ошибка, отправьте информацию запросов, с последнего вывода, разработчикам', reply_markup=START_KB)
    else:
        await msg.answer('Неправильная команда', reply_markup=START_KB)


def register_handlers_aliases(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(rayadotd, filters.Text(
        contains='rayadotd', ignore_case=True))
    bot_dispatcher.register_message_handler(rayadotmr, filters.Text(
        contains='rayadotmr', ignore_case=True))
    bot_dispatcher.register_message_handler(fuckmaryamtd, filters.Text(
        contains='fuckmaryamtd', ignore_case=True))
    bot_dispatcher.register_message_handler(fuckmaryamtmr, filters.Text(
        contains='fuckmaryamtmr', ignore_case=True))
    bot_dispatcher.register_message_handler(vanya, filters.Text(
        contains='ваня', ignore_case=True))
