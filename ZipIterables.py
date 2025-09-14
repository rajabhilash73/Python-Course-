"""
zip(*iterables) = aggregates iterables from two or more iterables (lists, tuples, sets etc.)
creates a zip objects with paired elements stored in tuples for each element within our zip objects.
"""
username = ["Abhilash", "Nishi", "Rony", "Rita"]
passwords = ["pa$swords", "abc123@", "1765at", "Tiger456"]


users = list(zip(username, passwords))
print(type(users))
for i in users:
    print(i)

print("-----------------------------------------------")

users = dict(zip(username, passwords))
for key, value in users.items():
    print(key + " : " + value)

print("-----------------------------------------------")

username = ["Abhilash", "Nishi", "Rony", "Rita"]
passwords = ["pa$swords", "abc123@", "1765at", "Tiger456"]
login_dates = ["1/01/2025", "11/02/25", "14/042025", "20/05/2025"]

users = zip(username, passwords, login_dates)
for i in users:
    print(i)



