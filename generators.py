# Generators
# can be used to enforce sequencing..
from time import sleep


def compute():
    for i in range(10):
        sleep(.5)
        yield i


for val in compute():
    print(val)
