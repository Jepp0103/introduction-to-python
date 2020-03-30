# point.py


class Point:
    def __init__(self, *args): # args -> tuple (1, 2, 3, 'hello')
        self.__x = args[0]
        self.__y = args[1]

    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
    

