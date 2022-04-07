string = input().split()
sums = 0
for i in string:
    sums += len(i) * 80

print(f'{sums//100} руб. {sums%100} коп.')
