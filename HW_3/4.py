def sums_dividers(n:int):
    sum = 0

    for i in range(1, n // 2 + 1): #единица и само число считаются делителями?
        if n%i == 0:
            sum += i

    return sum


print(sums_dividers(int(input('Введите число\n'))))
