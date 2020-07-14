l1 = [num for num in range(1, 11)]
cubes = map(lambda x: x**3, l1)

# print(list(cubes))

def mash_map(f, some_iterable):
    for item in some_iterable:
        yield f(item)

def mash_map2(f, some_iterable):
    return (f(item) for item in some_iterable)

print(l1)
cubed_ints = mash_map2(lambda x: x**3, l1)
print(cubed_ints)
print(next(cubed_ints))
print(next(cubed_ints))
print(next(cubed_ints))
print(list(cubed_ints))