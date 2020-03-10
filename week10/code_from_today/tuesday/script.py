# script.py



class A:

    # attributes / variables for data

    gender = 'Male'

    # Methods
    def __init__(self, *args): # age = 33 # default values
        
        if len(args) == 1:
            self.name = args[0]  # instance variable (starts with 'self')
        if len(args)  == 2:
            self.age = args[1]
            self.name = args[0]  # instance variable (starts with 'self')

    def __repr__(self):
        return str(self.__dict__)  # {key : value}

    def __str__(self):
        return self.name


c = A('Claus', 66, 33, 44,  666)
a = A('Anna')








