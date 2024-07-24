# # Description: This file demonstrates how to open, read, and close a file in Python.
# # Creating a file
# new_file = open('new_file.txt', 'x')

# # Writing to a file
# new_file.write('Once upon a time in a quaint village nestled between rolling green hills. \nThere lived a young girl named Elara. \nElara was known throughout the village for her curiosity and adventurous spirit. \nShe loved exploring the woods, climbing trees, and discovering hidden paths that led to magical places.\n')

# # Reading the contents of a file
# # print(new_file.read())


# # Opening a file in read mode
# new_file = open('new_file.txt', 'r')

# # Reading the contents of a file
# print(new_file.read())

# # Closing a file
# new_file.close()


def create_file():
    file_name = input('Enter the name of the file you want to create: ')

    content = input('Enter the content you want to write to the file: ')

    # Creating a file
    new_file = open(file_name, 'x')

    # Writing to a file
    new_file.write(content)

    # Closing a file
    new_file.close()

def read_file():
    file_name = input('Enter the name of the file you want to read: ')

    # Opening a file in read mode
    new_file = open(file_name, 'r')

    # Reading the contents of a file
    print(new_file.read())

    # Closing a file
    new_file.close()

def append_file():
    file_name = input('Enter the name of the file you want to append to: ')

    x = input('Enter the content you want to append to the file: ')

    # Opening a file in append mode
    new_file = open(file_name, 'a')

    # Appending to a file
    new_file.write(x)

    # Closing a file
    new_file.close()


def delete_file():
    file_name = input('Enter the name of the file you want to delete: ')

    # Deleting a file
    import os
    os.remove(file_name)
    print(f'{file_name} has been deleted successfully.')

# Assignment: Generate a story online and write a function that writes the story to a file. The story should be split into two parts. The first part should be written to a file while creating the file, and the second part should be appended to the file. Finally, the story should be read from the file and printed to the console.


# Step 1: Generate a story

# Step 2: Split the story into 2 parts

# Step 3: Create a file and write the first part of the story to a file

# Step 4: Update the story with the second part

# Step 5: Read the story from the file (i.e. print the contents of the file)

# All functions must run in one loop
