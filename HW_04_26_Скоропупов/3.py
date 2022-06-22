from pathlib import Path
import os
import datetime


def add_file(name):
    with open('x_files.txt', 'a', encoding='utf-8') as fin:
        fin.write(str(name) + '\n')

    return


def x_files(path, *, old=7):
    start_dir = Path(path)
    print(start_dir)
    if not start_dir.is_dir():
        print('Неверно указан путь')
        return
    content = os.listdir(start_dir)
    print(content)

    for i in range(len(content)):
        if Path(str(start_dir) + '\\' + content[i]).is_dir():
            print('Ето папощка', Path(str(start_dir) + '\\' + content[i]))
            x_files(Path(str(start_dir) + '\\' + content[i]), old=old)
        else:
            if datetime.timedelta(seconds=os.stat(Path(str(start_dir) + '\\' + content[i])).st_mtime).days > old:
                print('Ето файлик', Path(str(start_dir) + '\\' + content[i]))
                add_file(str(Path(str(start_dir) + '\\' + content[i])))

    return


x_files(input('Введите путь'), old=1)
