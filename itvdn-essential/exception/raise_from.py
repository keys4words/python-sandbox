a = 6
b = 0
try:
    res = a/b
except ZeroDivisionError as e:
    raise ValueError('second number is null') from e