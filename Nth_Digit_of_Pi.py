####################################################################################################################
# Udemy Complete Python Bootcamp
# Final Capstone Project: Pi to the Nth digit
# Completed on: 8/24/17
# Side Note: Used the Gauss-Legendre Algorithm
# Found this algorithm on Stack Overflow:
# https://stackoverflow.com/questions/347734/gauss-legendre-algorithm-in-python
# I have altered it in some ways.  I have set it to ask for the value.
####################################################################################################################

import decimal


def pi_calc():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        a = 1
        b = 1/D(2).sqrt()
        t = 1/D(4)
        p = 1
        pi = None
        while 1:
            an = (a+b)/2
            b = (a*b).sqrt()
            t -= p*(a - an)*(a-an)
            a = an
            p = 2*p
            piold = pi
            pi = ((a+b)*(a+b))/(4*t)
            if pi == piold:
                break
    return +pi

digit = int(input("Enter the digit you would like to print Pi up to: "))
decimal.getcontext().prec = digit
print(pi_calc())