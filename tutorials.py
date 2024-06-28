#strip()
# a = "hello   world  "

# print(a.strip())


#replace()
 
# x = "hello, world"
# print(a.replace("h", "j"))

# split()

# x = "Hello, World"
# a = x.split(",")
# print(a)


# a = "hello"
# b = "world"
# c = a + " " + b
# print(c)

# age = 36

# txt = f"my name is Newman, i am  {age}"
# print(txt)

# price = 50
# txt = f"The price is {price} dollars"
# print(txt)

# escape character

# text = "we are the so-called \"vikings\" from the north"
# print(text)

# print(10 > 9)
# print(9 > 10)

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")



# python operators

# x + y, x-y, x*y, x/y, x%y x ** y
# x = 5
# y = 3
# print(x + y)

# x = 5
# y = 3
# print(x - y)

# x = 2
# y = 3
# print(x * y)

# x = 8
# y = 2
# print(x / y)

# x = 3
# y = 2
# print(x % y)

# x = 20
# b = 3
# print(x % b)

# 2*2*2*2*2
# x = 2 
# y = 5
# print(x ** y) 

# Assignment Operators

# x = 5
# print(5 == 5)

# x = 4
# y = 2

# print(x - y)

 # x += 3   is the same as x = x + 3
# x = 5
# x += 3
# print(x)

# x = 5
# x -= 3
# print(x)

 
 #Python User Input 
   
# username = input("Enter username: ")  
# print("your username is: " + username)

# first_number = float(input("Enter first number: "))
# operator = input("Choose operator from the list('+', '-', '*', '/'): ")
# second_number = float(input("Enter second number: "))

# if operator == '+':
#     print(first_number + second_number)
# elif operator == '-':
#     print(first_number - second_number)
# elif operator == '*':
#     print(first_number * second_number)
# elif operator == '/':
#     print(first_number / second_number)
# else:
#     print("invalid operator")
    
    
# x = "people"
# print(type(x))

# List

# thislist = ['cherry', 'banana', 'apple', 'apple']
# print(thislist)

# print(len(thislist))

# thislist = ['cherry', 'banana', 'apple', 'apple', 23, True, False]

# print(type(thislist))
# print(thislist)

#Acess list items

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# # print(thislist[1])
# # print(thislist[3])

# print(thislist[-3])

#Change list items

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thislist[2] = 'cucumber'
# print(thislist)

#Add list items

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thislist.append('orange')
# print(thislist)

#Insert()
# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thislist.insert(3, 'orange')
# print(thislist)

#Extend list

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# tropical = ['mango', 'pinapple', 'papaya']

# thislist.extend(tropical)
# print(thislist)

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thisturple = ('mango', 'pinapple', 'papaya')
# thislist.extend(thisturple)
# print(thislist)

#Remove()

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thislist.remove('cherry')
# print(thislist)

#POP()

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thislist.pop()
# print(thislist)

# thislist.pop(3)
# print(thislist)

#del keyword

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# # del thislist[0]
# # print(thislist)
# del thislist
# print(thislist)


# clear()

# thislist = ['cherry', 'banana', 'apple', 'watermelon']

# thislist.clear()

# del thislist

# print(thislist)

# copy()
# firstlist = ['cherry', 'banana', 'apple', 'watermelon']
# secondlist = firstlist.copy()
# print(firstlist)
# print(secondlist)

# Sort()
# li = [1, 3, 4, 2, 5, 6, 7, 8, 9, 10]
# li.sort()
# print(li)

# Tuple methods

# thistuple = ('cherry', 'banana', 'apple', 'watermelon')
# print(thistuple)

# print(type(thistuple))

# append() method does not work with tuple
# thistuple.append('orange')

# remove() method does not work with tuple
# thistuple.remove('cherry')

# Pop() method does not work with tuple
# thistuple.pop()

# del keyword works with tuple
# del thistuple

# print(thistuple)

# clear() does not work with tuple
# print(thistuple.clear)

# copy() works does not work with tuple
# firsttuple = ('cherry', 'banana', 'apple', 'watermelon')
# secondtuple = firsttuple.copy()

# print(secondtuple)

# Count method (count())
# tup = ('cherry', 'banana', 'apple', 'watermelon', 'apple')
# print(tup.count('banana'))

# x = (1, 2, 3, 1, (1, 2), (), (1, 2), (), [], [], True, True, False)
# print(x.count(False))

# Index method (index())
# print(tup.index('banana'))

# Set methods

# thisset = {'cherry', 'banana', 'apple', 'watermelon'}

# Append() method does not work with set
# thisset.append('orange')

# # Add() method works with set
# thisset.add('orange')

# Pop()
# thisset.pop()
# thisset.pop()
# print(thisset)

# Remove() method 
# thisset.remove('banana')

# Discard() method
# thisset.discard('banana')

# Clear() method
# thisset.clear()

# Copy() method
# secondset = thisset.copy()

# Difference() method
# A = {'cherry', 'banana', 'apple', 'watermelon', 'pineapple'}

# B = {'cherry', 'banana', 'apple', 'watermelon', 'orange', 'mango'}

# A - B
# print(A.difference(B))
# B - A
# print(B.difference(A))

#Difference_update() method
# A.difference_update(B)
# print(A)

# # Union() method
# print(A.union(B))

