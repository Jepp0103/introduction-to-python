""" Bank Exercise 

Create a 

* Bank class
* Account Class
* Customer class

The bank class should be able to hold many account.
You should be able to add new accounts.
The Account class should have relevant details.
The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.


## Overloading

Add the abillity in your code to overload one or more init methods

"""

class Bank:

    def __init__(self, name):
        self.accounts = {}
        self.name = name

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.accounts)

class Account:
    def __init__(self, acc_no, cust):
        self.acc_no = acc_no
        self.cust = cust


class Customer:
    def __init__(self, name):
        self.name = name


class CaymanIslandBank(Bank):
    def __init__(self, name):
        super().__init__(name)



class A:
    def __init__(self, name):
        self.name = 'aaa'

class B:
    def __init__(self, name):
        self.name = 'bbb'

class C(A, B):
    def __init__(self, name):
        A.__init__(self, name)
        B.__init__(self, name)






bank = Bank('Claus')
cust = Customer('Claus')
acc = Account('1234', cust)
"""
bank.account[cust] = acc

bank.add_account(cust, acc)

"""













