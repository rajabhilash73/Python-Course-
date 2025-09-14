"""
List Comprehension = A way to create a new list with less syntax.
List comprehension is easier to read than lambda function.
"""
Squares = []
for i in range(1, 11):
    Squares.append(i * i)
    print(Squares)

Squares = [i * i for i in range(1, 11)]   # Use list comprehension here
print(Squares)

Students = [100, 90, 80, 70, 60, 50, 40, 30, 50, 20, 10, 25]
passed_students = list(filter(lambda x: x >= 30, Students))   # lambda function
print(passed_students)

passed_students =[i for i in Students if i >= 30]   # list comprehension
passed_students = [i if i >= 30 else "Failed" for i in Students]
print(passed_students)


