class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls


class Config:
    name = 'John Dow'


p = Person('Peter')
print(p.__dict__)
p2 = Person.from_file('names.txt')
print(p2.__dict__)
p3 = Person.from_obj(Config)
print(p3.__dict__)

