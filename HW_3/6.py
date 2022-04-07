def fibo_cycle(n:int):
    if n <= 0:
        return

    sum1 = 0
    sum2 = 1

    for i in range(n):
        if i%2 != 0:
            sum1 = sum1 + sum2
        else:
            sum2 = sum1 + sum2

    if sum1 > sum2:
        return(sum1)
    else:
        return(sum2)


for i in range(1, 20):
    print(fibo_cycle(i), end=' ')
