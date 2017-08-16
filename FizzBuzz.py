######################################################################################################################
# This is the FizzBuzz code
# If a number is a multiple of 3, then it will print Fizz
# If the number is a multiple of 5, it will print Buzz
# If it is a multiple of both, it will print FizzBuzz
# Completed 8/16/17 ~ Jason Jabbour
######################################################################################################################

def fizzbuzz(n):
    for i in range(n):
        if i%5 == 0 and i%3 == 0:
            print(i, ' FizzBuzz')
        elif i%3 == 0:
           print(i, ' Fizz')
        elif i%5 == 0:
            print(i, ' Buzz')
        else:
            print(i)

print(fizzbuzz(16))