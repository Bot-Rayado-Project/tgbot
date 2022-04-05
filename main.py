from aiogram.utils import executor
from initialize_bot import bot_dispatcher
from handlers import commands_slash, menu
from utils.terminal_codes import print_info

print_info('Bot started')
commands_slash.register_handler_commands_slash(bot_dispatcher)
menu.register_handlers_menu(bot_dispatcher)
executor.start_polling(bot_dispatcher, skip_updates=True)
