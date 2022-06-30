from pathlib import Path


def return_file():
    path = input('Введите путь к файлу_> ')

    with open(path, 'r') as fin:
        with open(str(Path.cwd()) + '\\second.py', 'w') as fon:
            fon.write(fin.read())
