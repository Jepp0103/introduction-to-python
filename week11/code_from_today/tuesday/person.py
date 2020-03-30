# person.py


class Person:
    
    def __init__(self, name):
        self.name = name


    @property           # getter
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        
        if name[0] in ['A', 'a']:
            self.__name = name
        else:
            print('You are not allowed here')
