def where_end(string):
    """
    Находит места, где завершается предложение по знакам препинания, исключая последний
    :param string: Предварительно обработанная строка
    :return: Список мест в бул. виде, где есть знаки препинания, исключая последний
    """
    punct = [False] * len(string)

    for i in range(len(string)-1):
        if string[i] in '.?!':
            punct[i] = True

    return punct


def upper_sen(string):
    """
    Считается, что пробелы расставлены правильно и в предложении нет троеточия
    :param string: Предварительно обработанная строка
    :return: Список заглавных букв в начале предложения не считая первого
    """
    end_sen = where_end(string)
    upper = [False] * len(string)

    for i in range(len(string)):
        if end_sen[i]:
            upper[i+2] = True

    return upper


def upper_i(string):
    '''
    Пробегает по строке создавая список буллеевых значений, где i должна быть заглавной
    :param string: предварительно обработанная строка
    :return: Список бул. значений, где i заглавная
    '''
    # Без комментария никто не поймет, что это первая заглавная буква
    upper = [True]

    for i in range(1, len(string) - 1):
        if string[i] == 'i':
            if string[i-1] == ' ' or string[i+1] in "' .?1":
                upper += [True]
            else:
                upper += [False]
        else:
            upper += [False]

    return upper + [False]


def is_upper(string):
    '''
    Создает список булеевых значений, где буква должна быть заглавная
    :param string: предварительно обработанная строка
    :return: Список бул. значений, где должна быть заглавная буква
    '''
    test = [i or j for i, j in zip(upper_i(string), upper_sen(string))]
    return test


def string_changer(string):
    '''
    Расставляет "правильно" загавные буквы
    :param string: Любая строка
    :return: Строка с "правильно" расставлеными заглавными буквами
    '''
    string = string.strip().lower()
    upper = is_upper(string)
    string = list(string)

    for i in range(len(string)):
        if upper[i]:
            string[i] = string[i].upper()

    return ''.join(string)


print(string_changer('what time do i have to be there? what’s the address? this time i’ll try to be on time!'))

# PS D:\Git\homework\HW_04.14_Скоропупов> py 95.py
# What time do I have to be there? What’s the address? This time I’ll try to be on time!
