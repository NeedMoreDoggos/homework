sums = []
reps = []
lucky_tickets = 0
index = -1
item = None

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            sums += [i + j + k]

sums.sort()

for i in range(len(sums)):
    if item != sums[i]:
        item = sums[i]
        index += 1
        reps += [1]
    else:
        reps[index] += 1

for i in reps:
    lucky_tickets += i ** 2

lucky_tickets -= 1 #Тут ответ если существует билет 000 000. => Нужно отнять один.

print(lucky_tickets)
# PEP8 Прочту на следующей неделе.
