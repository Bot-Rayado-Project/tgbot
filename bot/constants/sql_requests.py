'''
*
Файл с sql запросами
*
'''


ADD_COMMAND: str = "INSERT INTO users VALUES({0}, NOW(), '{1}');"
FIRST_ADD_CONFIG_BUTTONS: str = "INSERT INTO config VALUES({0}, '1 ячейка, 2 ячейка, 3 ячейка');"
UPDATE_CONFIG_BUTTONS: str = "UPDATE config SET keyboard_buttons = '{0}, {1}, {2}' where user_id={3};"
SELECT_CONFIG_KEYBOARD_BUTTONS: str = "SELECT keyboard_buttons FROM config WHERE user_id={0};"
SELECT_ALL_COMMANDS: str = "SELECT command FROM users WHERE user_id={0} ORDER BY date DESC;"