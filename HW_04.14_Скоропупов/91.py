def leap_year(year):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def ordinalDate(d, m, y):
    days = 0
    flag_leap = leap_year(y) # Я знаю, что можно не создавать эту переменную, просто для того, чтобы не путаться
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
    days_in[2] += int(flag_leap) # Я знаю, что интовать не обязательно. Просто путаюсь в типах. Так нагляднее
    if not m in days_in:
        print('Нет такого месяца')
        return
    if not 0 < d <= days_in[m]:
        print('Нет такого дня')
        return
    for i in range(1, m):
        days += days_in[i]
    return days + d


print(ordinalDate(31, 12, 2000))

#  29.2.2000 = 60; 31.12.2000 = 366
