def where_punct(string):
    string = string.strip()
    punct = ' .?!'
    punct_in = [symbol in punct for symbol in string]
    return punct_in


def new_sen(string):
    capitals = list()
    punct = where_punct(string)
    for i in range(len(punct)-1):
        if punct[i]:
            for j in range(i+1, len(string)):
                if string[j] != ' ':
                    capitals += [True]
                    break
        capitals += [False]
    return capitals


def capital_i(string):
    # Я буду думать, что строка всегда завершается символом пунктуации и нет случаев, где i будет последним символом
    punct = ' .?!'
    string = string.lower().strip()
    upper_i = list()
    for i in range(1, len(string)):
        if i == 'i':
            if string[i-1] == ' ' or string[i+1] in punct:
                upper_i += [True]
        upper_i += [False]
    return upper_i


def format_str(string):
    string = string.strip()
    capitals = [i or j for i, j in zip(capital_i(string), new_sen(string))]
    print(capitals)
    string = list(string)
    capitals[0] = True
    for i in range(len(string)):
        if capitals[i]:
            string[i] = string[i].upper()
    return ''.join(string)


print(format_str('can. can'))
