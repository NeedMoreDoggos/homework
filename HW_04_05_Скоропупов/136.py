def reverse_lookup(dic, item):
    keys = list()
    for i, j in dic.items():
        if item in [j]:
            keys.append(i)
    return keys


dicti1 = {
    1: 1,
    2: 2,
    3: 1,
    4: 2,
    5: 1,
}
dicti2 = {
    1: '111',
    2: '123',
    3: '11',
    4: '321',
    5: '111',
}
print(reverse_lookup(dicti2, '111'))

# [1, 3, 5]
# [1, 5]
