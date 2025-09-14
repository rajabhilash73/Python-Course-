"""
Nested Loop = The "Inner loop" will finish all it's iterations before finishing one iterations  of the "Outer Loop."
"""

Rows = int(input("How many rows? : "))
Columns = int(input("How many columns? : "))
Symbols = input("Write a symbol you use : ")

for i in range(Rows):
    for j in range(Columns):
        print(Symbols, end= " ")
        
    print()    