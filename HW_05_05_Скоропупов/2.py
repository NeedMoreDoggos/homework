def gen_perm(n, m=-1, prefix=None):
    m = len(n) if m == -1 else m
    prefix = prefix or []

    if m == 0:
        yield prefix

    for element in n:
        if element in prefix:
            continue
        prefix.append(element)
        yield from gen_perm(n, m - 1, prefix)
        prefix.pop()


for i in gen_perm({'cat', 'dog', 'fox', 'racoon'}):
    print(i)

# ['cat', 'racoon', 'fox', 'dog']
# ['cat', 'racoon', 'dog', 'fox']
# ['cat', 'fox', 'racoon', 'dog']
# ['cat', 'fox', 'dog', 'racoon']
# ['cat', 'dog', 'racoon', 'fox']
# ['cat', 'dog', 'fox', 'racoon']
# ['racoon', 'cat', 'fox', 'dog']
# ['racoon', 'cat', 'dog', 'fox']
# ['racoon', 'fox', 'cat', 'dog']
# ['racoon', 'fox', 'dog', 'cat']
# ['racoon', 'dog', 'cat', 'fox']
# ['racoon', 'dog', 'fox', 'cat']
# ['fox', 'cat', 'racoon', 'dog']
# ['fox', 'cat', 'dog', 'racoon']
# ['fox', 'racoon', 'cat', 'dog']
# ['fox', 'racoon', 'dog', 'cat']
# ['fox', 'dog', 'cat', 'racoon']
# ['fox', 'dog', 'racoon', 'cat']
# ['dog', 'cat', 'racoon', 'fox']
# ['dog', 'cat', 'fox', 'racoon']
# ['dog', 'racoon', 'cat', 'fox']
# ['dog', 'racoon', 'fox', 'cat']
# ['dog', 'fox', 'cat', 'racoon']
# ['dog', 'fox', 'racoon', 'cat']
