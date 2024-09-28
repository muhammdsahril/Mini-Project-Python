print("Welcome to my Game Quiz!")

playing = input(f"Do you want to play? ").lower()

if "yes" in playing.lower():
    print("Okay, Lets playing : )")
else:
    print("Okay, see you soon")
    quit()


answer = input("What does CPU stand for? ")
if "central processing unit" in answer.lower():
    print("correct")
    
else:
    print("its a central processing unit")