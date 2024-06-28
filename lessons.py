# Python Variable scopes

# Global Variables
x = 10

def add():
    # Local Variables
    x = 5
    y = 5
    z = x + y
    return z

y = 10
print(15)
print("The value of Y is: " + str(y))

def subtract():
    # Local Variables
    x = 15
    y = 5
    print(x - y)
    return(x - y)

def multiply():
    # Local Variables
    x = 5
    y = 5
    print(x * y)

def divide():
    # Local Variables
    x = 15
    y = 2
    print(x / y)

# Storing the return value of a function in a variable r and printing r
print(add())
# r = add()
# print(r)

# Calling the function subtract and printing the return value
# print(subtract())


# Random number generator
import random

# print(random.randint(20, 40))