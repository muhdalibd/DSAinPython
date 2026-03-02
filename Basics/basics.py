### Introduction to Programming
#   Programming == creating a set of instructions - that tells
#       a computer how to perform a task.
#       Those set of instruction called => Program

#   In Python Programming Language:
#       Source Code => Compiler => Byte Code => Interpreter => Mechine Code



### Introduction to Python and DSA
#   One of the most famous language
#   Easy to learn & understand
#   Beginer friendly
#   Concise Code & Open Source
#   Versatile => Web Dep., AI/ML, Data Science, Data Analytics, IOT

#   Download => VS Code & Python


### Starting with Python
# print("Hello World!")


''' Chapter 1: Basics
    01. Basics Program
    02. Python CLI
    03. Comments
    04. Indentation
    05. Variables
    06. Keywords in Python
    07. Data Types
    08. ASCII and Unicode
    09. Taking Input
    10. Operators
    11. Typecasting & type() function
    12. Hierarchy'''


#   Basic Program in Python
# print("Hello World!")
#   How to move to next line
# print("Hello,\nWorld!")


#   Pyhon CLI
''' Command Line Interface
        Command => python3 (for Start)
        REPL => Read Evaluate Print Loop
        Command => exit() or ^D '''



#   Python Comments
'''This is a multi line comment'''


#   Python Indentation
'''print("Hello World!")
    print("Hello World") # This is called Indentation Error'''
#   Indentation => Tab Space Basicaly


#   Variables and their Declarations
'''
    Variables => container used to store data.
        In programming container means Memory Space.
    Data can be different types. (Integer, Float, String, Boolean, NULL)
    In Python, Variables do not need to be declared with any particular type.
            Python is dynamically typed.
'''
#   Variable Naming Rules:
'''
    1. A variable name must start with a letter or underscore character.
    2. A variable name cannot start with a number.
    3. A variable name can only contain alphanumeric and underscores (A-z,0-9,_)
    4. Variable names are case-sensitive (count, Count & COUNT are three different variables)
    5. A variable name cannot be any of the Python Keywords.

        is_student => Snake Case (Prefered in Python)
        isStudent => Lower Camel Case
'''

'''   String   '''
name = "Isha"
# print(type(name))   # <class 'str'>
'''   Integer  '''
roll_no = 17
# print(type(roll_no))    # <class 'int'>
'''   Float    '''
percentage = 95.8
# print(type(percentage)) # <class 'float'>
'''   Boolean  '''
is_student = True
# print(type(is_student)) # <class 'bool'>

# print(name, roll_no, percentage, is_student)

'''   Updating the value:   '''
# percentage = 94
# print(name, roll_no, percentage, is_student)

'''   Printing with additional words  '''
# print("My name is " + name)   # Concatinate String
# print("My roll number is " + roll_no)     # TypeError: roll-no is Integer
# print("My roll number is ", roll_no)    # Right
# print("I scored", percentage, "% in my final exams.")

'''   Printing Expressions   '''
# print("My percentage has changed to", percentage - 5.0)

'''   Printing with Seperator   '''
# print(name, roll_no, percentage, is_student, sep="-")
# x = 1
# y = 2
# z = 3
# print(x,y,z, sep=" -> ")


#   Keywords in Python:
#       Search in Internet.


#   Python Data Types
'''
    1. Numeric => (Integer, Float, Complex Number)
    2. Boolean ==> (True or False)
    3. Sequence Type => (String, List, Tuple,)
    4. Dictionary => (Key value pairs stored)
    5. Set => (Unorder collection of unique items)
    6. None => NULL value
'''


#   ASCII & Unicode Values
'''
    ASCII => American Standard Code for Information Interchange.
    '        Represent Characters as Numeric Codes.
        A - Z ==> 65 - 90
        a - z ==> 97 - 112
        0 - 9 ==> 48 - 57
        Space ==> 32
'''
'''   ord( ) Function ==> Return ASCII value of a character    '''
# char = ' '
# print(ord(char))  # 32

'''   chr( ) Function ==> Opposite of ord( ) function  '''
# ascii = 67
# print(chr(ascii))   # C



'''   Taking Input from User   '''
# name = input("Enter your name: ")   # input() ==> always captured as string
# print("Your name is " + name)


'''   Typecasting  '''
#       process of converting one data type to another.

# age = input("Enter your age: ")
# print(type(age))    # <class 'str'>
# age = int(input("Enter your age: "))
# print(type(age))    # <class 'int'>

'''   Exercise   '''
#   Sum of Two Given Numbers:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum = num1 + num2
# print("Summation =", sum)



#   Operators:
'''
    1. Arithmetic Operators ==> (+, -, *, /, %, **, //)
    #       ==> ** (Exponential) = (4 ** 3 -> 64) == (4 * 4 * 4 -> 64) &
    #       ==> // (Floor Division) = return nearest whole number (4//3 --> 1)
    2. Assignment Operators ==> (=, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=)
    3. Comparison Operators
    4. Logical Operators
    5. Identity Operators
    6. Membership Operators
    7. Bitwise Operators
'''