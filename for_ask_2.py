# Создаем класс
class Number:    
    def __init__(self, digit):
        self.__digit = digit
    
    def get_dig(self):
        return self.__digit
    
    def set_dig(self, digit):
        self.__digit = digit
    
    # Создаем объект класса property
    digit = property(get_dig, set_dig)
    digit2 = 100
    

# Создаем объект класса Number
num = Number(12345)
# Затеняю атрибут класса digit, digit2
num.__dict__['digit'] = 'This is digit'
num.__dict__['digit2'] = 'This is digit'
# Парам пам пам
num.digit = 5
num.digit2 = 1
# digit в экземпляре проигнорировался и выполнился сеттер. Это видно потому, что находится в __dict__. В то же время digit2 затенился и изменился в экземпляре класса, а не в объекте класса
# Почему именно это я вижу? Почему не затенился локальным атрибутом атрибут класса?
print(num.digit, num.digit2, num.__dict__, Number.__dict__, sep='\n\n')
 