# Intersection() method
# print(A.intersection(B))

# Intersection_update() method
# print(A.intersection_update(B))
# print(A)


#  PYTHON DICTIONARIES

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "year": 2020,
# }

# print(thisdict)
# print(type(thisdict))
# print(len(thisdict))

# print(thisdict["brand"])

# print(thisdict)

#access a dictionary

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# # print(thisdict)

# # x = thisdict["model"]
# # print(x)

# x = thisdict.get("year")
# print(x)

#Get the keys

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# x = thisdict.keys()
# print(x)

# y = thisdict.values()
# print(y)

# items() = used to return the keys and values in form of a turple inside a list

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# x = thisdict.items()
# print(x)

# thisdict["year"] = 2024

# print(x)

#check if key exists

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# if "brand" in thisdict:
#     print("yes, brand is one of keys in thisdict")
    
#change dictionaries items

# update()
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# thisdict.update({"year": 2024})
# print(thisdict)

#Add items to a dictionary

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# thisdict["color"] = "red"
# print(thisdict)

# thisdict.update({"color":"blue"})
# print(thisdict)

#Remove dictionary items
   # pop()
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "electric": False,
# }

# thisdict.pop("electric")
# print(thisdict)

# popitem()
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# thisdict.popitem()
# print(thisdict)

# #del keyword
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# del thisdict["model"]
# print(thisdict)

# del thisdict
# print(thisdict)

# clear()
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# thisdict.clear()
# print(thisdict)

#looping through a dictionary
   #we can loop throught a dictionary using the python for loop(a for loop is used to ilterate
   # over a sequence like a list, turple, strings or other ilterable objects)
   # iterating over a sequence means going through each element one by one.
   
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# for x in thisdict:
#    print(x)

# for x in thisdict.keys():
#    print(x)

# for x in thisdict.values():
#    print(x)


# for x, y in thisdict.items():
#    print(x, y)

#copy a dictionary
   #copy()
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# mydict = thisdict.copy()
# print(mydict)

#dict()

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964,
#     "elctric": False,
# }

# mydict = dict(thisdict)
# print(mydict)

# Nested Dictionary

# myfamily = {
#    "child1" : {
#       "name": "peter",
#       "year": 2004
#    },
#    "child2" : {
#       "name": "john",
#       "year": 2007
#    },
#    "child3": {
#       "name": "promise",
#       "year": 2011
#    }
# }


# print(myfamily["child2"]["name"])


# PYTHON WHILE LOOP
# A LOOP - is a sequence of instructions that is continually repeated until a certain condition is reached.

#python has two primitive loop commands:
  #while loops
  #for loops
  
# i = 2
  
# while i <= 10:
#    print(i)
#    i += 2 # i = i + 2
   
   #break statement
   
# i = 0
# while i < 8:
#    print(i)
   
#    if i == 4:
#       break
#    i += 1 # i = i + 1
  
  # continue statement
# i = 0
# while i < 8:
#    i += 1
#    if i == 3:
#       continue
#    print(i)
   
   
# i = 1
# while i < 6:
#    print(i)
#    i += 1
# else:
#    print("i is no longer less than 6")

# i = 1
# while i <= 10:
#    print("Hello World")
#    i += 1
   
# i = 10
# while i >= 1:
#    print(i, "Hello World")
#    i -= 1

#PYTHON FOR LOOPS

# A for loop is used for ilterating over a sequence(that is either a turple,list,dictionary,set or a string).

# fruits = ["apple", "banana", "cherry", "cucumber"]

# # for x in fruits:
# #    print(x)

# for x in "banana":
#    print(x)

# fruits = ["apple", "banana", "cherry", "cucumber"]

# for x in fruits:
#    print(x)
#    if x == "cherry":
#       break

#we can stop the current ilteration of the loop and continue with the next using the continue statement

# fruits = ["apple", "banana", "cherry", "cucumber"]

# for x in fruits:
#    if x == "banana":
#       continue
#    print(x)

# The range() function

# for x in range(6):
#    print(x)

# for x in range(2, 6):
#    print(x)

# for x in range(2, 30, 3):
#    print(x)

# Else in for loop
# for x in range(6):
#    print(x)
# else:
#    print("finally finished!")

# Nested loop

# the inner loop will be executed one time for each ilteration of the outer loop
# adjective = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "chery"]

# for x in adjective:
#    for y in fruits:
#       print(x, y)
      
      
#PYTHON FUNCTION

# A function is a reusable block of code used to perform certain task when ever it called
# def keyword

# def myfunction():
#    greetings = "Hello Adanna"
#    some_more_greetings = "How are you doing"
#    print(greetings + " " + some_more_greetings)

# # print(greetings)

# myfunction()
# Positional arguments
def hello_p(title, name):
   print("Hey, " + title + " " + name)

# hello_p("Mr", "Duke")

# Keyword arguments
def hello_k(title, name, age): 
   print("Hey, " + title + " " + name)
   print("You are " + str(age) + " years old")

# hello_k(name="Duke", title="Mr", age=20)

# Nested function
def outer_function():
   print("This is the outer function")

   def inner_function():
      print("This is the inner function")

      def inner_inner_function():
         print("This is the inner inner function")
      
      inner_inner_function()
   
   inner_function()

outer_function()

# Return statement
