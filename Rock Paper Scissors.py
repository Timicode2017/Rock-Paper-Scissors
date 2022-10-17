# Explanation about the game.
# it is a simple game that we used to play in childhood which is our beautiful memories and times...
# the game is simple rock wins scissors, scissors wins paper, and paper wins rock,
# if both participants choose the same ability it's a draw and the point didn't count.
# so you play once again for the victory.

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)  # rock: 0, paper: 1 , scissors: 2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("You both chose rock, it's a draw!")

    elif user_input == "paper" and computer_pick == "paper":
        print("You both chose paper, it's a draw!")

    elif user_input == "scissors" and computer_pick == "scissors":
        print("You both chose scissors, it's a draw!")

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times")
print("The computer", computer_wins, "times")
print("Good Bye!")
