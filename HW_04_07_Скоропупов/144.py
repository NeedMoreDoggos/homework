def symbols(string):
    letters = dict()
    string = string.lower()
    zzz = 'qazwsxedcrfvtgbyhnujmikolp'
    for letter in string:
        if letter in zzz:
            letters.setdefault(letter, 0)
            letters[letter] += 1
    return letters


def anagram(str1, str2):
    return symbols(str1) == symbols(str2)


print(anagram('«William Shakespeare»', '«I am a weakish speller»'))

# True
