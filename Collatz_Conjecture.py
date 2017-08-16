####################################################################################################################
# Udemy Complete Python Bootcamp
# Final Capstone Project: Collatz Conjecture
# Completed on:
# Side note: One of my favorite mathematical conjectures!!
# F(n) = n/2 if n(mod2)=0 or 3n+1 if n(mod2)=1
####################################################################################################################

def collatz(i):
    #for i in range(n):
    while i > 1:
        if i % 2 == 0:
            i = i/2
            print(i)
        else:
            i = (3*i)+1
            print(i)


print(collatz(50))
