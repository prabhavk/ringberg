def Factorial(n): # F(n) = n * F(n-1). F(0) is defined to be 1
    assert(n == abs(int(n))) # checks whether or not n is a non-negative integer
    if (n == 0):
        return (1)
    else:
        return (n * Factorial(n-1))

def Fibonacci(n): # What is the nth number in the Fibonacci series F(n) = F(n-1) + F(n-2). The first two numbers in the series are 1. 
    assert(n == abs(int(n)) and n > 0) # checks whether or not n is a positive integer
    if (n == 1):
        return (1)
    elif (n == 2):
        return (1)
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))



def addition(x):
    x = x*2
    return (x)

