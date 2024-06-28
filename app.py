# How to declare variables in python
# Variables can be declared in python by assigning a value to it
x = 5 # This will declare a variable called "x" and assign the value of 5 to it
# Variables can also be declared without a value
y = None # This will declare a variable called "y" and it will have a value of None


# Data types in python
# Integers
a = 5

# Float
b = 5.5

# String
c = "Hello"

# Boolean
x = True
y = False
# print(x + y)

# Comments in python
# line 2
# line 3

"""
This is a multi-line comment
"""

# Adding two variables of different data types
i = 5 # Integer
p = 2.5 # Float
# print(i + p)

# String
w = "9"
x = "don"

# Adding two strings
# print(w + x)

# List
x = [8, "don"]

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(fruits[-1])

# Tuple
y = (True, "Adanna")

# Dictionary: Key/value pairs
dict = {"name": "Don", "gender": "M", "age": 20}

# Set: Unordered collection of items
set = {"Don", "M", 20}

k = 3 # int
l = 3.1 # float

# Printing the type of a variable
# print("Type of K is ", type(k))
# print("Type of L is ", type(l))

# Type casting in python
# Convert an integer to a string
a = str(3) # String

# Convert a float to an integer
b = int(6.5) # Integer

# Convert a string to an integer
c = int("5") # Integer

# print("Type of a is ", type(a))
# print("Type of b is ", type(b))
# print("Type of c is ", type(c))

# Slicing a string in python
h = "Slice me"
# print(h[0:5])

j = "TJ, 23"

q = str(890975423) # slicing a string

# print(q[0:2])

# print(name.strip())
# print(name.replace("D", "P"))
# print(name.split("o"))


# String methods in python
# Changing the case of a string
name = "Don"
# print(name.upper())
# print(name.lower())

# Using the strip method to remove whitespace 
names = " Don, Adanna, TJ, "
# print(names.strip())

# Using the replace method to replace a character in a string
# print(names.replace("Don", "Peter"))

# Using the split method to split a string
# print(names.split(","))

# Concatenating strings
a = "Hello "
y = " "
b  = "Don"
sentence = "how are you doing?"

# print(a + y + b + "," + y + sentence)

#Arithemetic Operations
# Addition
x = 10
# print(x)
y = 5

x = 5
# print(x)
x = 7
x = 3

# print(x)

# z = x + y

# print(z)

# Subtraction
# z = x - y

# print(z)

# # Multiplication
# z = x * y

# print(z)

# Division
# z = x / y

# print(z)

# Modulus
# x = 5
# y = 2

# z = x % y

# print(z)

# Exponentiation
z = 2 ** 2

# print(z)

# Floor division
z = 5 // 2

# print(z)

# Comparison Operators
x = 5
y = 2

# Greater than
# print(x > y)

# Less than
# print(x < y)

# print(0.3 < 0.35)

# # # Greater than or equal to
# x = 5
# y = 7

# print("The value of x is ", x)
# print("The value of y is ", y)

# print(x >= y)

# Less than or equal to
# print(x <= y)

# # Equal to
# print(x == y)

x = y

# print("The value of x is ", x)
# print("The value of y is ", y)

# print("Is x the same as y?", x == y)

# Not equal to
x = 4
y = 5

# ! not
# print(x != y)

# Logical Operators
# AND
w = 10
x = 5
y = 3
z = 7

# print(x > y)
# print(y < z)

# print(y < x and y < z and w < x)

# OR
# print(y < x or y > z or w < x)

# NOT
# print(not y > x)

# Membership Operators
# in
numbers = [1, 2, 3, 4, 5]

Y = {"keys": "values"}

dicts = {"name": "Adanna", "age": 23, "Gender": "F", "Adanna": ""}
car = {"name": "Toyota", "model": "Camry", "year": 2020}
device = {"name": "Samsung", "model": "Galaxy", "year": 2021, "price": 500, "color": "black", "RAM": 8}
song = {"name": "Don't stop", "artist": "Adanna", "year": 2021, "genre": "Afrobeat"}
a_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(song["artist"])

# print("RAM" in device)

# print(dicts)
# print the name of the person
# print(dicts["name"])

# print("Adanna" in dicts)

# print(3 in numbers)

# not in
# print(6 not in numbers)
# print("RAM" not in device)
# print("orange" not in a_tuple)

# Identity Operators
# is
x = 8
y = 8

print(x == y)
print(x is y)

# is not
# print(x is not y)

# Conditional Statements
# If statement
a = 5
b = 7


# if a == b:
#     print("a is equal to b")

# If else statement
# if a == b:
#     print("a is equal to b")
# else:
#     print("a is not equal to b")

# If elif else statement
# if a == b:
#     print("a is equal to b")
# elif a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is less than b")
