"""
Sort() methods = used with list
Sort() function = used with iterables
"""

# Students = ["Rohan", "Rahul", "Manpreet", "Roshni", "Tanisha", "Raman"]
# # Students.sort(reverse = True)
# sorted_students = sorted(Students, reverse=True)
# for i in sorted_students:
#     print(i)

Students = (("Shan", "A", 24),
            ("Sohan", "A", 26),
            ("Sameer", "A", 28),
            ("Abhay", "A", 30),
            ("Aman", "A", 29),
            ("Akay", "A", 32))
Age = lambda ages: ages[2]
Grade = lambda grades: grades[1]
# Students.sort(key = Grade)
# Students.sort(key = Age)
Sorted_students = sorted(Students, key = Age)
for i in Sorted_students:
    print(i)