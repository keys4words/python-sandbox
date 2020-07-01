class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, 'is', self.age)

john = Person('John', 22)

lucy = Person('Lucy', 34)

# Person.print_info(john)
# lucy.print_info()

class MyObject:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 43
        self.__private_attr = 876

    @property
    def private_attr(self):
        return self.__private_attr

    @private_attr.setter
    def private_attr(self, attr):
        if attr < 100:
            self.__private_attr = attr

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def __repr__(self):
        return '<Rectangle {} {}>'.format(self.side_a, self.side_b)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return '<Circle (%.1f)>' % self.radius

    @classmethod
    def from_rectangle(cls, rectange):
        radius = (rectange.side_a**2 + rectange.side_b**2)**0.5/2
        return cls(radius)

def main():
    # rectangle = Rectangle(3, 4)
    # print(rectangle)

    # first_circle = Circle(1)
    # print(first_circle)

    # second_circle = Circle.from_rectangle(rectangle)
    # print(second_circle)
    obj = MyObject()
    print(obj.private_attr)
    obj.private_attr = 90
    print(obj.private_attr)



if __name__ == '__main__':
    # MyObject.static_method()
    # obj = MyObject()
    # obj.instance_method()
    # obj.static_method()
    
    main()