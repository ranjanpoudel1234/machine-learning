## Partial function in python

from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
## The default values will start replacing variables from the left. The 2 will replace x. y will be equal to 4 when db(4) is called.
dbl = partial(multiply, 2)
print(dbl(4)) # prints 8



#Following is the exercise, function provided:
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

partialFunc = partial(func,5, 10,2)
print(partialFunc(6)) #60\