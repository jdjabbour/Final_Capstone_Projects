####################################################################################################################
# Udemy Complete Python Bootcamp
# Final Capstone Project: Fibonacci Sequence
# Completed on: 8/16/17
####################################################################################################################

def fibseq(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        t = a
        a = b
        b = t + a

for i in fibseq(10):
    print(i)