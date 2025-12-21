from random import *
def FOIL(a, b, c, d, x):
    a*x=a1
    c*x=a2
    #First Outer Inner Last
    result = a1 * a2 + a1 * d + a2 * b + b * d
    print(a)
    print(b)
    print(c)
    print(d)
    print(x)
    print(result)
FOIL(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

