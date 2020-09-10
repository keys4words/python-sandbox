class Person:
    def hello(self):
        print('Hello')

    @staticmethod
    def goodbye():
        print('Goodbye')


p = Person()
# p.hello()
p.goodbye()
p2 = Person()
print(id(p.goodbye), id(p2.goodbye))
