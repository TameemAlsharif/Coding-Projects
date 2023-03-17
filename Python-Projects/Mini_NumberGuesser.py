# Mini Number guesser inspiration from Tech with Tim
import random

top_range = input("Type a number: ")
guesses = 0

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time. ")
    quit()


random_number = random.randint(0, 11)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
        print("Pleasee type a number next time. ")
        continue

    if user_guess == random_number:
        print("You Got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses")