string = input()

if string.find('.') == -1 or string.find('@') == -1:
    print('Нет')
elif string.find('@') > string.find('.'):
    print('Нет')
else:
    print('Да')
