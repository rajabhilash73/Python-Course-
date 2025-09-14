"""
List Slicing = Basically lists slicing is happening when two integers where present hey both separate with semicolon(:).
"""
animals = ["cat", "bat", "tiger", "lion", "elephant", "leopard" ]
print(animals)
print(animals[0:5])
print(animals[1:5])
print(animals[:6])
print(animals[0:])
print(animals[0:-2])
print(animals[-4:-1])

# Checking len of a list.
print(len(animals))

# Changing values in a list with indexes.
animals = ["cat", "bat", "tiger", "lion", "elephant", "leopard" ]
animals[1] = "Dinosaur"
print(animals)

# List concatenation & List replication
animals = ["cat", "bat", "tiger", "lion", "elephant", "leopard" ]
birds = ["Piegion", "Parror", "Eagle", "Seagal", "Sparrow", "Vulture"]
Zoo = [animals + birds] # List concatenation
Zoo = [animals + birds] * 3 # List replication
print(Zoo)

# delete value from the list
animals = ["cat", "bat", "tiger", "lion", "elephant", "leopard" ]
del(animals[2])
print(animals)

# Working with a list.



