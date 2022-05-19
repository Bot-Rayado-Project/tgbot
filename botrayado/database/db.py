from botrayado.utils.constants import *
from aiogram import types
import typing
import sqlite3
from botrayado.utils.logger import get_logger
from botrayado.utils.constants import DBHOST, DBNAME, DBPASSWORD, DBPORT, DBUSER
import requests
import psycopg2


logger = get_logger(__name__)


def database_handler(ret_cfg: bool = False):
    def decorator(func: typing.Callable[..., typing.Any]):
        async def wrapper(msg: types.Message) -> str:
            
            sqlite_connection = psycopg2.connect(
                dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST)
            cursor = sqlite_connection.cursor()
            
            logger.info(f'Request: {msg.from_user.username} - {msg.text}')
            cursor.execute(ADD_COMMAND.format(
                msg.from_user.id, msg.text))
            sqlite_connection.commit()
            if ret_cfg:
                cursor.execute(
                    SELECT_CONFIG_KEYBOARD_BUTTONS.format(msg.from_user.id))
                btn = cursor.fetchall()
                if btn == []:
                    cursor.execute(
                        FIRST_ADD_CONFIG_BUTTONS.format(msg.from_user.id))
                    sqlite_connection.commit()
                    sqlite_connection.close()
                    # Вернет кнопки клавы с пустыми ячейками
                    return await func(msg, btn)
                else:
                    cursor.execute(
                        SELECT_CONFIG_KEYBOARD_BUTTONS.format(msg.from_user.id))
                    # Вернет кнопки клавы с чем то уже имеющимся
                    sqlite_connection.close()
                    return await func(msg, cursor.fetchall())
            else:
                sqlite_connection.close()
                return await func(msg)

        return wrapper
    return decorator


def set_button_blueprint(cmd: str, msg: types.Message, sc_btn: str) -> bool:
    
    sqlite_connection = psycopg2.connect(
        dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST)
    cursor = sqlite_connection.cursor()
    
    cursor.execute(
        SELECT_CONFIG_KEYBOARD_BUTTONS.format(msg.from_user.id))
    btn = cursor.fetchall()[0][0].split(', ')

    if sc_btn == btn[0]:
        cursor.execute(UPDATE_CONFIG_BUTTONS.format(
            cmd, btn[1], btn[2], msg.from_user.id))

    elif sc_btn == btn[1]:
        cursor.execute(UPDATE_CONFIG_BUTTONS.format(
            btn[0], cmd, btn[2], msg.from_user.id))

    elif sc_btn == btn[2]:
        cursor.execute(UPDATE_CONFIG_BUTTONS.format(
            btn[0], btn[1], cmd, msg.from_user.id))

    sqlite_connection.commit()
    sqlite_connection.close()


async def fetch_commands(msg: types.Message) -> list:
    
    sqlite_connection = psycopg2.connect(
        dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST)
    cursor = sqlite_connection.cursor()
    
    cursor.execute(SELLECT_ALL_COMMANDS.format(msg.from_user.id))
    cmd = cursor.fetchall()
    sqlite_connection.close()

    return cmd
