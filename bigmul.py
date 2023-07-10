from math import floor
import doctest
def prod(u : int, v : int):
    """this function multiplicate two big numbers recursively 
that receive from user
>>> 1254 * 4321
5418534

param u : big integer number 
param v : big integer number that multiplicate with u
param n1: calculate the length of the str(u)
param n2: calculate the length of the str(v)
param m : bisector of large numbers u,v with upper limit
param x, y : two parts of the u(123456: x = 123,y = 456)
param w, z : two parts of the v(654321: w = 654,y = 321)

returns: 
    u * v 
"""
    doctest.testmod()
    if u == 0 or v == 0:
        return 0
    elif u < 10 and v < 10:
        return u * v
    else:
        n1 = len(str(u))
        n2 = len(str(v))
        m = max(floor(n1/2),floor(n2/2))
        x = u // (10 ** m)
        y = u % (10 ** m)
        w = v // (10 ** m)
        z = v % (10 ** m)
        return (prod(x, w)*10**(m*2))+(prod(x, z)+ prod(w, y)) * (10 ** m) + prod(y, z)


print(prod.__doc__)
num_1 = int(input("Enter your first number:"))
num_2 = int(input("Enter your second number:"))    
print(prod(num_1, num_2))

