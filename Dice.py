import random

class Dice:
    def roll(self):
        dice_values = [1, 2, 3, 4, 5, 6]
        name = random.choice(dice_values)
        last = random.choice(dice_values)
        return name, last



dice = Dice()
print(dice.roll())






