# property_example.py

class A:
    def __init__(self):
        self.__name = 'Claus'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        #if name in [str]:
        self.__name = name

