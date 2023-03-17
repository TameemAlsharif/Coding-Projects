# Just a small mini game to get my coding skills up to speed
print("Welcome to the computer quiz! ")

userPlaying = input("Do you want to play? (Type 'yes' or 'no') ")

if userPlaying.lower() != "yes":
    print("Alright see you later! ")
    quit()

print("Okay! Let's play: ")

score = 0

answer = input("What does the UK stand for? ")
if answer.lower() == "united kingdom":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does KSA stand for? ")
if answer.lower() == "kingdom of saudi arabia":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does UAE stand for? ")
if answer.lower() == "united arab emirates":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score}/3")
print(f"You got {(score/3) *100}/3")

    
