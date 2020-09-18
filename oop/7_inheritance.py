class Person:
    age = 0
    def hello(self):
        print('Hello')


class Student(Person):
    def hello(self):
        print('I am student')


s = Student()
# print(dir(s))
s.hello()
# print(s.__dict__)
# print(Student.__dict__)
# print(Person.__dict__)


class IntelCpu:
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass

class I5(IntelCpu):
    pass


# i5 = I5()
# i7 = I7()

# print(isinstance(i5, IntelCpu))
# print(type(i5))

class One:
    pass

class Two(One):
    pass

class Three(Two):
    pass


# one = One()
# newOne = One()
# two = Two()
# three = Three()
# print(issubclass(type(three), type(one)))
# print(isinstance(one, type(newOne)))