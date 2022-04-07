def positive_sum(n:int):
    sum = 0

    for i in range(n):
        number = int(input('Введите число\n'))
        if number > 0:
            sum += number

    return sum


print(positive_sum(int(input('Введите колличество цифирей\n'))))
