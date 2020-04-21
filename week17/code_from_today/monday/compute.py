# computer.py

from time import sleep

def compute():
    val = []
    for i in range(10):
        sleep(.5)
        val.append(i)
    return val


class Compute:
    def __call__(self):
        val = []
        for i in range(10):
            sleep(.5)
            val.append(i)
        return val

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1 
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv


# generator function
def compute2():
    for i in range(10):
        yield i

# generator expression
g = (i for i in range(10))











