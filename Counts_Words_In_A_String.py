####################################################################################################################
# Udemy Complete Python Bootcamp
# Final Capstone Project: Count Words in a String
# Completed on: 8/16/17
####################################################################################################################
from collections import Counter

s = 'Hello this is a sting and this is also part of a string'
x = [i for i in s.split()]
print(Counter(x))


