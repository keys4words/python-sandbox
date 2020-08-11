import pickle
import reprlib

class Person:
    def __init__(self, name, age, siblings=None):
        self.name = name
        self.age = age
        self.siblings = siblings or []

    @reprlib.recursive_repr()
    def __repr__(self):
        return 'Person({name!r}, {age!r}, {siblings!r})'.format_map(self.__dict__)

    @staticmethod
    def make_siblings(first, second):
        first.siblings.append(second)
        second.siblings.append(first)


### cycling anchors
john = Person('John', 39)
melissa = Person('Melissa', 24)
Person.make_siblings(john, melissa)
# print(john, melissa)

### serialize with pickle
# with open('inout/data/persons.pkl', 'wb') as f:
#     pickle.dump((john, melissa), f)

with open('inout/data/persons.pkl', 'rb') as f:
    persons = pickle.load(f)

# print(persons)

### serialize to string with pickle
s = pickle.dumps({'first': True, 'second': None})
print(s)
u_s = pickle.loads(s)
print(u_s)
