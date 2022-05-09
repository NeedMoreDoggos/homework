def isbinary(string):
    binary_set = {'0', '1', 'b'}
    symbols = set(string)
    print(symbols, binary_set, symbols - binary_set)
    if not symbols - binary_set:
        if not 'b' in symbols:
            return True
        if string.count('b') > 1:
            return False
        if 'b' == string[0]:
            return True
        if '0b' == string[:2]:
            return True
        return False
    return False




print(isbinary('101011012010'))

# PS D:\Git\homework\HW_04.12_Скоропупов> py 2.py
# {'b', '0', '1'} {'b', '0', '1'} set()
# True
# PS D:\Git\homework\HW_04.12_Скоропупов> py 2.py
# {'0', '1'} {'0', '1', 'b'} set()
# True
# PS D:\Git\homework\HW_04.12_Скоропупов> py 2.py
# {'2', '0', '1'} {'b', '0', '1'} {'2'}
# False
