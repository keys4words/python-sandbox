class Point:
    WIDTH = 5

    # list of available slots for variables in Class
    __slots__ = ['__x', '__y']

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if (isinstance(x, int) or isinstance(x, float)):
            return True
        return False

    def setCoords(self, x, y):
        # if (isinstance(x, int) or isinstance(x, float)) and \
        #     (isinstance(y, int) or isinstance(y, float)):
        #     self.__x = x
        #     self.__y = y
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Coordinates must be numbers')

    def getCoords(self):
        return self.__x, self.__y


    # def __getattribute__(self, item):
    #     if item == '_Point__x':
    #         return 'Overloading variable x'
    #     else:
    #         return object.__getattribute__(self, item)

    # def __setattr__(self, key, value):
    #     if key == 'WIDTH':
    #         raise AttributeError
    #     else:
    #         self.__dict__[key] = value


    # def __getattr__(self, item):
    #     print('__getattr__:'+item)

    # def __delattr__(self, item):
    #     print('__delattr__:'+item)


p = Point(1, 2)
# print(p.__x)
p.setCoords(10,10)
p.setCoords('a20',20)
print(p.getCoords())
print('get private attribute with name mangling ->', p._Point__x)
print('get private method with name mangling ->', Point._Point__checkValue(4))
# p.WIDTH = 10
p.zz
p.zz=1
del p.zz
