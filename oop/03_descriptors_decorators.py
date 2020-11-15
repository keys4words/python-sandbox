class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):
        # print('__getCoordX')
        return self.__x

    @coordX.setter
    def coordX(self, x):
        # print('__setCoordX', x)
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError('Wrong format')

    @coordX.deleter
    def coordX(self):
        print('Delete X property')
        del self.__x

    # coordX = property(__getCoordX, __setCoordX, __delCoordX)


pt = Point(2, 3)
pt.coordX = 100
x = pt.coordX
print(x)
del pt.coordX
