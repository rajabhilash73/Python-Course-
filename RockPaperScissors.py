"""
Rock Paper Scissors Game
"""
import random
while True:

    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("Rock, Paper, Scissors : ? ")
 
    if player == computer:   
       print("Computer : ", computer)
       print("Player : ", player)
       print("It's a tie game!")
    elif player == "Rock":
        if computer == "Paper":
           print("Computer : ", computer)
           print("Player : ", player)
           print("You Loose!")
        if computer == "Scissors":
           print("Computer : ", computer)
           print("Player : ", player)
           print("You Win the game!")
    elif player == "Paper":
        if computer == "Scissors":
           print("Computer : ", computer)
           print("Player : ", player)
           print("You Loose!")
        if computer == "Rock":
           print("Computer : ", computer)
           print("Player : ", player)
           print("You Win the game!")
           
    play_again = input("Play again? (Yes/No) : ") 
    if play_again != "Yes":
        break   
    
print("Bye!")     
    