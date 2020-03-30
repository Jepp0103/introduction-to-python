"""
Encaptiolation &  Propeties exercises
All following exercises should be done by using Properties when needed. The focus should be on encapsulation. 

1. Car object
Create a Car class. 
When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph).
They all 4 should be properties.

"""
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

"""
2. Bank 
In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.  
The bank class should futher be change into not taking any accounts as parameters at initialization. The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).      
Somewhere you should change the code so that a customer only can create one account.     
The Customer class should make sure that the customer is over 18 year of age.

"""

class Bank:    
    def __init__(self):
        self.__accounts = []  # When bank is initialized it has  the abillity to hold many accounts
    
    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, acc):
        if type(acc) in [list, tuple, set]:
            for i in acc:
                self.__has_account(i)
                self.__accounts.append(i)
        else:
            self.__has_account(acc)
            self.__accounts.append(acc)

    def __has_account(self, acc):
        for i in self.accounts:
            if acc.cust.name == i.cust.name:
                raise ValueError('Customer aleready has an account!')
        return False

class Account:
    def __init__(self, number, customer):
        self.number = number
        self.customer = customer

    #number
    @property
    def number(self, number):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    #customer
    @property
    def customer(self, customer):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def setAge(self, age):
        if age < 18:
            raise ValueError("Age is too low!")
        self.__age = age

    


"""
3. Machine -> printer
Create a Machine class that takes care of powering on and off a the machine.   
Create a printer class that is a subclass of the Machine super class.   
The printer should be able to print to console.  
The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.  

"""

class Machine:
    def __init__(self, modelnumber):
        self.__modnr = modelnumber


class Printer(Machine):
    def __init__(self, modelnumber):
        
        # 1. 
        super().__init__(modelnumber)
        # 2. 
        Machine.__init__(self, modelnumber)



