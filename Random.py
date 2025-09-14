import random

x = random.randint(1, 10)  # For positive value
y = random.random() # This ones for floating value

my_list = ["Rock", "Paper", "Scissors"]
z = random.choice(my_list)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A"]
random.shuffle(cards)
print(cards)