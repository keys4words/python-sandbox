class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getCoordX(self):
        print('__getCoordX')
        return self.__x

    def setCoordX(self, x):
        print('__setCoordX')
        self.__x = x

pt = Point(1, 2)
pt.coordX = 100

