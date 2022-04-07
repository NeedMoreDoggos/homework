def print_row(m:int, n:int):
    if m > n:
        print('m > n, а нужно m <= n')
        print_row(int(input()), int(input()))
        return
        
    for i in range(m, n + 1):
        print(i, end=' ')


print_row(int(input()), int(input()))
