# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def div(x, y):
#     return x / y

# def mul(x, y):
#     return x * y

operations = {
    # '+': add,
    # '-': sub,
    # '/': div,
    # '*': mul, 
    # '^': pow
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y, 
    '^': lambda x, y: x ^ y
}

try:
    first = float(input('Enter first number: '))
    operation = input('Input operation: ')
    second = float(input('Enter second number: '))
    result = operations[operation](first, second)
except ValueError:
    print('Incorrect input')
except KeyError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Result:', result)