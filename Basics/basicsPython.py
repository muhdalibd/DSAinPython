# print("Hello World!")
# print('Hello World!')   # prefer double quote

#   This is my first Python Program.

# print("I like pizza.")
# print("It's really good.")

'''
    # Variable = A container for a value (string, integer, float, boolean)
    '            A variable behaves as if it was the value it contains.
'''



''' String  '''

# first_name = "Bro"
# # first_name = 'Bro'  #   prefer double quote
# food = "pizza"
# email = "bro123@fake.com"

# print(first_name)
# print(f"Hello, {first_name}.")
# print(f"You like {food}.")
# print(f"Your e-mail is: {email}")



''' Integers  '''

# age = 25
# quantity = 3
# num_of_students = 30

# print(f"You are {age} years old.")
# print(f"You are buying {quantity} items.")
# print(f"Your class has {num_of_students} students.")



''' Float   '''


# price = 10.99
# gpa = 3.2
# distance = 5.5

# print(f"The price is ${price}.")
# print(f"Your CGPA is {gpa}.")
# print(f"You walked at {distance} km.")



''' Boolean '''


# is_student = False
# # print(f"Are you a student?: {is_student}")
# if is_student:
#     print("You are a student.")
# else:
#     print("You are not enrolled.")


# for_sale = True
# if for_sale:
#     print("That item is for sale.")
# else:
#     print("That item is NOT available.")


# is_online = True
# if is_online:
#     print("You are online.")
# else:
#     print("You are offline.")



'''
    Typecasting = The process of converting a variable form one data type to another
    '               str(), int(), float(), bool()
'''

# name = "Bro Code"
# age = 25
# gpa = 3.2
# is_student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# gpa = int(gpa)
# print(type(gpa))
# print(gpa)

# age = str(age)
# print(type(age))
# print(age)  #   25

# age += "1"
# age += 1    #   Cann't Concatinate with Integer
# print(age)  #   251

# # name = ""
# name = bool(name)
# print(type(name))
# print(name)



'''
    input() = A function that prompts user to enter data
    '         Returns the entered data as a String.
'''

# name = input("What is your name?: ")
# age = input("How old are you?: ")
# print(f"Hello, {name}.")
# print(f"You are {age} years old.")

# # age = age + 1   #   can only concatenate str (not "int") to str
# print("Happy Birthday!")

# age = int(input("How old are you?: "))
# age += 1
# print(f"You are {age} years old.")


'''
    EXERCISE 01: Rectangle Area Calc
'''

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area is {area} cm²")    #   NumLock + Alt + 0178


'''
    🟧  EXERCISE 02: Shopping Card Program
'''

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
# print(f"You have bought {quantity} x {item}/s")
# print(f"You have to pay ${total}")


'''
    Madlibs Game
    '   Word game where you create a story
    '   by filling in blanks with random words
'''

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (persion, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}")


'''
    Arithmetic Operators
'''

# friends = 5
# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 3
# print(friends)
# remainder = friends % 2
# print(remainder)


''' Some Important Function '''


# x = 3.14
# y = -4
# z = 5

# result = round(x)   #  3
# result = abs(y)     #  4
# result = pow(4, 3)  # 64
# result = max(x, y, z)  # 5
# result = min(x, y, z)  # -4
# print(result)


'''   Some Important Math Function  '''


# import math
# x = 9.1
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)   # round next integer
# result = math.floor(x)  # round previous int 
# print(result)



'''
    EXERCISE 03: Cercumference of Circle
'''

# import math
# radius =  float(input("Enter the radius of a circle ?: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is {round(circumference, 2)} cm.")



'''
    EXERCISE 04: Area of Circle
'''

# import math
# radius =  float(input("Enter the radius of a circle ?: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is {round(area, 2)} cm².")



'''
    EXERCISE 05: Hypotenous of Right Angle
'''

# import math
# a =  float(input("Enter side A ?: "))
# b =  float(input("Enter side B ?: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"The side C of right angle is: {c}.")




'''
    if = Do some if some condition is True
    '    Else do something else
'''


# age = int(input("Enter your age: "))
# if age >= 100:
#     print("You are too old to sign up!")
# elif age >= 18:
#     print("You are now signed up!")
# elif age <= 0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to sign up.")


# responce = input("Would you like food? (Y/N): ")
# if responce == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")


# name = input("Enter your name: ")
# if name == "":
#     print("You did not type your name!")
# else:
#     print(f"Hello, {name}")


# for_sale = True
# if for_sale:
#     print("This item  is for sale.")
# else:
#     print("This item is NOT available.")


# online = False
# if online:
#     print("The user is online.")
# else:
#     print("The user is offline.")



'''
    EXERCISE 06: Python Calculator
'''

# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# result = 0

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     result = num1 / num2
# else:
#     print("Enter valid operator.")

# print(f"{num1} {operator} {num2} = {round(result, 2)}")



'''
    EXERCISE 07: Python Weight Converter
'''

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pound? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Libs."
#     print(f"Your weight is {round(weight, 2)} {unit}.")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is {round(weight, 2)} {unit}.")
# else:
#     print(f"{unit} was not valid.")

'''
    EXERCISE 08: ⭐ Temperature Conversion 🌡️
'''

# temp = float(input("Enter the value of temperature: "))
# unit = input("Enter temperature unit (F/C): ")

# if unit == 'F':
#     result = (5/9)*(temp-32)
#     print(f"The Temperature in Celsius is: {round(result,2)}°C")
# elif unit == 'C':
#     result = (9/5)*temp + 32
#     print(f"The Temperature in Fahrenheit is: {round(result,2)}°F")
# else:
#     print(f"{unit} is a invalid unit of measurement")


'''
    Logical Operators = Evaluate multiple conditions (or, and, not)
    '                   or  = at least one condition must be true
    '                   and = both conditions must be True
    '                   not = inverts the condition (not False, not True)
'''

# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")


temp = 25
is_sunny = True

if temp > 28 and is_sunny:
    print("It is HOT outside.")
elif temp <=0 and is_sunny:
    print("It is COLD outside.")
else:
    print("It is SUNNY.")