arr = list(range(8))

def func(x):
    return x*2


print(list(map(func, arr)))
print(list(map(lambda x: x**3, arr)))