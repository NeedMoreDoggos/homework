def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)


print(gcd(1720, 680))
# 40 
