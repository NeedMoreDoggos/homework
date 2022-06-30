from pathlib import Path


def x_files(dir_name):
    path = Path(dir_name)
    if not path.is_dir():
        raise ValueError('Ссылка не на папощку')
    # return (tuple(path.glob('**/*.*'))) но это не канает для линя. Ну и полные пути к файлам
    return tuple([file.name for file in path.glob('**/*') if file.is_file()])


print(x_files('E:\Python курс\Python\homework\HW_04.28\TestFolder'), sep='\n')
# ('7MD9i.chm', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'r62Bf.txt', 'xcD1a.zip')
