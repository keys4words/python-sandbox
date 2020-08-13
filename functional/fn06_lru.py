import random, time

from functools import lru_cache


def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@lru_cache(maxsize=None)
def fib2(n):
    if n==1 or n==2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

def analyze_algo(func1, func2, arr=random.randint(35, 40)):
    start1 = time.time()
    res1 = func1(arr)
    end1 = time.time()
    print(f'{func1.__name__}({arr})\t->{res1}\t->{end1-start1:.5f}')
    start2 = time.time()
    res2 = func2(arr)
    end2 = time.time()
    print(f'{func2.__name__}({arr})\t->{res2}\t->{end2-start2:.5f}')

analyze_algo(fib, fib2)