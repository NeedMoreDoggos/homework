from msg import *

COMMANDS = ('quit', 'msg')

while True:
    command, *string = input('Введите команду _> ').split()
    
    if command not in COMMANDS:
        print('Неизвестная команда')
        continue    
    elif command == COMMANDS[0]:
        print('Пока')
        break   
    elif command == COMMANDS[1]:
        important_message(' '.join(string))
    else:
        raise Exception('Невероятное событие с нами(есть какая-то необработанная команда)')

    

# Импортировать имя модуля с первой цифирей мне не удалось