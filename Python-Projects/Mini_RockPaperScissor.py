# Mini Rock Paper Scissor game to get back up to speed inspiration from Tech with Tim
import random 

user_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissors"]
#Index No:   0       1          2

while True:
    user_input = input("Type Rock/Paper/Scissiors or 'q' to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    # Rock: 0, Paper: 1, Scissors: 2    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost!")
        computer_wins +=  1
    
print(f"You won {user_wins} times and the computer won {computer_wins}")
print("Goodbye!")

