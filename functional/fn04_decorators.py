def decorator(fn):
    def decorated_fn(*args, **kwargs):
        print('Start of decorated function')
        fn(*args, **kwargs)
        print('End of decorated function')
    return decorated_fn

@decorator
def print_hello():
    print('Hello')


# print_hello()
# print('*'*20)
# print_hello = decorator(print_hello)
# print_hello()


# decorator with params
def make_decorator(string):
    def decorator(fn):
        def decorated_fn(*args, **kwargs):
            print(string)
            fn(*args, **kwargs)
        return decorated_fn
    return decorator


@make_decorator('Before invokation')
@make_decorator('Before invokation second!!!')
def print_hello2():
    print('Hello')


print_hello2()