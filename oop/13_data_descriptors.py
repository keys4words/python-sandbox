from time import time

class Epoch:
    def __get__(self, instance, owner_class):
        # print(f"Self: {self}")
        # print(f"Instance: {instance}")
        # print(f"Owner: {owner_class}")
        print(f'id of self: {id(self)}')
        if instance is None:
            return self
        return int(time())

    def __set__(self, instance, value):
        pass


class MyTime:
    epoch = Epoch()


m = MyTime()
print(m.epoch)
m1 = MyTime()
print(m1.epoch)
# print('*'*25)
# MyTime.epoch


class Person:
    _name = 'Maxim'
    @property
    def name(self):
        return self._name

# print(Person.name)
# print(Person().name)
