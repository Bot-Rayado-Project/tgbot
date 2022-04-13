from botrayado.utils.constants import *
from aiogram import types
import typing
import sqlite3
from botrayado.utils.logger import get_logger


logger = get_logger(__name__)


def set_up_connection_with_db(data_base_name: str) -> tuple | None:
    try:
        sqlite_connection: sqlite3.Connection = sqlite3.connect(data_base_name)
        return sqlite_connection, sqlite_connection.cursor()

    except sqlite3.Error:
        logger.error("Не удалось подключиться к базе данных users.db")
        exit()


sqlite_connection, cursor = set_up_connection_with_db("botrayado/database/db/users.db")


def database_handler(ret_cfg: bool = False):
    def decorator(func: typing.Callable[..., typing.Any]):
        async def wrapper(msg: types.Message) -> str:

            logger.info(f'Request: {msg.from_user.username} - {msg.text}')
            cursor.execute(ADD_COMMAND.format(msg.from_user.id, msg.text))
            sqlite_connection.commit()
            if ret_cfg:
                cursor.execute(SELECT_CONFIG_KEYBOARD_BUTTONS.format(msg.from_user.id))
                btn = cursor.fetchall()
                if btn == []:
                    cursor.execute(FIRST_ADD_CONFIG_BUTTONS.format(msg.from_user.id))
                    sqlite_connection.commit()
                    return await func(msg, btn)  # Вернет кнопки клавы с пустыми ячейками
                else:
                    cursor.execute(SELECT_CONFIG_KEYBOARD_BUTTONS.format(msg.from_user.id))
                    return await func(msg, cursor.fetchall())  # Вернет кнопки клавы с чем то уже имеющимся
            else:
                return await func(msg)

        return wrapper
    return decorator


def set_button_blueprint(cmd: str, msg: types.Message, sc_btn: str) -> bool:

    cursor.execute(SELECT_CONFIG_KEYBOARD_BUTTONS.format(msg.from_user.id))
    btn = cursor.fetchall()[0][0].split(', ')

    if sc_btn == btn[0]:
        cursor.execute(UPDATE_CONFIG_BUTTONS.format(cmd, btn[1], btn[2], msg.from_user.id))

    elif sc_btn == btn[1]:
        cursor.execute(UPDATE_CONFIG_BUTTONS.format(btn[0], cmd, btn[2], msg.from_user.id))

    elif sc_btn == btn[2]:
        cursor.execute(UPDATE_CONFIG_BUTTONS.format(btn[0], btn[1], cmd, msg.from_user.id))

    sqlite_connection.commit()