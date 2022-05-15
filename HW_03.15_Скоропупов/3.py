def converter(m):
    return m * 100, m * 10, m * 1000, m / 1609.34


print(converter(int(input())))
