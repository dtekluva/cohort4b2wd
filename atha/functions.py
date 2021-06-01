import random


def guess():

    computer_pick = random.randint(1,4)
    user_pick = int(input("Please enter your guess : "))

    if user_pick == computer_pick:
        print("YEAAAYY")
    else:
        print("BOOOOO...!!!")

for i in range(5):
    guess()