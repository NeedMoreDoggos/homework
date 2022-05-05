digits = list()
sums = 0

while True:
    digit = input('Введите цифирь => ')
    if digit == '':
        break
    if not digit.isdigit():
        print('Это не цифирь :<')
        continue
    digit = int(digit)
    sums += digit
    digits.append(digit)

mid = sums / len(digits)

print(f'Среднее значение == {mid}')
print(f'Списочек <= {mid}')
print(*[i for i in digits if i <= mid], sep='\n')
print(f'Списочек > {mid}')
print(*[i for i in digits if i > mid], sep='\n')
