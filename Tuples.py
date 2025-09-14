"""
Tuples = The collection which is ordered and unchangeable which is used to group together related data.
- Tuple is immutable which is it cannot change the value once it is created.
- A Tuple object doesn't support item assignment, which means we cannot assign a new value when tuple is created.
"""
Student = ("Bro", 19, "Male")
print(Student.count("Bro"))
print(Student.index("Male"))


for x in Student:
    print(x)
    
if "Bro" in Student:
    print("Bro is here")    