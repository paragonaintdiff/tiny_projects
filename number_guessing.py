import random

def guess_number():

    max_of_range = input("Input max number of range >> ")

    if max_of_range.isdigit():
        max_of_range = int(max_of_range)

        if max_of_range <= 0:
            print("Pls input a number > 0 next time.")
            quit()

    else:
        print("Pls input number next time.")
        quit()

    rand_no = random.randint(0, max_of_range)
    guesses = 0

    while True:

        guesses += 1
        user_guess = input("Your guess?(>0) > ")

        if user_guess.isdigit():
            user_guess = int(user_guess)

            if user_guess <= 0:
                print("Pls only guess a number > 0.")
                quit()
        else:
            print("Input only number pls.")
            quit()
    
        if user_guess == rand_no:
            print(f"Congrats!!! you gussed it right in {guesses} guesses.")
            break
        else:
            if user_guess > rand_no:
                print("You were above the correct guess.")
            else:
                print("You were below the correct guess.")

def play_again():
    
    response = input("Play again? (yes/no) : ").upper()
    if response == "YES":
        return True
    else:
        return False

guess_number()

while play_again():

    guess_number()

 

