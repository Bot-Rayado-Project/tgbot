from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from botrayado.utils.constants import TOKEN

bot = Bot(token=TOKEN)
bot_dispatcher = Dispatcher(bot)