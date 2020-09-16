class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, new_name):
        print('From set_name()')
        self._name = new_name

    
    name = property(fget=get_name, fset=set_name)


# p = Person('James')
# p.name = 'Keanu'
# print(p.__dict__)
# print(p.name)

class Person2:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, new_name):
        print('From set_name()')
        self._name = new_name

    
    name = property(get_name)
    name = name.setter(set_name)


# p = Person2('James')
# p.name = 'Keanu'
# print(p.__dict__)
# print(p.name)


class Person3:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        print('From get_name()')
        return self._name
    
    @name.setter
    def name(self, new_name):
        print('From set_name()')
        self._name = new_name


p = Person3('James')
p.name = 'Keanu'
print(p.__dict__)
print(p.name)