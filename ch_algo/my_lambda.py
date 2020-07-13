from random import randint

def my_math_func(x, f):
    return f(x)

def x_cube(x):
    return x**3

res = lambda x: x**3
# print(my_math_func(5, x_cube))
print(res(5))

letters = ['a', 'b', 'c', 'd', 'e']
print(list(map(lambda x: x+x.capitalize(), letters)))

my_ints = [randint(1, 1000) for num in range(100)]
print(my_ints)
print(list(map(lambda x: x**3, my_ints)))