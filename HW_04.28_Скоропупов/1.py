def csv_reader(file, separator=','):
    seps = ',;\\t'
    if separator not in seps:
        raise ValueError(f'Разделитель должен быть в {seps}')

    try:
        with open(file, 'r', encoding='utf-8') as fin:
            # Насколько правильно делать это так? Просто если файл освобождать быстрее, то нужно вынести переменные и
            # закрыть менеджер контекста. Иначе файл будет открыт, пока не сделаем все операции?
            name = fin.readline().strip().split(separator)
            val = [string.split(separator) for string in fin.read().strip().split()]
            return {name[i]: [int(val[j][i]) for j in range(len(val))] for i in range(len(name))}
    except FileExistsError:
        return


print(csv_reader('test.csv'))
print(csv_reader('test.csv', 's'))
# {'col1': ['1', '2', '3'], 'col2': ['10', '20', '30'], 'col3': ['100', '200', '300']}
# Traceback (most recent call last):
#   File "E:\git\homework\HW_04.28_Скоропупов\1.py", line 17, in <module>
#     print(csv_reader('test.csv', 's'))
#   File "E:\git\homework\HW_04.28_Скоропупов\1.py", line 4, in csv_reader
#     raise ValueError(f'Разделитель должен быть в {seps}')
# ValueError: Разделитель должен быть в ,;\t
