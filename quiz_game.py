options = ["Y","N"]

play = None 

while play not in options:

    play = str(input("Do you wanna play?(Y/N) ").upper())

if play == "Y":
    print("You gonna play a quiz game...")
else:
    print("Bye"*2)
    quit()

def game():

    print("Let's get started...")
    score = 0
    count = 0
    
    one = str(input("What is python? >")).lower()
    count += 1
    if one == "programming language":
        print("Correct!")
        score+=1
    else:
        print("False!")
    
    two = str(input("What is CS? >")).lower()
    count += 1
    if two == "computer science":
        print("Correct!")
        score+=1
    else:
        print("False!")
    three = str(input("What is HTML? >")).lower()
    count += 1
    if three == "hyper text markup language":
        print("Correct!")
        score+=1
    else:
        print("False!")
    four = str(input("What is CSS? >")).lower()
    count += 1
    if four == "cascading style sheet":
        print("Correct!")
        score+=1
    else:
        print("False!")
    five = str(input("What is your name >")).lower()
    count += 1
    if five == "nyan min myat":
        print(f"Hello {five}")
        score+=1
    else:
        print("False!")
    six = str(input("Who is mthc? >")).lower()
    count += 1
    if six == "devil in disguise":
        print("Correct!")
        score+=1
    else:
        print("False!")
    seven = str(input("What is love? >")).lower()
    count += 1
    if seven == "money":
        print("Correct!")
        score+=1
    else:
        print("False!")
    eight = str(input("What is your dream? >")).lower()
    count += 1
    if eight == "billionarie":
        print("Correct!")
        score+=1
    else:
        print("False!")
    nine = str(input("Who do you love? >")).lower()
    count += 1
    if nine == "mthc":
        print("Correct!")
        score+=1
    else:
        print("False!")
    ten = str(input("Why? >")).lower()
    count += 1
    if ten == "coz i'm stupid af":
        print("Correct!")
        score+=1
    else:
        print("False!")
    eleven = str(input("keep moving forward? >")).lower()
    count += 1
    if eleven == "wish i could":
        print("Correct!")
        score+=1
    else:
        print("False!")
    twelve = str(input("Wanna die? >")).lower()
    count += 1
    if twelve == "yes":
        print("Correct!")
        score+=1
    else:
        print("False!")
    thirteen = str(input("Will you grind? >")).lower()
    count += 1
    if thirteen == "yes":
        print("Correct!")
        score+=1
    else:
        print("False!")
    twelve = str(input("Will you grid till death to get her? >")).lower()
    count += 1
    if twelve == "yes":
        print("Correct!")
        score+=1
    else:
        print("False!")

    print(f"You got {score} questions out of total.")
    print(f"Your score is {(score/count)*100} %.")

game()
quit()