from shutil import get_terminal_size as gts


def split_line(text):
    long = gts()[0] - 5
    strings = list()
    n = 0
    
    while len(text) >= long * n:
        strings.append(text[n * (long): (n + 1) * (long)])
        n += 1

    return strings


def important_message(text):
    long = gts()[0] - 1
    strings = split_line(text)
    
    print('#', '=' * (long - 2), '#', sep='')
    print('#', ' ' * (long - 2), '#', sep='')
    for i in range(len(strings)):
        print('#', strings[i].ljust(long - 4, ' '), '#')
    print('#', ' ' * (long - 2), '#', sep='')
    print('#', '=' * (long - 2), '#', sep='')
    
    return
