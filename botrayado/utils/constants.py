import os
from typing import NamedTuple
from botrayado.keyboards.schedule_kb import GROUP_BFI_KB
from botrayado.keyboards.schedule_kb import GROUP_BVT_KB
from botrayado.keyboards.schedule_kb import GROUP_BST_KB
from botrayado.keyboards.schedule_kb import GROUP_BEI_KB
from botrayado.keyboards.schedule_kb import GROUP_BIB_KB
from botrayado.keyboards.schedule_kb import GROUP_BAP_KB
from botrayado.keyboards.schedule_kb import GROUP_BMP_KB
from botrayado.keyboards.schedule_kb import GROUP_BUT_KB
from botrayado.keyboards.schedule_kb import GROUP_ZRC_KB
from botrayado.keyboards.schedule_kb import GROUP_BRT_KB
from botrayado.keyboards.schedule_kb import GROUP_BIK_KB
from botrayado.keyboards.schedule_kb import GROUP_BEE_KB
from botrayado.keyboards.schedule_kb import GROUP_BER_KB
from botrayado.keyboards.schedule_kb import GROUP_BBI_KB
from botrayado.keyboards.schedule_kb import GROUP_BIN_KB
from botrayado.keyboards.schedule_kb import STREAM_IT_KB
from botrayado.keyboards.schedule_kb import STREAM_TSEIMK_KB
from botrayado.keyboards.schedule_kb import STREAM_RIT_KB
from botrayado.keyboards.schedule_kb import STREAM_KIIB_KB
from botrayado.keyboards.schedule_kb import STREAM_SISS_KB

DAYS_OF_WEEK = ['Сегодня', 'Завтра', 'Вся неделя', 'Текущая неделя', 'Следующая неделя']
FACULTIES = ['ИТ', 'КиИБ', 'РиТ', 'ЦЭиМК', 'СиСС']
STREAMS = ['БВТ', 'БФИ', 'БСТ', 'БЭИ', 'БИБ', 'БМП', 
'ЗРС', 'БАП', 'БУТ', 'БРТ', 'БИК', 'ББИ', 'БЭЭ', 'БЭР', 'БИН']
GROUPS = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 
'бвт2106', 'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105',
'бст2106', 'бэи2101', 'бэи2102', 'бэи2103', 'биб2101', 'биб2102', 'биб2103', 'биб2104',
'бап2101', 'бмп2101', 'бут2101', 'бээ2101', 'бэр2101', 'бби2101', 'зрс2101', 'зрс2102',
'брт2101', 'брт2102', 'бик2101', 'бик2102', 'бик2103', 'бик2104', 'бик2105', 'бик2106',
'бик2107', 'бик2108', 'бик2109', 'бин2101', 'бин2102', 'бин2103', 'бин2104', 'бин2105',
'бин2106', 'бин2107', 'бин2108', 'бин2109', 'бин2110']
FACULTIES_KB_BUTTONS = {
    'ИТ': STREAM_IT_KB,
    'КИИБ': STREAM_KIIB_KB,
    'РИТ': STREAM_RIT_KB,
    'СИСС': STREAM_SISS_KB,
    'ЦЭИМК': STREAM_TSEIMK_KB}
STREAMS_KB = {
    'бвт': GROUP_BVT_KB,
    'бфи': GROUP_BFI_KB,
    'бст': GROUP_BST_KB,
    'бэи': GROUP_BEI_KB,
    'биб': GROUP_BIB_KB,
    'бмп': GROUP_BMP_KB,
    'зрс': GROUP_ZRC_KB,
    'бап': GROUP_BAP_KB,
    'бут': GROUP_BUT_KB,
    'брт': GROUP_BRT_KB,
    'бик': GROUP_BIK_KB,
    'бби': GROUP_BBI_KB,
    'бээ': GROUP_BEE_KB,
    'бэр': GROUP_BER_KB,
    'бин': GROUP_BIN_KB
}


USERSIDS = os.environ.get('USERSIDS').split()
TOKEN = os.environ.get('TOKEN')
EADRESS = os.environ.get('EADRESS')
EPASSWORD = os.environ.get('EPASSWORD')
DEBUG = os.environ.get('DEBUG') or False
RESTIP = os.environ.get('RESTIP') or 'localhost'
RESTPORT = os.environ.get('RESTPORT') or '8000'
VOLUMENAME = os.environ.get('VOLUMENAME')


# Команды SQLITE
ADD_COMMAND: str = 'INSERT INTO users VALUES({0}, (STRFTIME("%Y-%m-%d %H:%M:%f", "NOW")), "{1}");'
FIRST_ADD_CONFIG_BUTTONS: str = 'INSERT INTO config VALUES({0}, "1 ячейка, 2 ячейка, 3 ячейка");'  # Вызывается только первый раз для каждого пользователя.
UPDATE_CONFIG_BUTTONS: str = 'UPDATE config SET keyboard_buttons = "{0}, {1}, {2}" where user_id={3};'  # Обновить кнопки по записи.
SELECT_CONFIG_KEYBOARD_BUTTONS: str = 'SELECT keyboard_buttons FROM config WHERE user_id={0};'
SELLECT_ALL_COMMANDS: str = "SELECT command FROM users WHERE user_id={0} ORDER BY date DESC;"


DAYS_ENG = ['ponedelnik', 'vtornik', 'sreda', 'chetverg', 'pjatnitsa', 'subbota']
DAYS_RU = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
DLT = ['перезаписать', 'удалить']
PAIRS = ['1 пара', '2 пара', '3 пара', '4 пара', '5 пара', 'весь день']
WEEKS = ['четная', 'нечетная', 'обе']


class HeadmanRequest(NamedTuple):
    week: str = None
    dayofweek: str = None
    pair: str = None
    move: str = None
    changes: str = None


headman_requests = {}

# Старосты

headmans_ids: dict = {489684053: 'бвт2103'}