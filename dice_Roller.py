from random import randint

""""This is a very simple piece of code to roll a number of dice of a certain size that could be used for games such as Monopoly, Yahtzee  ect"""

#Dice pool
d4 = 4
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d20 = 20
d100 = 100


def multiroll(num: int, dice: int):

    count = 0
    result = []

    while count < num:
        roll = randint(1,dice)
        result.append(roll)
        count +=1

    return result

print(multiroll(3,d4))
