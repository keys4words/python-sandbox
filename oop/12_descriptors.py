class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname



class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)
    
    def set(self, value):
        self._value = value

    
    def get(self):
        return self._value


class Person2:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)