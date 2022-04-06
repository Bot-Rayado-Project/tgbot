from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.menu_kb import START_KB
from utils.aiohttp_requests import aiohttp_fetch


async def joke(msg: types.Message):
    mesg = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await msg.answer(str(mesg), reply_markup=START_KB)


def register_handlers_joke(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(joke, filters.Text(contains=['Анекдот'], ignore_case=True))