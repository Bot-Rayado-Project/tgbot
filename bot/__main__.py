from bot import *


bot = Bot(token=TOKEN)
bot_dispatcher = Dispatcher(bot)


schedule.register_handlers_schedule(bot_dispatcher)
start.register_handlers_start(bot_dispatcher)
joke.register_handlers_joke(bot_dispatcher)
help_handler.register_handlers_help(bot_dispatcher)
donate.register_handlers_donate(bot_dispatcher)
menu.register_handlers_menu(bot_dispatcher)
blueprints.register_handler_config(bot_dispatcher)
null.register_handlers_null(bot_dispatcher)
executor.start_polling(bot_dispatcher, skip_updates=True)
