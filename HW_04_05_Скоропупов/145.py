def points(word):
    word = word.upper()
    sum = 0
    dicti = {
        1: "AEILNORSTU",
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ',
    }
    for letter in word:
        for i, j in dicti.items():
            if letter in j:
                sum += i
                break
    return sum


print(points('Points'))

# 141 нее сделаю. Мой уровень англицкова не такой хороший, чтобы искать закономерности в языке
# 8
