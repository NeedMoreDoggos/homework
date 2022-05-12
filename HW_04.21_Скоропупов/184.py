def flattening(arr):
    flattening_arr = list()
    if isinstance(arr, (int, float, bool)):
        flattening_arr.append(arr)
    else:
        for item in arr:
            if isinstance(arr, (int, float, bool)):
                flattening_arr.append(item)
            elif isinstance(arr, (tuple, list, range, set, frozenset)):
                flattening_arr += flattening(item)
            else:
                continue
    return flattening_arr


def flattening_2(data):
    if not data:
        return []
    if isinstance(data[0], list):
        return flattening_2(data[0]) + flattening_2(data[1:])
    return [data[0]] + flattening_2(data[1:])

print(flattening_2( [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
print(flattening( [1, [2, 3], [4, [5, [6, 7]]],{1, 2, 3, 4, (1, 2, 3, range(1, 10))},'dad11', [[[8], 9], [10]]]))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 10]
