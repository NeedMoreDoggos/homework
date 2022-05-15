def prod(number):
    p = 1
    digits = [int(digit) for digit in number]
    for digit in digits:
        p *= digit
    return p


print(prod(input()))
