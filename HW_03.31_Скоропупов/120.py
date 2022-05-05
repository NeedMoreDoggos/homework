words = list()

while ele:=input():
    words.append(ele)


def pstring(arr):
    string = ', '.join(arr[:-1])
    string += f' и {arr[-1]}'
    return string


print(pstring(words))

# Cat
# dog
# Cat
#
# Cat, dog и Cat
