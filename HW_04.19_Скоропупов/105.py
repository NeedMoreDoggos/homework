hexa_didgits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
digit_hexa = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def to_dec(number, n_system):
    sum = 0
    number = str(number)[::-1]

    for i in range(len(number)):
        sum += n_system ** i * hexa_didgits[number[i]]

    return sum


def dec_to(number, n_system):
    if int(number) < n_system:
        return digit_hexa[number]
    return f'{dec_to(int(number) // n_system, n_system) + digit_hexa[int((number)) % n_system]}'


def to_all(number, in_n_system, out_n_system):
    return  dec_to(to_dec(number, in_n_system), out_n_system)


print(to_all('4324324784782', 12, 16))

#print(to_all('11111111111111111', 10, 10))
#11111111111111111
# print(to_all('11111111111111111', 5, 14))
# 93357ADB7B
# print(to_all('4324324784782', 12, 16))
# 2298B58BFB52
