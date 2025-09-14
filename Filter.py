"""
filter() = Creates a collection of elements from iterable for which a function returns true.
filter(function, iterables)
"""
Friends = [("Rahul", 24),
           ("Aditya", 25),
           ("Rohan", 25),
           ("Piyush", 16),
           ("Ankit", 15),
           ("Aneesh", 28),
           ("Tanisha", 25),
           ("Anjali", 26)]
age = lambda data: data[1] >= 18
drinking_buddies = filter(age, Friends)
for i in drinking_buddies:
    print(i)