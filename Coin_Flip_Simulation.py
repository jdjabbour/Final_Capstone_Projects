####################################################################################################################
# Udemy Complete Python Bootcamp
# Final Capstone Project: Coin Flip Simulation
# Completed on: 8/28/17
####################################################################################################################
import random

def flip(n):
    flip_count = 0
    heads = 0
    tails = 0
    while flip_count <= n:
        x = random.randrange(1, 3)
        if x == 1:
            heads += 1
        else:
            tails += 1

        flip_count += 1
    print('Heads: %s' % heads)
    x = heads/n
    x = x*100
    print('Percentage of flips: %s' % x)
    print('Tails: %s' % tails)
    y = tails/n
    y = y*100
    print('Percentage of flips: %s' % y)




z = int(input('Enter the number of flips: '))
flip(z)