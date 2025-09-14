"""
Function = A block of code which is executed when it is called.
Default parameters = Assigning a value to parameter, which is used when no arguments are passed.
"""
def hello(name):
    print("Hello!" + " " + name)
    print("What's your plan today buddy?")
    
my_name = "Abhilash"    
    
hello(my_name)


def hello(first_name, last_name, age):
    print("Hello" + " " + first_name + " " + last_name)   
    print("You are" + " " + str(age) + " " + "Years old") 
    print("Great to see you bro!")
    
hello("Abhilash", "Raj", 24)

def my_function():
    print("I an Abhilash Raj ")
    print("And i am a python developer working in google.")
my_function()

import random
def get_answer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so."
    elif answerNumber == 3:
        return "Without a doubt"
    elif answerNumber == 4:
        return "Yes - definitely"
    elif answerNumber == 5:
        return "You may rely on it"
    elif answerNumber == 6:
        return "Reply hazy, try again."
    elif answerNumber == 7:
        return "Ask again later"
    elif answerNumber == 8:
        return "Better not tell you now"
    elif answerNumber == 9:
        return "Cannot predict now"

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)

def about_me(name, age):
    print("Hello, I am" + ' ' + name + ' ' + "I am " + str(age) + " Years old. " )
about_me("Abhilash", 23)

def print_something(name = "Abhi",  age = "Unknown"):
    print("Hello i am ", name, " and i am ",  age)
print_something(age = 24, name = "Unknown")

#  Return values from the function
def math_sum(num1, num2):
    return num1 * num2
math1 = math_sum(7, 9)
math2 = math_sum(12, 20)
print("The first sum is ", math1, "and the second sum is ", math2)

# Calculate area of rectangle.

def calc_rect_area(length, width):
    area = length * width
    print(area)
calc_rect_area(8, 4)

# Calculate area of circle.
import math
def cal_cir_area(r):
    area = math.pi * r * r
    print(area)
cal_cir_area(8)

# Draw triangle
def draw_triangle(height):   # Function parameters
    for i in range(1, height + 1):
        print(" " * (height - i) + "* " * i)

draw_triangle(5)  # Functions arguments

def cal_sum(a, b):
    sum = a * b
    print(sum)
    # return sum
cal_sum(8, 10)  # Arguments

# In another way
def cal_sum(a, b):
    return a + b
sum = cal_sum(5, 7)
print(sum)


"""
Write a function to print the length of a list.(list is the parameter)
"""

cities = ["Patna", "Delhi", "Mumbai", "Ahmedabad", "Indore", "Lucknow"]
def len_cities(cities):
    print(len(cities))
len_cities(cities)

"""
Write a function to print the elements in a single line.(list is the parameter.)
"""

heroes = ["Thor", "Captain America", "IronMan", "Wolverine", "Hulk", "Wanda"]
def len_heroes(heroes):
    print(len(heroes))
print(heroes[0], end=" ")    
print(heroes[1], end=" ")
len_heroes(heroes)