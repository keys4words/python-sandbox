class Base:
    def method(self):
        print('Base method', __class__.__name__)


class Child(Base):
    def child_method(self):
        print('Child method', __class__.__name__)

    def method(self):
        print('Method from child class', __class__.__name__)


# obj = Child()
# obj.method()
# obj.child_method()
# base = Base()
# base.method()


class Figure:
    def __init__(self, side=0.0):
        self.side = side


class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('* ' * self.side)

class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)


class Horse:
    def run(self):
        print('I am running')

class Bird:
    def fly(self):
        print('I am flying')

class Pegasus(Horse, Bird):
    pass


class A:
    def method(self):
        print("A method")


class B(A):
    pass


class C(A):
    def method(self):
        print("C method")


class D(B, C):
    pass


class MethodContainer:
    def __init__(self, data):
        self.data = data

    def method(self):
        print('method invoked')
        print('data = ', self.data)


def main():
    # square = Square(3)
    # triangle = Triangle(4)
    # square.draw()
    # print()
    # triangle.draw()

    # pegasus = Pegasus()
    # pegasus.run()
    # pegasus.fly()
    # print(Pegasus.__name__)
    # print(Pegasus.__bases__)

    # obj = D()
    # obj.method()
    # for cls in [A, B, C, D]:
    #     print(cls.__name__, cls.__mro__)

    instance = MethodContainer(8)
    print(type(MethodContainer.method))
    print(type(instance.method))
    MethodContainer.method(instance)

if __name__ == '__main__':
    main()