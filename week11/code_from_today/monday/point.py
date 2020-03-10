# point.py



class Point:
    def __init__(self, *args): # args -> (1, 3)
        self.x = args[0]
        self.y = args[1]

    @property # getter
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 10:
            self.__x = 10
        else:
            self.__x = x



"""

    def get_x(self):
        return self.__x

"""

"""
x = Point(1, 2)
x2 = Point(2, 3 )
x3 = Point(3, 4)

x3.set_x(x.get_x() + x2.get_x()) 
x3.x = x.x + x2.x

"""


