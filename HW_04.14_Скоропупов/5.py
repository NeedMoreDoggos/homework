from random import randrange


def am(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def gm(numbers):
    prod = 1
    for number in numbers:
        prod *= number
    return  prod ** (1 / len(numbers))


def ms(numbers):
    sum = 0
    for number in numbers:
        sum += number ** 2
    return (sum / len(numbers)) ** (1 / 2)


def hm(numbers):
    sum = 0
    for number in numbers:
        sum += 1 / number
    return len(numbers) / sum


def mid(arg):
    print(arg, type(arg))
    if not isinstance(arg, (str, list, tuple)):
        return
    if isinstance(arg, str):
        arg = [int(i) for i in arg.split()]
    values = {
        'am': am(arg),
        'gm': gm(arg),
        'ms': ms(arg),
        'hm': hm(arg)
    }
    return values


print(mid([randrange(1, 100) for _ in range(100)]))


# (1, 2, 3, 4, 5) <class 'tuple'>
# {'am': 3.0, 'gm': 2.605171084697352, 'ms': 3.3166247903554, 'hm': 2.18978102189781}
# PS D:\Git\homework\HW_04.14_Скоропупов> py 5.py
# 1 2 3 4 5 <class 'str'>
# {'am': 3.0, 'gm': 2.605171084697352, 'ms': 3.3166247903554, 'hm': 2.18978102189781}
# [1, 21, 5, 53, 22, 53, 94, 2, 43, 11, 13, 31, 94, 42, 35, 83, 67, 30, 60, 89, 42, 82, 31, 13, 49, 51, 83, 62, 86, 99, 59, 89, 31, 82, 94, 25, 26, 92, 46, 40, 86, 62, 54, 1
# 9, 58, 87, 78, 7, 50, 67, 17, 7, 44, 26, 98, 84, 36, 51, 80, 58, 77, 94, 37, 9, 86, 7, 43, 22, 36, 18, 42, 86, 16, 33, 99, 91, 34, 87, 92, 51, 65, 85, 79, 67, 97, 17, 25,
# 93, 18, 30, 48, 95, 82, 32, 89, 80, 80, 61, 55, 41] <class 'list'>
# {'am': 53.99, 'gm': 42.21067363380052, 'ms': 61.36130702649675, 'hm': 22.35462128298347}
# 1.0 <class 'float'>
# None
