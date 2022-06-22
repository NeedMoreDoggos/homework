def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)
    
    return inner
    

@counter
def test():
    pass