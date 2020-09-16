class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f"{self._name} {self._surname}"
        return self._full_name



p = Person('Ivan', 'Ivanov')
print(p.__dict__)
# p.name = 'John'
print(p.full_name)
print(p.__dict__)
p.surname = 'Petrov'
print(p.__dict__)
print(p.full_name)
print(p.__dict__)
