# add.py

from datetime import datetime

def log(func):
    def wrapper(*args):
        # log to a text file
        f = open('log.txt', 'a+')
        f.write(f'{datetime.now()}, {args} = {func(*args)} \n')
        return func(*args)
    return wrapper


@log
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

@log
def printer(text):
    return text * 2
