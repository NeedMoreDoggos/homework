# print(input()[::-1]) Не проканало бы, да?


def re(number):
    new_number = 0
    i = 3
    while i > -1:
        new_number += number % 10 * 10**i
        i -= 1
        number //= 10
    return new_number


print(re(int(input())))
