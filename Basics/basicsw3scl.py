'''
    Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
'''
#   Check the Python version of the editor:
# import sys
# print(sys.version)

#   The Python Command Line
#   Open Terminal => C:\Users\Your Name> python => (for Start)
#   to quit the python command line interface:  => exit()

'''
    Python Statements:
    Semicolons are optional in Python. You can write multiple statements on one line
    by separating them with ; but this is rarely used because it makes it hard to read:
    Print Without a New Line:
    By default, the print() function ends with a new line.
    If you want to print multiple words on the same line, you can use the 'end' parameter:
'''
#   You can use either " double quotes or ' single quotes:
# print('Hello World!')
# print("Hello World!")

# print("Python is fun!") print("Really!")    #   ERROR
# print("Python is fun."); print("Python is used in AI/ML")   #   ; as a separator

# print("Hello World!", end=" ")  #   we add a space after end=" " for better readability.
# print("Python is really fun.")

# print("I am", 35, "years old.")     #   Mix Text and Numbers


'''
    Python Variables:
    Variables are containers for storing data values.
    Variable Names:
    A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
    Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
'''
# x = 5
# y = "John"
# print(x)
# print(y)

#   Variables do not need to be declared with any particular type, and can even change type after they have been set.
# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

#   If you want to specify the data type of a variable, this can be done with casting.
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

#   Get the Type
#   You can get the data type of a variable with the type() function.
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

#   Single or Double Quotes?
#   String variables can be declared either by using single or double quotes:
# x = "John"
# # is the same as
# x = 'John'

#   Case-Sensitive
#   Variable names are case-sensitive.
# a = 4
# A = "Sally"
# #A will not overwrite a

'''
    Multi Words Variable Names
    1.  Camel Case
    Each word, except the first, starts with a capital letter:
    myVariableName = "John"
    2.  Pascal Case
    Each word starts with a capital letter:
    MyVariableName = "John"
    3.  Snake Case
    Each word is separated by an underscore character:
    my_variable_name = "John"
'''

#   Python Variables - Assign Multiple Values
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

#   One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

#   Unpack a Collection
#   If you have a collection of values in a list, tuple etc. Python allows you to
#   extract the values into variables. This is called unpacking.
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
'''
    Python - Output Variables
'''
# x = "Python"
# y = "is"
# z = "awesome"
# print(x,y,z)    #   Python is awesome

# x = "Python "
# y = "is "
# z = "awesome"
# print(x+y+z)    #   Python is awesome

# x = 5
# y = "John"
# print(x, y)     #   Output: 5 John
# print(x + y)     #   Output: ERROR