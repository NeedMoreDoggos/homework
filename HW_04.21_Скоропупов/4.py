def hof(func, *args, pref_str=True):
    result = round(func(*args), 2)
    return str(result) if pref_str else float(result)


print(hof(lambda x, k, b: k*x + b, 5, 2, 10), type(hof(lambda x, k, b: k*x + b, 5, 2, 10)))

# (5, 2, 10)
# 20 <class 'str'>

print(hof(lambda x, a, b, c: a*x**2+b*x+c, 2, 3, 4, 5, pref_str=False), type(hof(lambda x, a, b, c: a*x**2+b*x+c, 2, 3, 4, 5, pref_str=False)))

# (2, 3, 4, 5)
# 20 <class 'str'>
# 25.0 <class 'float'>
