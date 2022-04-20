from aiogram.utils import executor
from initialize_bot import bot_dispatcher
from botrayado.handlers import start, donate, _help, joke, schedule, menu, config, null, admin, aliases


f = open('logs.log', 'w')
f.write('Bot started')
f.close()


start.register_handlers_start(bot_dispatcher)
joke.register_handlers_joke(bot_dispatcher)
_help.register_handlers_help(bot_dispatcher)
start.register_handlers_start(bot_dispatcher)
donate.register_handlers_donate(bot_dispatcher)
menu.register_handlers_menu(bot_dispatcher)
schedule.register_handlers_schedule(bot_dispatcher)
config.register_handler_config(bot_dispatcher)
admin.register_handlers_admin(bot_dispatcher)
aliases.register_handlers_aliases(bot_dispatcher)
null.register_handlers_null(bot_dispatcher)
executor.start_polling(bot_dispatcher, skip_updates=True)

