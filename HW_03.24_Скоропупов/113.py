words = list()

while True:
    word = input('Введите слово => ')
    if word == '': #Тут наверное стоит проверить таким образом же, да? Тк 0 тоже при вводе станет False, а в задаче именно пустая строка
        break
    if word in words:
        continue
    else:
        words.append(word)

print(*words)
