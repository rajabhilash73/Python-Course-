"""
1. Write a program to input two numbers and print their sum.
"""
# First_Number = int(input("Enter the first number : "))
# Second_Number = int(input("Enter the second number : "))
#
# print("Sum = ", First_Number + Second_Number)
#
# """
# 2. Write a python program to print area of square.
# """
# first= float(input("Enter the first side of square : "))
# second= float(input("Enter the second side of square : "))
# area_of_square = (first * second)
# print("The area of square is :", area_of_square)
#
# """
# 3. Write a program to calculate average of two numbers.
# """
# first= float(input("Enter the first number : "))
# second= float(input("Enter the second number : "))
# print("average = ", (first + second)/ 2)
#
# """
# 4. Write a program to enter 2 integer value a and b. Print true if a is greater than or equal to b. if not print false.
# """
# a= int(input("Enter the first value : "))
# b= int(input("Enter the second value : "))
#
# print(a>=b)

# Strings questions

"""
1. Write a prython program to input user's first name and print it's length.
"""
# first_name = input("Enter your first name : ")
# print("The length of the first name is : ", len(first_name))
#
# print(type(first_name))
#
# """
# 2. Write a program to find occurence of '$' in a string.
# """
#
# str = "I am abhilash raj and i have money in dolllar $"
# print(str.count("$"))

# If-elif-else statements
"""
Write a python program to gives grades to the students according to their marks.
"""
# marks = int(input("Enter your marks : "))
# if(marks>=90):
#     print("You scored A.")
# elif marks>=80 and marks<90:
#     print("You scored B.")
# elif marks>=70 and marks<80:
#     print("You Scored C.")
# elif marks >= 60 and marks < 70:
#     print("You Scored D.")
# elif marks >= 50 and marks < 60:
#     print("You Scored E.")
# elif marks >= 40 and marks < 50:
#     print("You Scored E+.")
# else:
#     print("You scored nothing")


# We use nesting in this code, in which we can write if statement in if statement.
# age = int(input("Enter your age : "))
# if age >= 18:
#     if age >= 80:
#         print("You are not allowed to drive a vehicle, because you are too old.")
#     else:
#         print("You can drive a vehichle.")
# else:
#     print("You can not drive a vehicle.")


"""
Q. Write a python program to check the input number is even or odd.
"""
# num = float(input("Enter a number : "))
# if num % 2 == 0:
#     print("The number is even number.")
# else:
#     print("The number is odd")

# """
# Q. Write a program in python to find the greatest of 3 numbers entered by an user.
# """
# num1 = float(input("Enter first number : "))
# num2 = float(input("Enter second number : "))
# num3 = float(input("Enter third number : "))
# if num1 > num2 and num1 > num3:
#     print("The greatest number is num1 : ", num1)
# elif num2 > num1 and num2 > num3:
#     print("The greatest number is num2 : ", num2)
# elif num3 > num1 and num3 > num2:
#     print("The greatest number is num3 : ", num3)
# else:
#     print("Byee")
#
# """
# Q. Write a program to check if a number is multiple of 7 or not.
# """
#
# num = int(input("Enter a number : "))
# if num % 7 == 0:
#     print("The number is multiple of 7.")
# else:
#     print("It is not multiple of 7.")
#     print("Thank you for your input.")

# Tuple question
# """
# Q. Write a python program to ask user to enter names of their 3 favourite movies and store them into list.
# """
# movies = []
# movie1 = input("Enter your favourite movie : ")
# movie2 = input("Enter your favourite movie : ")
# movie3 = input("Enter your favourite movie : ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)
#
# """
# Q. Write a program to check if a given number is palindrome or not.
# """
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
#
# copy_list1 = list1.copy()
# copy_list1.reverse()
#
# if list1 == copy_list1:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")
#
# """
# Q. Write a program to count number of students of grade "A" in the following tuple.
# """
# grade = ("A", "B", "A", "C", "A", "B")
# print(grade.count("A"))
#
# """
# Write a python program to store the above value in list and sort them to "A" to "D"
# """
# grade = ["A", "B", "A", "C", "A", "B"]
# grade.sort()
# print(grade)

