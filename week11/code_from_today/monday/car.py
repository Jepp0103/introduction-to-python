# car.py

class Car:

    def __init__(self, *args):
        self.__make = []        
        self.mph = args[0]


    @property
    def make(self):
        return self.__make



    @make.setter
    def make(self, make):
        self.__make.append(make)

        """
        if isinstance(make, list):
            self.__make = make
        else:
            raise Exception('Make is not a list')
        """


    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, x):
        if type(x) == int:
            self.__mph = x
        else:
            #print('It have to be an int')
            raise TypeError('Has to be an int')
