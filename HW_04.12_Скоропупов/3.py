from string import punctuation
from pprint import pprint


def punct_remover(string):
    for i in punctuation:
        string = string.replace(i, '')
    string = string.replace('»', '')
    string = string.replace('—', '')
    string = string.replace('«', '')
    string = string.replace('…', '')
    return string


def reader(file_name):
    with open(file_name, encoding='utf-8') as fin:
        strings = [punct_remover(string).strip().lower() for string in fin]
    return strings


def towords(strings):
    words = list()
    for string in strings:
        words += string.split()
    return set(words)


def len_dic(words):
    max_len = len(max(words, key=len))
    word_leng = {i: [word for word in words if len(word) == i] for i in range(1, max_len + 1)} # Интересный факт. Самое длинное слово 18 символов "сверхъестественная", слова длинной 17 символов нет
    return word_leng


def letters_by_length(dicti):
    len_letters = dict()
    for length, words in dicti.items():
        for word in words:
            for letter in word:
                len_letters[letter][length] = len_letters.setdefault(letter, dict()).setdefault(length, 0) + 1
    return len_letters



pprint(letters_by_length(len_dic((towords(reader('poem.txt'))))))


# Интересно, что в пунктуации не вся пунктуация. Нет дефиса и кавычек "ёлочек". + какой-то странный символ троеточия …
# dict_keys(['с', 'я', 'у', 'в', '—', 'к', 'б', 'о', 'и', 'а', 'ж', '»', 'е', 'д', 'ю', 'м', 'н', 'х', 'т', 'п', '«', 'ы', 'з', 'л', '
# й', 'э', 'ь', 'ё', 'ч', 'р', 'ш', '…', 'г', 'щ', 'ц', 'ф', 'ъ', 'p'])
# Часть ответа. Первая 'p' -- латинская. Как она там оказалась, я не знаю.
# {'p': {7: 1},
#  'а': {1: 1,
#        2: 6,
#        3: 38,
#        4: 142,
#        5: 294,
#        6: 451,
#        7: 532,
#        8: 423,
#        9: 279,
#        10: 177,
#        11: 93,
#        12: 34,
#        13: 17,
#        14: 15,
#        15: 3,
#        16: 1,
#        18: 1},
#  'б': {1: 1,
#        2: 2,
#        3: 12,
#        4: 43,
#        5: 89,
#        6: 125,
#        7: 119,
#        8: 79,
#        9: 64,
#        10: 53,
#        11: 38,
#        12: 10,
#        13: 4,
#        14: 4,
#        15: 1},
