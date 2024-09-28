name = input("Type your name: ")
print("Welcome", name, "to this advanture")

answer = input("Your are on a dirt road, which way you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river, Type walk to walk or swimp to swimp ")
    if answer == "walk":
        print("You run for mile and run out of water")
    elif answer == "swimp":
        print("Your swamp and were earen by fish")
    else:
        print("Not a valid answer")
elif answer == "right":
    answer = input("You come to bridge, (cross/back? )")
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross and meet strangger, wanna talk to him?(yes/no) ")
        if answer == "yes":
            print("You get a gold and win")
        elif answer == "no":
            print("You ignore the stranger")
        else:
            print("Not a valid answer, You lose")
else:
    print("Not a valid answer. Choose Right / Left")
    
print("Thanks for trying")