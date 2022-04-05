from aiogram import types, Dispatcher
from initialize_bot import bot
from keyboards.menu_kb import START_BUTTONS_PAYLOAD, START_KB

async def call_menu(callback: types.CallbackQuery):
    await callback.message.answer('Выберите кнопку из перечисленных.', reply_markup=START_KB)
    await callback.answer()
    

def register_handlers_menu(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_callback_query_handler(call_menu, text='menu')