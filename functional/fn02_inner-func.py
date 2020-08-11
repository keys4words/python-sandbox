def add(x):
    def do_add(y):
        return x + y
    return do_add

add_to_five = add(5)
# print(add_to_five(7))
# print(add(5)(3))

def Person(name, age):
    def print_hello():
        print('Hello! My name is {}'.format(name))
    
    def get_age():
        return age

    return {'print_hello': print_hello, 'get_age': get_age}


john = Person('John', 32)
john['print_hello']()
print(john['get_age']())