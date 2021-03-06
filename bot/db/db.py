from aiogram import types
from bot.constants.sql_requests import *
from bot.constants.enviroment import *
from bot.logger.logger import get_logger
import traceback
import typing
import asyncpg


'''
*
Это файл отвечает за все взаимодействия с базой данных только телеграм бота
*
'''


logger = get_logger(__name__)


async def database_connection(user: str, password: str, name: str, host: str) -> asyncpg.Connection | None:

    '''Эта функция устанавливает соединение с базой данных'''

    try:
        connection = await asyncpg.connect(user=user, password=password, database=name, host=host)
        logger.info(
            f'Successfully connected to database {name} to host {host} with user {user}')
        return connection

    except Exception as e:
        logger.error(
            f"Error connecting to database: {traceback.format_exc()}")
        return None


async def database_connection_close(connection: asyncpg.Connection) -> None:

    '''Эта функция закрывает соединение с базой данных'''

    try:
        await connection.close()
    
    except Exception as e:
        logger.error(f'Error in close connection to databasse: {traceback.format_exc()}')


async def database_get_blueprints_buttons(message_from_user: types.Message) -> list | None | bool:
    
    '''Эта функция получает кнопки шаблонов из баз данных'''

    connection = await database_connection(DBUSER, DBPASSWORD, DBNAME, DBHOST)
    if connection == None: return False

    buttons_in_db = await connection.fetch(
        SELECT_CONFIG_KEYBOARD_BUTTONS.format(message_from_user.from_user.id))
    # Получает кнопки по айди пользователя
    if buttons_in_db == []:
       await connection.fetch(
            FIRST_ADD_CONFIG_BUTTONS.format(message_from_user.from_user.id))
    # Добавляет кнопки если он впервые создаёт шаблоны

    await database_connection_close(connection)

    return buttons_in_db


async def database_set_button_blueprint(new_button: str, message_from_user: types.Message, old_button: str) -> None | bool:
    
    '''Эта функция устанавливает новую кнопку шаблона, сохраняя её вместо старой в базе данных'''

    connection = await database_connection(DBUSER, DBPASSWORD, DBNAME, DBHOST)
    if connection == None: return False
    
    buttons_in_db = (await connection.fetch(
        SELECT_CONFIG_KEYBOARD_BUTTONS.format(message_from_user.from_user.id)))[0][0].split(', ')

    if old_button == buttons_in_db[0]:
        await connection.fetch(UPDATE_CONFIG_BUTTONS.format(
            new_button, buttons_in_db[1], buttons_in_db[2], message_from_user.from_user.id))

    elif old_button == buttons_in_db[1]:
        await connection.fetch(UPDATE_CONFIG_BUTTONS.format(
            buttons_in_db[0], new_button, buttons_in_db[2], message_from_user.from_user.id))

    elif old_button == buttons_in_db[2]:
        await connection.fetch(UPDATE_CONFIG_BUTTONS.format(
            buttons_in_db[0], buttons_in_db[1], new_button, message_from_user.from_user.id))

    # Сверяем какой кнопке соответсвует выбранная пользователем и перезаписываем

    await database_connection_close(connection)


async def database_fetch_all_commands(message_from_user: types.Message) -> list | bool:
    
    '''Эта функция заносит все команды ранее введённые пользователем в список'''

    connection = await database_connection(DBUSER, DBPASSWORD, DBNAME, DBHOST)
    if connection == None: return False

    all_user_commands = await connection.fetch(SELECT_ALL_COMMANDS.format(message_from_user.from_user.id))
    await database_connection_close(connection)

    return all_user_commands


def database_handler():
    def decorator(func: typing.Callable[..., typing.Any]):
        async def wrapper(message_from_user: types.Message) -> str | bool:

            '''Эта декоратор для сохранения каждой команды в базу данных и параллельной записи в логи запроса'''
            
            connection = await database_connection(DBUSER, DBPASSWORD, DBNAME, DBHOST)
            if connection == None: return func(message_from_user, False)

            logger.info(f'Request: {message_from_user.from_user.username} - {message_from_user.text}')
            await connection.fetch(ADD_COMMAND.format(
                message_from_user.from_user.id, message_from_user.text))
            await database_connection_close(connection)
            return await func(message_from_user)

        return wrapper
    return decorator
