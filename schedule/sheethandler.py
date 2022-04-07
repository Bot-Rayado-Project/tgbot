from schedule.whataweek import get_week
from transliterate import translit
from datetime import datetime, timedelta
from utils.aiohttp_requests import aiohttp_fetch
from utils.constants_schedule import DAYS_ENG, DAYS_RU
import json


async def print_schedule(day_type, group):

    day_time_utc = datetime.weekday(datetime.today().utcnow() + timedelta(hours=3))
    if day_type == 'завтра':
        day_time_utc += 1
    week_checked = await get_week()
    even = True if week_checked == 'четная' else False
    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
        + 'День недели: ' + DAYS_RU[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_checked.capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'
    group = translit(group, language_code='ru', reversed=True)

    if day_type == 'завтра':
        if day_time_utc == 6:
            day_of_week = DAYS_ENG[0]
        elif day_time_utc == 5:
            return 'Занятий нет'
        else:   
            day_of_week = DAYS_ENG[day_time_utc]
    else:
        if day_time_utc == 6:
            return 'Занятий нет'
        else:
            day_of_week = DAYS_ENG[day_time_utc]

    responce = json.loads(await aiohttp_fetch(url='http://rest-service-container:8000/{0}/{1}/{2}/{3}'.format(group, day_of_week, even, False)))
    output += responce['schedule']
    return output
async def print_full_schedule(day_type, group):

    week_checked = await get_week()
    if week_checked == 'четная':
        if day_type == 'следующая неделя':
            even = False
        else:
            even = True
    else:
        if day_type == 'следующая неделя':
            even = True
        else:
            even = False
    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
        + 'Неделя: ' + week_checked.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'
    group = translit(group, language_code='ru', reversed=True)

    responce = json.loads(await aiohttp_fetch(url='http://rest-service-container:8000/{0}/{1}/{2}/{3}'.format(group, 'ponedelnik', even, True)))

    for i in range(6):
        output += '\n' + DAYS_RU[i].capitalize() + '\n\n'
        output += responce['schedule'][i][0]
    return output
        