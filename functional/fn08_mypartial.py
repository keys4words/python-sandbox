from functools import partial
# partial
def add(x, y):
    return x + y

add_to_five = partial(add, 5)
# print(add_to_five(4))
# print(add_to_five(9))

print_with_comma = partial(print, sep=', ')
print_with_comma(43,5,7)