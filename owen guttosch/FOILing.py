from random import *
def FOIL(a, b, c, d, x):
    e=a*x
    f=c*x
    #First Outer Inner Last
    result = e * f + e * d + f * b + b * d
    print(a)
    print(b)
    print(c)
    print(d)
    print(x)
    print('comes to:')
    print(result)
    print()

for i in range(10):
    FOIL(randint(0,i), randint(0,i), randint(0,i), randint(0,i), randint(0,i))

