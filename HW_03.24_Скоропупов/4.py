digits = [int(i) for i in input('Введите строку текста => ').split()]
how_many = 0

for i in range(len(digits)-1):
    if digits[i] < digits[i+1]:
        how_many += 1

print(how_many)
