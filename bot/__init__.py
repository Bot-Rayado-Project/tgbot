from aiogram.utils import executor
from bot.handlers.menu import help_handler, start, donate, joke, menu, null
from bot.handlers.schedule import blueprints, schedule
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from bot.constants.enviroment import TOKEN