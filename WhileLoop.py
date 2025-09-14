"""
While Loop = A statements that will execute it's block of code, as long as it's condition remains true.
"""

# name = ""
# while len(name) == 0:
#     name = input("Enter your name : ")
#
# print("Hello " + name)
# (print(len(name)))
#
# count = 1  # Iterators
# while count <= 5:  # Iterations
#     print("Hello Abhilash!")
#     count += 1
#     print(count)
#
# name = ""
# while name != 'your name' :
#     print("Please type your name. ")
#     name = input("Enter your name : ")
# print("Thank you. ")

"""
Print numbers 1 to 5
"""
i = 1
while i <= 5:
    print(i)
    i += 1
print("Loop ended")

run = True
current = 1
while run:
    if current == 101:
        run = False
    else:
        print(current)
        current += 1

count = 1
while count <= 5:
    print("Hello Abhilash")
    count += 1
print(count)

# break
i = 1
while i <= 5:
    print(i)
    if i == 4:
        break
    i += 1

print("End of the loop")

# Continue
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
"""
Print odd numbers.
"""
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

"""
Print even numbers
"""
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
