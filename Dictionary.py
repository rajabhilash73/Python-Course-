"""
Dictionary = A mutable which is considered as a changeable unordered collection of unique key : values pairs.
- Fast because they are hashing, and allow us to access the value quickly.
- They don't allow duplicate keys.
- Dictionary is mutable because we can change its values whenever we want.
- They are unordered.
"""

Capitals = {"India": "New Delhi",
            "USA": "Washington DC",
            "Russia": "Moscow",
            "Japan": "Tokyo",
            "Australia": "Sydney",
            "England": "London"}

# print(Capitals["India"])
# print(Capitals.get("Germany")) #.get() - function used to identify whether the value in the dictionary is available or not.
#print(Capitals.values()) # This functions returns the value in the dictionary.
#print(Capitals.keys()) - This function returns values in dictionary
#print(Capitals.items()) - Returns all key values as tuples.
# print(Capitals.update({"Germany": "Berlin"}))
# print(Capitals.update({"USA": "Massachusetts"}))
# print(Capitals.pop("China"))
# print(Capitals.clear())


# for key, value in Capitals.items():
#     print(key, value)
#
# info = {
#     "Name" : "Abhilash Raj",
#     "Age" : 23,
#     "Qualification": "Graduate",
#     "CGPA" : 8.8,
#     "Job" : "Python Developer",
#     "Programming" : ["Python", "JavaScript"],
#     "Database": ["MySql", "PostgreSQL"],
#     "Tools" : "Github",
#     "Department": "Computer Science",
#     "Country": "India",
#     "is_available_to_join" : "Yes",
#     "Company" : "Google",
#     "Package" : "75LPA",
#     "Work_in_country" : "United States",
#     "is_adult" : True
#
# }
# print(info)
# print(info["Name"])
# info["Job"] = "Backend Developer"
# print(info)
#
# # Nested dictionary
#
# student_info = {
#     "Name" : "Abhilash Raj",
#     "id" : 88,
#     "Age" : 23,
#     "Qualification": "Graduate",
#     "subjects" : {
#         "Python" : 95,
#         "C" : 88,
#         "JavaScript" : 96,
#         "HTML" : 99,
#         "Data Structure with Python" : 85,
#         "Discrete Mathematics" : 100
#     },
#     "CGPA" : 8.8
# }
# print(student_info)
# print(student_info["subjects"])
# print(student_info["subjects"]["Python"])
#
# # Dict methods
# #.keys()
# print(info.keys())
#
# # Type casting
# print(tuple(info.keys()))
# print(list(info.keys()))
#
# # To find the total number of key value pairs.
# print(len(info))
#
# print(info.keys())
# print(student_info.values())
# print(student_info.items())
# print(list(student_info.items()))
#
# # If we want to access the keys and value pairs individually.
# pairs = list(student_info.items())
# print(pairs[0])
#
# print(student_info.get("subjects"))  # .get() methods returns value of the key.
# print(student_info["subjects"])  # They both provide the same answers.
#
# # .update()
# print(student_info.update({"City" : "Patna"}))
# print(student_info)
# new_dict = {"City": "Patna"}
# student_info.update(new_dict)
# print(student_info)
#
# #  Write a python program in dictionary to print birthdays of users followed by their name.
#
# Birthdays = {"Abhilash" : "24th May", "Nishi" : "4th Feb", "Ansh": "2nd Aug", "Dhoni" : "7th July", "Riya" : "14th Jan", "Bob" : "8th Sept"}
#
# while True:
#     print("Enter a name : ")
#     name = input()
#     if name == " ":
#         break
#     if name in Birthdays:
#         print(Birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print("I don't have birthday information for " + name)
#         print("Ok tell me. What is their birthday : ")
#         birthday = input()
#         Birthdays[name] = birthday
#         print("Their birthday is updated in our database.")
#         print("Thank you....")


# The keys(), values(), and items() methods.
# .values()
# -- Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values or key-value pairs
# -  in a dictionary respectively.
Birthdays = {"Abhilash" : "24th May", "Nishi" : "4th Feb", "Ansh": "2nd Aug", "Dhoni" : "7th July", "Riya" : "14th Jan", "Bob" : "8th Sept"}
for date in Birthdays.values():
    print(date)

# .keys()
for  k in Birthdays.keys():
    print(k)

# .items()
for i in Birthdays.items():
    print
Birthdays = {"Abhilash" : "24th May", "Nishi" : "4th Feb", "Ansh": "2nd Aug", "Dhoni" : "7th July", "Riya" : "14th Jan", "Bob" : "8th Sept"}
for v in Birthdays.values():
    print(v)

for k in Birthdays.keys():
    print(k)

for i in Birthdays.items():
    print(i)

Birthdays = {"Abhilash" : "24th May", "Nishi" : "4th Feb", "Ansh": "2nd Aug", "Dhoni" : "7th July", "Riya" : "14th Jan", "Bob" : "8th Sept"}
for k, v in Birthdays.items():
    print("Key :" + k + " Value :" + str(v))  # str(v) is used to convert the value to a string; though here it's already a string.

# Checking wheather a key or value exists in a dictionary
# For key
Birthdays = {"Abhilash" : "24th May", "Nishi" : "4th Feb", "Ansh": "2nd Aug", "Dhoni" : "7th July", "Riya" : "14th Jan", "Bob" : "8th Sept"}
if 'Abhilash' in Birthdays:
    print("Yes Abhilash is exists.")
else:
    print("Abhilash is not exists.")

# for value
Birthdays = {"Abhilash" : "24th May", "Nishi" : "4th Feb", "Ansh" : "2nd Aug", "Dhoni" : "7th July", "Riya" : "14th Jan", "Bob" : "8th Sept"}
print("Abhilash" in Birthdays.keys())
print("4th Feb" in Birthdays.values())

# Checking if both key and values exist.
print(("Abhilash", "24th May") in Birthdays.items())

#.get()
Items = {"Maggie" : 5, "Coffee" : 6}
print("I am bringing " + str(Items.get("Maggie", 5)) + ' ' + 'Maggies to you.')