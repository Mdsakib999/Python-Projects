#Make a Dice Roll program using python...

import random

def rolling_dice():
    roll = input("Roll the dice? (Y/N): ")

    while roll.lower() == "Y".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))

        roll = input("Roll again? (Y/N): ")
        print("Game finished")



rolling_dice()