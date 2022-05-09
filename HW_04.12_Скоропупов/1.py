from random import randrange as rr


def union(arr1, arr2):
    return set(arr1+arr2) # ну или set(arr1) | set(arr2)


list1 = [rr(1, 10) for _ in range(100)]
list2 = [rr(1, 10) for _ in range(100)]
print(union(list1, list2))


# {1, 2, 3, 4, 5, 6, 7, 8, 9}
