import datetime

def conv_time(my_time: datetime.timedelta) -> str:
    minute = str(my_time).split(":")[1].lstrip("0")
    sec = round(float(str(my_time).split(":")[-1]))
    if minute:
        out_time: str = f'{minute} мин. {sec} сек.'
    else:
        out_time: str = f'{sec} сек.'
    return out_time

def out_answers():
    pass
