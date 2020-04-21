# start_example.py

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        val = func(*args)
        end = (time.time()) - start
        print(f'Time elepsed: {end}')
        return val
    return wrapper

# @timer
@profile
def sum_of_list():
    return sum([i*i for i in range(1, 100000)])

@profile
def sum_of_gen():
    return sum((i*i for i in range(1, 100000)))


sum_of_list()
sum_of_gen()
