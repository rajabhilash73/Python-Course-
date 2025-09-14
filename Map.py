"""
map() = applies a function to each item in an iterable (list, tuples, etc.)
"""
Store = [("Shirt", 20.00),
         ("Jeans", 35.00),
         ("Jacket", 50.00),
         ("Shoes", 65.00),
         ("Shocks", 10.00),
         ("Tshirt", 25.00)]

to_Rupees = lambda data: (data[0], data[1] * 85.36)
to_Dollars = lambda data: (data[0], data[1] / 85.36)
store_rupees = list(map(to_Rupees, Store))
store_Dollars = list(map(to_Dollars, Store))

for i in store_rupees:
    print(i)

for i in store_Dollars:
    print(i)