from botrayado.schedule.whataweek import get_week_parity
from botrayado.utils.logger import get_logger
from botrayado.utils.http_request import aiohttp_fetch
from botrayado.utils.constants import DAYS_ENG, DAYS_RU, RESTIP, RESTPORT
from datetime import datetime, timedelta
from transliterate import translit
import traceback
import json

logger = get_logger(__name__)





async def print_schedule(user_id: int, day_type: str, stream_group: str) -> str:

    day_time_utc = datetime.weekday(
        datetime.today().utcnow() + timedelta(hours=3))
    changed_day_time_utc = day_time_utc if day_type == 'сегодня' else day_time_utc + 1
    if changed_day_time_utc == 6:  return 'Занятий нет'
    if changed_day_time_utc == 7:  changed_day_time_utc = 0

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
        return 'Ошибка в определении четности недели, сообщите разработчикам'

    schedule = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
        + 'День недели: ' + DAYS_RU[changed_day_time_utc].capitalize() + '\n' + 'Неделя: ' \
        + changed_week_parity.capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'

    day_of_week = DAYS_ENG[changed_day_time_utc]

    try:
        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id='+\
        f'{user_id}&stream_group={stream_group}&parity={changed_week_parity}&day={day_of_week}'))
        schedule += response["shared_schedule"][day_of_week]

    except Exception as e:
        logger.error("Ошибка в обращение к rest-service в функции print_schedule в sheethandler.py,"+\ 
        " ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"

    return schedule


async def print_full_schedule(user_id: int, day_type: str, stream_group: str) -> str:

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

    schedule = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
        + 'Неделя: ' + changed_week_parity.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'

    try:
        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={user_id}&stream_group={stream_group}&parity={changed_week_parity}'))
        for i in range(6):
            schedule += str('<b>\n') + DAYS_RU[i].upper() + str(
                '</b>\n\n') + response["shared_schedule"][DAYS_ENG[i]]
                
    except Exception as e:
        logger.error("Ошибка в обращение к rest-service в функции print__full_schedule в sheethandler.py, ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"
    
    return schedule
