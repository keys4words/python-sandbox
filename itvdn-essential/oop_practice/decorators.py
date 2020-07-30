def outer_func(func):
    print('This is outer func')
    func()
    print('This is outer func')


def outer_func2(func):
    def wrapper():
        print('This is outer func')
        func()
        print('This is outer func')
    return wrapper

def inside_func():
    print("This is inside func")

print('func in func')
outer_func(inside_func)

@outer_func2
def inside_func2():
    print("This is inside func")


print('decorator')
inside_func2()


