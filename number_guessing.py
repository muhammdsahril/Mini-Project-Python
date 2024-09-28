import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number larger than 0")
    quit()
    
random_number = random.randint(0, top_of_range)
gueses = 0


while True:
    gueses += 1
    user_guesss = input("Make a guess: ")
    if user_guesss.isdigit():
        user_guesss = int(user_guesss)
    else:
        print("Please type a number larger than 0")
        continue
    if user_guesss == random_number:
        print("You got it!")
        break
    elif user_guesss > random_number:
        print("Your above the number")
    else:
        print("Your below the number")
        
print("You got it in", gueses, "gueses")
