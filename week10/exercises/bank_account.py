""" Bank Exercise 

Create a 

* Bank class
* Account Class
* Customer class

The bank class should be able to hold many accounts.
You should be able to add new accounts.
The Account class should have relevant details.
The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.


## Overloading

Add the abillity in your code to overload one or more init methods

"""
class Account:
    def __init__ (self, name, age, account_number, password):
        self.name = name
        self.age = age
        self.account_number = account_number
        self.password = password

class Customer:
    def __init__ (self, name, age, fortune):
        self.name = name
        self.age = age
        self.fortune = fortune

class Bank:
    def __init__(self):
        self.accounts = []

    def addAccount(self, Account):
        self.accounts.append(Account)
        return self.accounts

    def deleteAccount(self, Account):
        self.accounts.remove(Account)
        return self.accounts


def main():
    accountA = Account("Jeppe", 25, 123498389, "Jeppe1234")
    accountB = Account("Carl", 22, 12324228389, "Carl1234")
    accountC = Account("Amber", 21, 29292000, "Amber1234")

    accountD = Account("Michael", 23, 29222000, "Michael1234")
    accountE = Account("Jasmin", 20, 1122000, "Jasmin1234")
    accountF = Account("Carlos", 21, 2929222000, "Carlos1234")

    bankA = Bank()
    bankB = Bank()

    #Adding accounts
    bankA.addAccount(accountA)
    bankA.addAccount(accountB)
    bankA.addAccount(accountC)

    bankB.addAccount(accountD)
    bankB.addAccount(accountE)
    bankB.addAccount(accountF)

    #Printing all accounts in a bank
    print("BankA accounts:")
    for account in bankA.accounts:
        print(account.name, account.age, account.account_number, account.password)

    print("")

    print("BankB accounts:")
    for account in bankB.accounts:
        print(account.name, account.age, account.account_number, account.password)

    bankB.deleteAccount(accountD)
    print("")

    print("BankB accounts deleted:")
    for account in bankB.accounts:
        print(account.name, account.age, account.account_number, account.password)
main()
