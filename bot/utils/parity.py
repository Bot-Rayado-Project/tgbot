from datetime import datetime, timedelta


'''
*
Этот файл отвечает за определение чётности недели, одна единственная функция
*
'''


async def get_week_parity() -> str:

    date = datetime.date(datetime.today() + timedelta(hours=3))
    month = str(date)[5:7]
    month = int(str(date)[6:7]) if month[0] == '0' else int(str(date)[5:7])
    format = "%Y-%m-%d"
    past_year = str(int(str(datetime.date(datetime.today() + timedelta(hours=3)))[:4]) - 1)
    current_year = str(datetime.date(datetime.today() + timedelta(hours=3)))[:4]
    
    try:
        if month < 9:
            number_of_week_now = date.isocalendar()[1]
            weeks_in_past_year = datetime.strptime('{}-12-31'.format(past_year), format).isocalendar()[1] \
            - datetime.strptime('{}-09-01'.format(past_year), format).isocalendar()[1] + 1
            number_of_week_now += weeks_in_past_year

        if month >= 9:
            number_of_week_now = date.isocalendar()[1]
            weeks_in_past_semestr = datetime.strptime(date, format).isocalendar()[1] \
            - datetime.strptime('{}-09-01'.format(current_year), format).isocalendar()[1] + 1
            number_of_week_now += weeks_in_past_semestr

    except Exception as e:
        logger.error(
            f"Ошибка в определении четности недели, get_week в whataweek.py ({e}): {traceback.format_exc()}")
        return 'ошибка'

    return 'четная' if number_of_week_now % 2 == 0 else 'нечетная'
