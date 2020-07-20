import time

def recur_countdown_timer(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recur_countdown_timer(n-1)

def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print(n)

z = 5
# print(f"Counting down from {z}:")
# iter_countdown_timer(z)
# print(recur_countdown_timer(z))

def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n - 1)

# print(factorial_recur(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))