import random

userWins = 0
computerWins = 0
option = ["rock", "paper", "scissor"]

while True:
    userInput = input("Typer Rock/Paper/Scissor or Q to Quit: ").lower()
    if userInput == "q":
        break
    if userInput not in option:
        print("Input the right command")
        continue
    randomNumber = random.randint(0, 2)
    # rock = 0, paper = 1, scissor = 2
    computerPick = option[randomNumber]
    print("Computer picked", computerPick)
    
    if userInput == "rock" and computerPick == "scissor":
        print("You Won")
        userWins += 1
        continue
    
    elif userInput == "paper" and computerPick == "rock":
        print("You Won")
        userWins += 1
        continue
    
    elif userInput == "scissor" and computerPick == "paper":
        print("You Won")
        userWins += 1
        continue
    else:
        print("You lost")
        computerWins += 1

print("You won", userWins, "times")
print("The Computer won", computerWins, "times") 
print("Goodbye!")