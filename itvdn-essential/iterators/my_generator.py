def generator():
    yield 'one'
    yield 'two'

g = generator()
print(g)
print(dir(g))
print(next(g))
print(next(g))
# print(next(g))

print('='*10)

def fib(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second

# count = int(input('How many Fibonacci number to show? - '))
# for el in fib(count):
#     print(el)


print('='*10)
def generator_func():
    for x in range(5):
        for y in range(3):
            if x == y:
                yield x * y

g = generator_func()
g1 = (x * y for x in range(5) for y in range(3) if x == y)
# for value in g:
#     print(value)
# print('-'*10)
# for value in g1:
#     print(value)

print(sum(x**2 for x in range(10)))

def subgen():
    yield '"subgen #1"'
    yield '"subgen #2"'
    yield '"subgen #3"'
    yield '"subgen #4"'

def gen_with_subgen():
    yield from (x*2 for x in range(10))
    yield from subgen()
    yield 'end'

for value in gen_with_subgen():
    print(value, end=' ')