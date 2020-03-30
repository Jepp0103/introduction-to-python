# car.py


class Car:
    def __init__(self, *args):
        self.__make = [] 

    @property 
    def make(self):
        print('In my getter')
        return self.__make
    
    @make.setter
    def make(self, make):
        print('In my setter')
        self.__make.append(make)


