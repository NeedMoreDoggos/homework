letters_sps = 'bcdfghjklmnpqrstvwxyz aeiouBCDFGHJKLMNPQRSTVWXYZAEIOU1234567890'


def pigs(word):
    cons = 'bcdfghjklmnpqrstvwxyz'
    vocals = 'aeiou'
    word = word.lower()
    if word[0] in cons:
        for i in range(len(word)):
            if word[i] in vocals:
                return f'{word[i:]}{word[:i]}ay'
    elif word.isdigit():
        return f'{word}'
    else:
        return f'{word}way'


def edit_string(string):
    # string = string.lower()
    if not string:
        return string
    if not string[0] in letters_sps:
        return f' {string[0]}{edit_string(string[1:])}'
    return f'{string[0]}{edit_string(string[1:])}'


def pig_string(string):
    new_string = ''
    where_cap = list()
    words = edit_string(string).split()
    where_cap = [word[0].isupper() for word in words]
    print(where_cap)
    # words = edit_string(string).split()
    for i in range(len(words)):
        if words[i][0] in letters_sps:
            words[i] = pigs(words[i])
    print(words)
    for i in range(len(words)):
        if where_cap[i]:
            words[i] = words[i].capitalize()
    for word in words:
        if word.isalnum():
            new_string += ' '
            new_string += word
        else:
            new_string += word
    print(new_string)
    return new_string.strip()


print(pig_string(input()))


# Это ужастно, но оно работает. По тому, как отлаживал удалять небуду. Если пойму, что где-то есть проблема тяжело будет находить снова
# How? Are, you! Intel 1234
# [True, False, True, False, False, False, True, False]
# ['owhay', '?', 'areway', ',', 'ouyay', '!', 'intelway', '1234']
#  Owhay? Areway, ouyay! Intelway 1234
# Owhay? Areway, ouyay! Intelway 1234
