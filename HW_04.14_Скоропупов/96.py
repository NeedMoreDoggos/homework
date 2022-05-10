def new_strip(string):
    start = 0
    end = len(string) - 1
    for i in range(len(string)):
        if ord(string[i]) != 32:
            start = i
            break
    for i in range(len(string)-1, -1, -1):
        if ord(string[i]) != 32:
            end = i
            break
    return string[start: end+1]


def is_didgit(symbol):
    code = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    if ord(symbol) not in code:
            return False
    return True


def is_number(string):
    string = new_strip(string)
    if len(string) < 1:
        return False
    if not is_didgit(string[0]) and not ord(string[0]) in [43, 45]:
        return False
    for symbol in string[1:]:
        if not is_didgit(symbol):
            return False
    return True


print(is_number('     +212332312321  '))
# True
