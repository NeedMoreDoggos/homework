def counter(func):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)
    
    return wrapper

@counter
def test_1():
    return 1 

class Counter:
    all_count = dict()
    
    def __init__(self, func):
        self.func = func
        self.count = 0
  
    def __call__(self, *args, **kwargs):
        self.count += 1
        self.all_count[self.func.__name__] = self.count
        return self.func(*args, **kwargs)


@Counter
def test_2():
    return 2


@Counter
def test_3():
    return 3
    

for _ in range(10):
    test_2()
for _ in range(20):
    test_3()


print(test_2.count, test_3.count, Counter.all_count)