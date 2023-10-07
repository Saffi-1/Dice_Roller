import random

def roll_dice():
    num_dice = int(input("How many dice do you want to roll? "))
    print("Rolling the dice...")
    print("The result is:")

    for _ in range(num_dice):
        roll_result = random.randint(1, 6)
        print(roll_result)

    play_again = input("Do you want to roll the dice again? (yes/no) ")
    if play_again.lower() == "yes":
        roll_dice()
    else:
        print("Thank you for using the Dice Roller app. Goodbye!")

roll_dice()