from botrayado.schedule.whataweek import get_week
from transliterate import translit
from datetime import datetime, timedelta
from botrayado.utils.aiohttp_requests import aiohttp_fetch
from botrayado.utils.constants import DAYS_ENG, DAYS_RU
from botrayado.utils.constants import RESTIP, RESTPORT
from botrayado.utils.logger import get_logger
import traceback
import json


logger = get_logger(__name__)


async def print_schedule(day_type, group):

    day_time_utc = datetime.weekday(
        datetime.today().utcnow() + timedelta(hours=3))

    if day_type == 'завтра': day_time_utc += 1
    if day_time_utc == 6: return 'Занятий нет'
    if day_time_utc == 7: day_time_utc = 0

    try:
        week_checked = await get_week()

    except Exception as e:
        logger.error(f'Ошибка в определении недели, whataweek.py {e}, {traceback.format_exc()}')
        return None

    even = True if week_checked == 'четная' else False

    if week_checked == 'четная' and day_type == 'завтра' and day_time_utc == 0:
        even = False
        week_checked = 'нечетная'

    elif week_checked == 'нечетная' and day_type == 'завтра' and day_time_utc == 0:
        even = True
        week_checked = 'четная'

    try:
        output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
            + 'День недели: ' + DAYS_RU[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_checked.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'
        day_of_week = DAYS_ENG[day_time_utc] if day_type == 'завтра' else DAYS_ENG[day_time_utc]

    except Exception as e:
        logger.error(f'Ошибка связанная с заданием day_time_utc в sheethandler.py {e}, {traceback.format_exc()}')
        return None

    group = translit(group, language_code='ru', reversed=True)

    try:
        responce = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?group={group}&even={even}&day={day_of_week}'))
        output += responce['schedule']

    except Exception as e:
        logger.error(f'Ошибка в обращении к rest-service, print_schedule, sheethandler.py {e}, {traceback.format_exc()}')
        return None

    return output


async def print_full_schedule(day_type, group):

    try:
        week_checked = await get_week()

    except Exception as e:
        logger.error(f'Ошибка в определении недели, whataweek.py {e}, {traceback.format_exc()}')
        return None

    if week_checked == 'четная':
        if day_type == 'следующая неделя':
            even = False 
            week_checked = 'нечетная' 
        else:
            even = True
            week_checked = 'четная' 
    else:
        if day_type == 'следующая неделя':
            week_checked = 'четная'
            even = True 
        else:
            even = False
            week_checked = 'нечетная' 

    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
        + 'Неделя: ' + week_checked.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'
    group = translit(group, language_code='ru', reversed=True)

    try:
        responce = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?group={group}&even={even}'))
        for i in range(6):
            output += '\n' + DAYS_RU[i].capitalize() + '\n\n'
            output += responce['schedule'][i]['schedule']
            
    except Exception as e:
        logger.error(f'Ошибка в в обращении к rest-service, print_full_schedule, sheethandler.py {e}, {traceback.format_exc()}')
        return None

    return output
