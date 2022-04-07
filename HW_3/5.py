def print_row():
    sum = ''

    while True:
        n = input('Введите число\n')
        sum += n + ' '
        if int(n)%7 != 0:
            return sum


print(print_row())
