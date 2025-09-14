"""
Lambda function = Function written in one line using lamda keyword accepts any amount of argument,
but only has one operator.
Lambda parameters : expression
"""
# def double(x):
#     return x * 2
# print(double(6))

multiply = lambda x, y: x * y

double = lambda x: x * 2

add = lambda x, y, z: x + y + z

divide = lambda x, y: x / y

full_name = lambda first_name, last_name: first_name + " " + last_name

age_check = lambda age: True if age >= 18 else False

print(multiply(12, 8))

print(double(6))

print(add(200, 100, 150))

print(divide(80, 2))

print(full_name("Abhilash", "Raj"))

print(age_check(20))