"""
List = A list is a value that contains multiple values in an ordered sequence.
- It can store elements of different types like (integer, string, float, etc.)
- Values inside lists are also called items.
- Lists are mutable in python where as you can change the value and assign a new value in it whenever you want.
- Where as, String is immutable in python in which you cannot change the value once it was created.
"""
# food = ["Pizza", "Burger", "Sandwich", "Momos","Chaat", "Chowmin"]
# #print(food[0])
# food[0] = "Golgappa"
# #print(food[0])
# #food.append("icecream")
# #food.remove("Momos")
# #food.pop()
# #food.insert(1, "Manchurian")
# #food.sort()
# food.clear()
#
# for x in food:
#     print(x)

# marks = [99.9, 98.7, 96.5, 92, 95, 97.89]
# print(marks)
# print(type(marks))
# print((len(marks)))

students = ["Abhilash", 22303316016, "BCA", 8.87, "Python Dveloper"]
print(students)
students[2] = "MCA"
print(students)

name = ["Bob", "Alisson", "Max", "Dorith", "Catherine", "Eve"]
popped = name.pop(0)
print(f"{popped =}")
print(f'{name =}')