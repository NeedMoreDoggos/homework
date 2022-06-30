import time

N = 10 ** 8


def bench(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Время работы {func.__name__} _> {end - start}')
        return res

    return wrapper


@bench
def append_use():
    global N
    arr = list()

    for i in range(N):
        arr.append(i)

    return arr


@bench
def concat_use():
    global N
    arr = list()

    for i in range(N):
        arr += [i]

    return arr

@bench
def lc_use():
    global N
    return [i for i in range(N)]

a = append_use()
b = concat_use()
c = lc_use()
# N = 10 ** 8
# Время работы append_use _> 9.440819501876831
# Время работы concat_use _> 8.270529508590698
# Время работы lc_use _> 4.550224781036377
# N = 10 ** 6
# Время работы append_use _> 0.11800026893615723
# Время работы concat_use _> 0.10402679443359375
# Время работы lc_use _> 0.07202029228210449
# N = 10 ** 8
# После подключения к электро сети
# Время работы append_use _> 4.369599342346191
# Время работы concat_use _> 5.6571125984191895
# Время работы lc_use _> 3.210222005844116