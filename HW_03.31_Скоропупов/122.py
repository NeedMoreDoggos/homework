def pigs(word):
    cons = 'bcdfghjklmnpqrstvwxyz'
    vocals = 'aeiou'
    if word[0] in cons:
        for i in range(len(word)):
            if word[i] in vocals:
                return f'{word[i:]}{word[:i]}ay'
    return f'{word}way'


def pig_string(string):
    words = string.split()
    for i in range(len(words)):
        words[i] = pigs(words[i])
    return ' '.join(words)


print(pig_string(input()))

print('bcdfghjklmnpqrstvwxyzaeiou'.upper())

# cow milc apple sexy owls years sleep intel
# owcay ilcmay appleway exysay owlsway earsyay eepslay intelway
