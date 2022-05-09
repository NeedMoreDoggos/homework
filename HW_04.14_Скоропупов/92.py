def leap_year(year):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def ordinalDate(d, m, y):
    days = 0
    flag_leap = leap_year(y)
    days_in = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days_in[2] += int(flag_leap)
    if not m in days_in:
        print('Нет такого месяца')
        return
    if not 0 < d <= days_in[m]:
        print('Нет такого дня')
        return
    for i in range(1, m):
        days += days_in[i]
    return days + d


def date(y, d):
    flag_leap = leap_year(y)
    if flag_leap and d > 366:
        print('Слишком много дней')
        return
    if not flag_leap and d > 365:
        print('Слишком много дней')
        return
    days_in = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
    days_in[2] += int(flag_leap)
    month = 1
    while d > days_in[month]:
        d -= days_in[month]
        month += 1
    return d, month, y


# print(date(2000, 366))


def date_calc(d, m, y):
    last_date = ordinalDate(d, m, y) + 90
    flag_leap = leap_year(y)
    if last_date > 365 + int(flag_leap):
        y += 1
        last_date -= 365 + int(flag_leap)
    return date(y, last_date)


# print(f'1, 12, 1999 {date_calc(1, 12, 1999)}')


# 30, 1, 2000 (29, 4, 2000)
# 30, 12, 2000 (30, 3, 2001)
# 1, 12, 1999 (29, 2, 2000)
