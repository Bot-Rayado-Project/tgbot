from aiogram.utils import executor
from initialize_bot import bot_dispatcher
from handlers import start, donate, _help, joke
from utils.terminal_codes import print_info

print_info('Bot started')


start.register_handlers_start(bot_dispatcher)
joke.register_handlers_joke(bot_dispatcher)
_help.register_handlers_help(bot_dispatcher)
start.register_handlers_start(bot_dispatcher)
donate.register_handlers_donate(bot_dispatcher)
executor.start_polling(bot_dispatcher, skip_updates=True)

