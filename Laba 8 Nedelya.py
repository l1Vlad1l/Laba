import datetime


def curr_week():
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year
    a = datetime.datetime(year, month, 1)
    first_day = datetime.datetime.weekday(a)
    week_count = 0
    for i in range(1, day + 1):
        first_day += 1
        if first_day == 6:
            week_count += 1
            first_day = 0
    if week_count % 2 == 0:
        return "нечетная"
    else:
        return "четная"


def curr_week_for_bd(x):
    if x == 1:
        if curr_week() == "нечетная":
            return 2
        else:
            return 1
    if curr_week() == "нечетная":
        return 1
    else:
        return 2