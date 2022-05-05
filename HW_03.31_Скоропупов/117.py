string = input('Введите строку => ')


def remover1(word):
    removed = '.,!?-":;'
    for i in removed:
        word = word.replace(i, '').strip()
    return word


def remover2(word):
    if not word or word[0] != "'" and word[-1] != "'":
        return word
    if word[0] == "'":
        return remover2(word[1:])
    if word[-1] == "'":
        return remover2(word[:-1])


words = [remover2(remover1(word)) for word in string.split()]

print(words)


# Введите строку => aqwe1!!1 2dd:;; :;; 123dsa,. w'a a' a'''' ''asd
# ['aqwe11', '2dd', '', '123dsa', "w'a", 'a', 'a', 'asd']
# Там не указано, какая именно строка. Я буду думать, что внутри слов только 1 ',
# чтобы не писать 3 функцию по поиску и удалениюэтого безобразия внутри слова
