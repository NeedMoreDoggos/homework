def punct_remover(string):
    punct = '?.,;:"@*&!'
    for i in punct:
        string = string.replace(i, '')
    return string


def string_to_words(string):
    count = dict()
    string = string.lower()
    string = punct_remover(string)
    words = string.split()
    for word in words:
        count.setdefault(word, 0)
        count[word] += 1
    return [(i, j) for i, j in count.items()]


def need_word(string):
    words = string_to_words(string)
    return min(words, key=lambda x: x[::-1])


print(need_word('Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра '))

# ('без', 1)
