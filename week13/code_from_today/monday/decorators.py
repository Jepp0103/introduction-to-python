# decorators.py

# Functions are first class functions.
# functions can take other functions as parameters
# fnctions can return functions as return values


def my_first_class_function(x):
    print(x())
    return x

#def greet():
#    return 'Hello'



# inner
def foo():

    # declare
    def inner():
        return 'Hello from inner'

    return inner


# simple decorator

def my_decorator(func):
    def wrapper(*args):
        print('This is before functions execution')
        func(*args) # print('Hello')
        print('This is done after execution')
    return wrapper


"""
@my_decorator
def greet():
    print('Hello')


# greet = my_decorator(greet)
"""
"""
@my_decorator
def greet(name):
    print(f'Hello {name}')
"""
@my_decorator
def greet2(name, age):
    print(f'Hello {name}, {age}')




def me_2_decorator(func):
    def wrapper(*args):
        x = 'Before execution of func'
        x += func(*args)
        x += 'After execution'
        return x
    return wrapper


@me_2_decorator
def greet(name):
    return f'Hello {name}'

x = greet('Anna')
#print(x)
