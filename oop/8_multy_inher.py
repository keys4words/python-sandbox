class FoodMixin:
    food = None
    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set!')
        print(f"I like {self.food}")



class Person:
    def hello(self):
        print('I am Person')


class Student(Person, FoodMixin):
    food= 'Pizza'
    def hello(self):
        print('I am Student')


class Professor(Person):
    def hello(self):
        print('I am Professor')


class Someone(Student, Professor):
    pass


s = Someone()
s.hello()
print(s.__class__.__mro__)
s.get_food()