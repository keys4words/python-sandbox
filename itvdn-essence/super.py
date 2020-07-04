class Base:
    def method(self):
        print('Base method invoked on', type(self).__name__, 'instance')

class Child(Base):
    def method(self):
        super().method()
        print('Child method invoked on', type(self).__name__, 'instance')


base = Base()
base.method()

child = Child()
child.method()