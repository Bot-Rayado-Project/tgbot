import botrayado.utils.constants as constants
import botrayado.keyboards.headman_kb as headman_kb
import botrayado.keyboards.schedule_kb as schedule_kb
import botrayado.keyboards.menu_kb as menu_kb
import botrayado.schedule.sheethandler as sheethandler

from aiogram import types, Dispatcher
from aiogram.dispatcher import filters

from botrayado.database.db import database_handler
from botrayado.utils.logger import get_logger

logger = get_logger(__name__)


@database_handler()
async def start(msg: types.Message) -> str:
    if constants.headmans_ids.get(msg.from_user.id) is not None:
        await msg.answer('Выберите неделю', reply_markup=headman_kb.CHOOSE_WEEK_KB)
    else:
        await msg.answer('Доступа нет. До свидания', reply_markup=schedule_kb.DAYS_OF_WEEK_KB)


@database_handler()
async def choose_day(msg: types.Message) -> str:
    constants.headman_requests[msg.from_user.id] = constants.HeadmanRequest(msg.text)  # Неделя
    await msg.answer('Выберите день недели', reply_markup=headman_kb.CHOOSE_DAY_OF_WEEK_KB)


@database_handler()
async def print_day_schedule(msg: types.Message) -> str:
    constants.headman_requests[msg.from_user.id] = constants.HeadmanRequest(constants.headman_requests[msg.from_user.id].week, msg.text)  # День недели
    if constants.headman_requests[msg.from_user.id].week.lower() == 'обе':
        schedule = ''
        await msg.answer(f'Текущее расписание на выбранные дни:', reply_markup=headman_kb.CHOOSE_PAIR_KB)
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[msg.from_user.id].lower(),
                                                             constants.headman_requests[msg.from_user.id].dayofweek.lower(),
                                                             True)
        await msg.answer(schedule, reply_markup=headman_kb.CHOOSE_PAIR_KB)
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[msg.from_user.id].lower(),
                                                             constants.headman_requests[msg.from_user.id].dayofweek.lower(),
                                                             False)
        await msg.answer(schedule, reply_markup=headman_kb.CHOOSE_PAIR_KB)
    else:
        even = True if constants.headman_requests[msg.from_user.id].week.lower() == 'четная' else False
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[msg.from_user.id].lower(),
                                                            constants.headman_requests[msg.from_user.id].dayofweek.lower(),
                                                            even)
        await msg.answer(f'Текущее расписание на выбранный день: \n {schedule}', reply_markup=headman_kb.CHOOSE_PAIR_KB)
    await msg.answer('Выберите пару для редактирования либо 6-ую кнопку для добавления общей аннотации ко дню', reply_markup=headman_kb.CHOOSE_PAIR_KB)


@database_handler()
async def option_select(msg: types.Message) -> str:
    constants.headman_requests[msg.from_user.id] = constants.HeadmanRequest(constants.headman_requests[msg.from_user.id].week,
                                                                         constants.headman_requests[msg.from_user.id].dayofweek,
                                                                         msg.text)  # Пара
    await msg.answer('Выберите опцию - удалить пару или перезаписать.', reply_markup=headman_kb.CHOOSE_MOVE_KB)



@database_handler()
async def deleted_pair(msg: types.Message) -> str:
    constants.headman_requests[msg.from_user.id] = constants.HeadmanRequest(constants.headman_requests[msg.from_user.id].week,
                                                                         constants.headman_requests[msg.from_user.id].dayofweek,
                                                                         constants.headman_requests[msg.from_user.id].pair,
                                                                         msg.text)  # Действие
    logger.info(constants.headman_requests[msg.from_user.id])
    if msg.text.lower() == 'удалить':
        await msg.answer('Пара успешно удалена', reply_markup=menu_kb.START_KB)
    else:
        await msg.answer('Введите изменения')


@database_handler()
async def annotains(msg: types.Message) -> str:
    await msg.answer('Look', reply_markup=menu_kb.START_KB)


def register_handlers_headman(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        start, filters.Text(equals='Редактировать расписание', ignore_case=True))
    bot_dispatcher.register_message_handler(
        annotains, filters.Text(equals='Посмотреть аннотации', ignore_case=True))
    bot_dispatcher.register_message_handler(
        choose_day, filters.Text(equals=constants.WEEKS, ignore_case=True))
    bot_dispatcher.register_message_handler(
        print_day_schedule, filters.Text(equals=constants.DAYS_RU, ignore_case=True))
    bot_dispatcher.register_message_handler(
        option_select, filters.Text(equals=constants.PAIRS, ignore_case=True))
    bot_dispatcher.register_message_handler(
        deleted_pair, filters.Text(equals=constants.DLT, ignore_case=True))