from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 1000 #need for sqrt() precision

def devils_wifi(position, n = 800):
    # the Chudnovsky brothers' formula
    # Each new term of the formula gives an additional 14 digits of pi.
    # by default n = 80 

    pi = Decimal(0)
    k = 0
    while n > k:
        pi += Decimal((-1)**k*factorial(6*k)*(13591409+545140134*k))/Decimal(factorial(k)**3*(factorial(3*k))*((640320)**3)**k)
        k += 1 
    pi *= Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return str(pi).split(str(position))[0][-8:]

print(devils_wifi(28638823))
assert devils_wifi(28638823) == "73115956", 'wrong password'