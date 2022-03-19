# Задание 1


number_1 = float(input('Введите первое число '))

def odd_or_not(number):
    if number % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')

# odd_or_not(number)


# Задание 2


def age(age):
    if age >= 0 and 13 >= age:
        print('Детство')
    elif 24 >= age and age >= 14:
        print('Молодость')
    elif 59 >= age and age >= 25:
        print('Зрелость')
    elif age >= 60:
        print('Старость')
    else:
        print('Некорректный возраст')

# age(number)


# Задание 3


number_2 = float(input('Введите второе число '))


def number_magic(number_1, number_2):
    if number_1 % number_2 == 0:
        print(f"{number_1} делится на {number_2} нацело\nЧастное: {int(number_1 / number_2)}")
    else:
        print(f"{number_1} не делится на {number_2} нацело\nЧастное: {int(number_1 / number_2)}\nОстаток: {number_1 % number_2}")


# number_magic(number_1, number_2)


#Задание 4


number_3 = float(input('Введите третье число '))


def neg(number):
    if number <= 0:
        return 0
    else:
        return number


def sum_pos(number_1, number_2, number_3):
    return neg(number_1) + neg(number_2) + neg(number_3)


print(sum_pos(number_1, number_2, number_3))
