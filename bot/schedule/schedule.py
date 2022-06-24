from bot.utils.parity import get_week_parity
from bot.logger.logger import get_logger
from bot.utils.http import aiohttp_fetch
from bot.constants.schedule import DAYS_ENG, DAYS_RU
from bot.constants.enviroment import RESTIP, RESTPORT
from datetime import datetime, timedelta
from transliterate import translit
import traceback
import json


'''
*
Этот файл отвечает за получение и сборку в строку расписания, для последующего вывода
*
'''


logger = get_logger(__name__)


async def print_schedule(user_id: int, day_type: str, stream_group: str) -> str:

    '''Эта функция отвечает за сборку и вывод расписания на отдельный день, в частности сегодня или завтра'''

    day_time_utc = datetime.weekday(
        datetime.today().utcnow() + timedelta(hours=3))

    changed_day_time_utc = day_time_utc if day_type == 'сегодня' else day_time_utc + 1

    if changed_day_time_utc == 6:  return 'Занятий нет'

    if changed_day_time_utc == 7:  changed_day_time_utc = 0
    
    # Определяем какой день недели по счёту, начиная от нуля, изменяем в зависимости 
    # от полученного сегодня или завтра от пользователя

    week_parity_now = await get_week_parity()

    if week_parity_now == 'четная':
        if day_type == 'завтра' and changed_day_time_utc == 0:
            changed_week_parity = 'нечетная'
        else:
            changed_week_parity = week_parity_now

    elif week_parity_now == 'нечетная':
        if day_type == 'завтра' and changed_day_time_utc == 0:
            changed_week_parity = 'четная'
        else:
            changed_week_parity = week_parity_now

    else:
        logger.error('Ошибка в обращении к функции get_week_parity в whataweek.py')
        return 'Непредвиденная ошибка, информация отправленна разработчикам'
    # С помощью get_week_parity определяем четность недели и меняем её в зависимости
    # от нужного дня пользователю

    schedule = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
        + 'День недели: ' + DAYS_RU[changed_day_time_utc].capitalize() + '\n' + 'Неделя: ' \
        + changed_week_parity.capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'
    # Шапка расписания

    day_of_week = DAYS_ENG[changed_day_time_utc] # День недели транслитом для обращения к рест сервису

    try:
        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id=' \
        + f'{user_id}&stream_group={stream_group}&parity={changed_week_parity}&day={day_of_week}'))

        # Обращение к рест-сервису для получения расписания, записывается в responce, после добавляется
        # в итоговый вывод

        schedule += response["shared_schedule"][day_of_week]

    except Exception as e:
        logger.error("Ошибка в обращение к rest-service в функции print_schedule в sheethandler.py," \
        + " ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"

    return schedule


async def print_full_schedule(user_id: int, day_type: str, stream_group: str) -> str:
    
    '''Эта функция отвечает за сборку и вывод расписания на всю неделю, на текущую или следующую'''

    week_parity_now = await get_week_parity()

    if week_parity_now == 'четная':
        if day_type == 'следующая неделя':
            changed_week_parity = 'нечетная'
        else:
            changed_week_parity = 'четная'

    elif week_parity_now == 'нечетная':
        if day_type == 'следующая неделя':
            changed_week_parity = 'четная'
        else:
            changed_week_parity = 'нечетная'

    else:
        logger.error('Ошибка в обращении к функции get_week_parity в whataweek.py')
        return 'Ошибка в определении четности недели, сообщите разработчикам'
    # С помощью get_week_parity определяем четность недели и меняем её в зависимости
    # от выбранной пользователем недели

    schedule = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
        + 'Неделя: ' + changed_week_parity.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'
    # Шапка расписания 

    try:
        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id=' \
        + f'{user_id}&stream_group={stream_group}&parity={changed_week_parity}'))

        # Обращение к рест-сервису для получения расписания, записывается в responce, после добавляется
        # в итоговый вывод

        for i in range(6):
            schedule += str('<b>\n') + DAYS_RU[i].upper() + str(
                '</b>\n\n') + response["shared_schedule"][DAYS_ENG[i]]
                
    except Exception as e:
        logger.error("Ошибка в обращение к rest-service в функции print_full_schedule" \
        + " в sheethandler.py, ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"
    
    return schedule
