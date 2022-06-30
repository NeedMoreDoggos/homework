import datetime
import time


def spy(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now().time().strftime("%H:%M:%S")
        try:
            with open('msg.txt', 'a', encoding='utf-8') as fon:
                fon.write(f'{now}     {args[0].name}: {args[1]}\n')
        except FileExistsError:
            pass
        return func(*args, **kwargs)
    return wrapper


class Person:
    def __init__(self, name, login, email):
        self.name = name
        self.login = login
        self.email = email


class TxtMsgSender:
    @staticmethod
    @spy
    def send(obj, msg):
        print(f'{obj.name}: {msg}')


a = Person('Dogs', 'good_boi', 'boi@dog.com')
TxtMsgSender.send(a, 'Hello')
#  Это для того, чтобы показать, что время пишет нормальное
time.sleep(5)
TxtMsgSender.send(a, 'How a u?')
time.sleep(5)
TxtMsgSender.send(a, '???')
