#dec.py
from time import time
def timer(func, x, y):
    before = time()
    rv = func(x, y)
    after = time()
    print('elapsed', after - before)
    return rv

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print('add(10)', timer(add, 10, 20))
print(add(10, 20), add(10,30))
