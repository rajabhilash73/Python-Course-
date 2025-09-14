"""
Set = Set is a collection that is unordered, uniindexed and no duplicates value stores in it.
- Set is mutable, but set's elements are immutable
"""
Utensils = {"Fork", "Spoon","Knife", "Glass", "Jug", "Plate"}
Dishes = {"Bowl", "Cup", "Mug", "Karahi", "Topiya", "Karchi"}
# Utensils.add("Napkiene")
#Utensils.remove("Spoon")
# Utensils.clear()
# Utensils.update(Dishes)
# Dinner_Table = Utensils.union(Dishes) # Combine both sets and returns new one
# print(Utensils.difference(Dishes))
Utensils.intersection(Dishes)

for x in Utensils:
    print(x)

collection = set()
print(type(collection))