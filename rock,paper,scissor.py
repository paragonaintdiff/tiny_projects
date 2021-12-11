import random

choices = ["rock","paper","scissors"]

you_win = 0
computer_win = 0
tie = 0

while True:

    you_pick = input("Rock, paper, scissors or Q to quit >>> ").lower()

    if you_pick == "q":
        print("You Quited.")
        break

    if you_pick not in choices:
        continue
    
    random_no = random.randint(0,2)
    computer_pick = choices[random_no]

    if you_pick == "rock" and computer_pick == "scissors":
        print(f"You {you_pick} and computer {computer_pick}")
        print("You win.")
        you_win += 1
    elif you_pick == "paper" and computer_pick == "rock":
        print(f"You {you_pick} and computer {computer_pick}")
        print("You win.")
        you_win += 1
    elif you_pick == "scissors" and computer_pick == "paper":
        print(f"You {you_pick} and computer {computer_pick}")
        print("You win.")
        you_win += 1
    elif you_pick == computer_pick:
        print(f"You {you_pick} and computer {computer_pick}")
        print("Draw?")
        tie += 1
    else:
        print(f"You picked {you_pick} but computer was {computer_pick}")
        print("You lost!")
        computer_win += 1

print(f"You won {you_win} times and computer won {computer_win} times.")
print(f"You both tied {tie} times.")
print("Bye! See You Next Time.....")



