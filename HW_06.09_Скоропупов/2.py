from datetime import datetime, timedelta


class Moment:
    def __init__(self):
        self.date = datetime.now()

    # Предположу, что у нас 0 часовой пояс и находимся мы в Лондоне
    def moment_in_tz(self, tz: int) -> datetime:
        if tz in range(-12, 13, 1):
            return self.date + timedelta(hours=tz)
        raise ValueError('Часовые пояса от -12, до 12 включительно')

    def time_of_day(self, tz) -> None:
        hours = self.moment_in_tz(tz).hour

        if 0 <= hours < 6:
            print('Ночь')
        elif 6 <= hours < 12:
            print('Утро')
        elif 12 <= hours < 18:
            print('День')
        elif 18 <= hours < 24:
            print('Вечер')
        else:
            raise Exception('Случилось невероятное')

    def upd(self) -> None:
        self.date = datetime.now()


happy_moment = Moment()
happy_moment.upd()
happy_moment.time_of_day(7)
happy_moment.time_of_day(122)
# Утро
# Traceback (most recent call last):
#   File "E:\git\homework\HW_06.09_Скоропупов\2.py", line 34, in <module>
#     happy_moment.time_of_day(122)
#   File "E:\git\homework\HW_06.09_Скоропупов\2.py", line 15, in time_of_day
#     hours = self.moment_in_tz(tz).hour
#   File "E:\git\homework\HW_06.09_Скоропупов\2.py", line 12, in moment_in_tz
#     raise ValueError('Часовые пояса от -12, до 12 включительно')
# ValueError: Часовые пояса от -12, до 12 включительно
