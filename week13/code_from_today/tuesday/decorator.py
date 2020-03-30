# decorator.py


# Functions in python are first class function
# functions can take other functions as parameters
# functions can return other functions


def my_first_class_function(x):
    return x

#def greet():
#    print('Hello')



# Inner functions

def foo():

    # define a function
    def inner():
        return 'inner msg'

    # executig
    #x = inner()
    #print(x)

    return inner


# simple decorator

def my_decorator(func):

    def wrapper(*args):
        print('Something before execution of func')
        func(*args) # print('Hello')
        print('Something happens after')
    
    return wrapper
"""
@my_decorator
def greet():
    print('Hello')
"""

# greet = my_decorator(greet)



"""
@my_decorator
def greet(name):
    print(f'Hello {name}')

@my_decorator
def greet_me_2():
    print('Hello')

"""


# decorator returning values

def my_dec(func):
    def wrapper(*args):
        x = 'From before \n'
        x += func(*args) + '\n'
        x += 'After func'
        return x
    return wrapper



@my_dec
def greet(name):
    return f'Hello {name}'



















    
