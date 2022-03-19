number_1 = 1
number_2 = 2
letter_1 = 'a'
letter_2 = 'b'

def odd_or_not(number):
    if number % 2 == 0:
        return 0
    else:
        return 1

def what_is_letter(letter):
    if letter == 'a' or letter == 'c' or letter == 'e' or letter == 'g':
        return 1
    else:
        return 0

# Черные (1, 1) или (0, 0), белые все остальные


def contact(number, letter):
    return str(odd_or_not(number)) + str(what_is_letter(letter))


def color(con):
    if (con == '11') or (con == '00'):
        return 1
    else:
        return 0


def color_check(number_1, letter_1, number_2, letter_2):
    col_1 = color(contact(number_1, letter_1))
    col_2 = color(contact(number_2, letter_2))
    if col_1 == col_2:
        print('Цвет один')
        return 1
    else:
        print('Разные цвета')
        return 0

a = color_check(number_1, letter_1, number_2, letter_2)

print(a)
