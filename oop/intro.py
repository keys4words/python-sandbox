class Person:
    name = 'Ivan'

    def hello():
        print('hello')


p1 = Person()
print(id(p1))
p2 = Person()
print(id(p2))
print(p1.name == p2.name)
print(id(Person.name), id(p1.name))
print(p1.__dict__, p2.__dict__)
p1.name, p2.age = 'Maxim', 26
print(p1.__dict__, p2.__dict__)
print(Person.hello, p1.hello)
print(type(Person.hello), type(p1.hello))


# print(dir(Person))
# print('='*25)
# print(Person.__dict__)
# Person.age = 34534
# print('='*25)
# print(Person.__dict__)
# print(getattr(Person, 'name'))
# setattr(Person, 'dob', '1980-01-01')
# print('='*25)
# print(Person.__dict__)
# delattr(Person, 'dob')
