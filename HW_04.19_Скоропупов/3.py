from random import randrange as rr


def remover(arr, n, *, new=True):
    if len(arr) < 4:
        raise Exception(f'len(arr) == {len(arr)} < 4')

    new_arr = arr[:] if new else arr

    for i in range(n):

        new_arr.remove(max(new_arr))
        new_arr.remove(min(new_arr))
    return new_arr



test_arr = [rr(1, 100) for _ in range(3)]

print(test_arr, remover(test_arr, 3, new=False))

# [95, 15, 60, 64, 62, 29, 58, 73, 39, 13] [60, 62, 58, 39]
# [52, 52, 21, 23] [52, 52, 21, 23]
# Traceback (most recent call last):
#   File "D:\Git\homework\HW_04.19_Скоропупов\3.py", line 16, in <module>
#     print(test_arr, remover(test_arr, 3, new=False))
#   File "D:\Git\homework\HW_04.19_Скоропупов\3.py", line 6, in remover
#     raise Exception('len(arr) < 4')
# Exception: len(arr) < 4


