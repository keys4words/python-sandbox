class MyObject:
    def __init__(self):
        self.password = None
    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == 'pass':
            return 'secret value'
        else:
            return object.__getattribute__(self, item)


obj = MyObject()
print(obj.password)
# print(obj.secret_field)
obj.password = 'pass'
print(obj.secret_field)