from random import randint


def rolldice():
    first_dice = randint(1, 6)
    second_dice = randint(1, 6)
    print(f"{first_dice} and {second_dice}")