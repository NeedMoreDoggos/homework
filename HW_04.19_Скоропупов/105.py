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


def to_dec(number, n_system):
    sum = 0
    number = str(number)[::-1]
    for i in range(len(number)):
        sum += n_system ** i * hexa_didgits[number[i]]
    return sum


def dec_to(number, n_system):
    if int(number) < n_system:
        return str(number)
    return f'{dec_to(int(number) // n_system, n_system) + str(int(number) % n_system)}'

def to_all(number, in_n_system, out_n_sustem):
    pass


print(dec_to('1555', 12))
