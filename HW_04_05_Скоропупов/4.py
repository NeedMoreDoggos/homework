def name_chenger(word, digit):
    index = word.rfind('.')
    return f'{word[:index]}_{digit}{word[index:]}'


def no_dupl(string):
    dicti = dict()
    names = string.split()
    for i in range(len(names)):
        word = names[i]
        dicti.setdefault(word, 0)
        dicti[word] += 1
        if dicti[word] > 1:
            names[i] = name_chenger(word, dicti[word])
    return ' '.join(names)


print(no_dupl('1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp'))

# ['1.py', '1.py', 'aux.h', 'main.cpp', 'functions.h', 'main.cpp', '2.py', 'main.cpp']
# 1.py 1_2.py aux.h main.cpp functions.h main_2.cpp 2.py main_3.cpp