# """
# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
# """
# names = ["Abhilash", "Ansh", "Nishi", "Ayaan", "Rishav", "Alok"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
#
#
# """
#  3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each mes
# sage should be the same, but each message should be personalized with the
# person’s name.
# """
# names = ["Abhilash", "Ansh", "Nishi", "Ayaan", "Ravish", "Alok"]
# for name in names:
#     print(f"Hello, {name}, congratulations for getting a new job in Google.")
#
#
#
# """
#  3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
# """
# vehicles = ["HondaCity", "BMW", "Jaguaar", "Ferari", "Fortuner", "Range Rover"]
# for vehicle in vehicles:
#     print(f"I would like to own a {vehicle}")
#
#
# # Set questions
#
# """
# Q. Write a python program to store the following word meaning in python dictionary.
# table: "piece of furniture, "list of facts and figure"
# cat: "a small animal"
# """
#
# dict = {
#     "table" : ["Piece of furniture", "list of facts and figure"],
#     "cat" : "a small animal"
# }
# print(dict)
#
# """
# Q. You are given a list of subjects for students. Assume one classroom is required for 1 subject.
# How many classrooms are required for all subjects.
# """
# subjects = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }
# print(len(subjects))
#
# """
# Q. Write a python program to enter marks of six subjects from the user and store them into a dictionary.
# Start with an empty dictionary and store one by one. Use subjects name as key and marks as a value.
# """
# marks = { }
# x = int(input("Enter a marks of Maths : "))
# marks.update({"Maths" : x})
#
# x = int(input("Enter a marks of Physics : "))
# marks.update({"Physics" : x})
#
# x = int(input("Enter a marks of Chemistry : "))
# marks.update({"Chemistry" : x})
#
# x = int(input("Enter a marks of English : "))
# marks.update({"English" : x})
#
# x = int(input("Enter a marks of Physical Education : "))
# marks.update({"Physical Education" : x})
#
# x = int(input("Enter a marks of Hindi : "))
# marks.update({"Hindi" : x})
#
# print(marks)
#
# """
# Q. Figure out a way to store 9 and 9.0 as separate values in a set.
# (You acn take help of an built-in data type.)
# """
# values = {
#     ("float" ,9.0),  # Considered as a set.
#     ("int", 9)
# }
# print(values)
#
# values = {
#     "float": 9.0,  # Considered as a dictionary.
#     "int": 9
# }
# print(values)

# Loops practice questions

"""
Q. Write a python program to print numbers from 1 to 100
"""
# i = 1
# while i <= 100:
#     print(i)
#     i +=1
# print("Thank you for your time.")
#
# """
# Q. Write a python program to print numbers from 100 to 1.
# """
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("Thank you.")
#
# """
# Q. Print the multiplication table of table n.
# """
# n = int(input("Enter a number : "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1
#
# """
# Q. Print the elements of the following list using a loop.
# """
# #traverse
# nums = [1, 4, 9, 16, 25, 50, 75, 100, 120, 150]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1
#
# """
# #  Q. Write a python program to find x in a number in the form of tuple.
# """
# nums = [1, 4, 9, 16, 25, 50, 75, 100, 120, 150]
# i = 0
# x = 75
# while i < len(nums):
#     if nums[i] == x:
#         print("Found at index ", i)
#         break
#     else:
#         print("Finding....")
#     i += 1
#
#
# """
# Q. Print the elements of the following list using a loop.
# """
#
# nums = [1, 4, 9, 16, 25, 50, 75, 100, 120, 150, 200]
# i = 0
# x = 100
# for num in nums:
#     # print(nums)
#     if num == x:
#         print("Found at index ", i)
#         break
#     else:
#         print("Still finding....")
#     i += 1
#
# """
# Q. Search for number x in this tuple using loop.
# """
# # THis is also called linear search
# nums = [1, 4, 9, 16, 25, 50, 75, 100, 120, 150, 200]
# i = 0
# x = 100
# for num in nums:
#     # print(nums)
#     if num == x:
#         print("Found at index ", i)
#         break
#     else:
#         print("Still finding....")
#     i += 1
#
# """
# Q. Print numbers between 1 to 100.
# """
# for i in range(1, 101):
#     print(i)
#
# """
# Print numbers between 100 and 1.
# """
# for num in range(100, 0, -1):
#     print(num)
#
# """
# Print the multiplication table of number n
# """
# n = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
#     i += 1

"""
Write a python program to print sum of natural numbers.
"""
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The total sum is : ", sum)

"""
Q. Write a python program to print factorial of n.
"""
n = 6
fact = 1
for i in range(1, n + 1):
    fact *= i
print("The factorial of ", n, "is : ", fact)

"""
Q. Write a python program to convert USD into INR
"""

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val)
converter(10000)

