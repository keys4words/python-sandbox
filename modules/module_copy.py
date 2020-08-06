import copy

class Container:
    def __init__(self):
        self.list = [1, 2, 3]
        self.number = 8


obj = Container()
print(obj.list, ' - ', obj.number)
shallow_copy = copy.copy(obj)
shallow_copy.list.append(4)
print(obj.list)

deep_copy = copy.deepcopy(obj)
deep_copy.list.append(5)
print(obj.list)