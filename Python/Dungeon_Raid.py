#File Imports
from asyncio.windows_events import NULL
import linecache
from random import randint
import time

#Global Variables
agelimit = 18
playerList = ["Valid Players: "]
playerAmount = 0
lvlExp = 50


#Player 1
firstname = input("Please enter your forename: ")
age =  int(input("What is your age: "))

if age < agelimit:
    print("You're not old enough to enter")
else:
    print("You may enter!")
    playerList.append(firstname)
    playerAmount = playerAmount + 1
    proceed = input("Are you ready to play? Yes/No\n")

#Player 2
if proceed == "Yes":
    print("The Game Will Now Begin")
elif proceed == "No":
    firstname2 = input("Please enter your forename: ")
    age = int(input("What is your age: "))

if age < agelimit and proceed == "No":
    print("You're not old enough to enter")
else:
    print("You may enter!")
    playerList.append(firstname2)
    playerAmount = playerAmount + 1
    proceed = input("Are you ready to play? Yes/No\n")

#Player 3
if proceed == "Yes":
    print("The Game Will Now Begin")
elif proceed == "No":
    firstname3 = input("Please enter your forename: ")
    age =  int(input("What is your age: "))

if age < agelimit and proceed == "No":
    print("You're not old enough to enter")
else:
    print("You may enter!")
    playerList.append(firstname3)
    playerAmount = playerAmount + 1
    proceed = input("Are you ready to play? Yes/No\n")

#Player 4
if proceed == "Yes":
    print("The Game Will Now Begin")
elif proceed == "No":
    firstname4 = input("Please enter your forename: ")
    age =  int(input("What is your age: "))

if age < agelimit and proceed == "No":
    print("You're not old enough to enter")
else:
    print("You may enter!")
    playerList.append(firstname4)
    playerAmount = playerAmount + 1

if playerAmount == 4:
    print("You have reached the maximum players")

#Assigning player characters    
player_1 = [firstname, 150, 1, 0]
player1_name, player1_healths, player1_level, player1_exp = player_1
print(player_1)

player_2 = [firstname2, 150, 1, 0]
player2_name, player2_healths, player2_level, player2_exp = player_2
print(player_2)

player_3 = [firstname3, 150, 1, 0]
player3_name, player3_healths, player3_level, player3_exp = player_3
print(player_3)

player_4 = [firstname4, 150, 1, 0]
player4_name, player4_healths, player4_level, player4_exp = player_4
print(player_4)

playersExp = [player1_exp, player2_exp, player3_exp, player4_exp]

#Player Leveling
def levelup(exp, nextExp,level, health):
    baseHealth1 = 150
    while exp >= nextExp:
            level += 1
            player1_level = level
            exp -= nextExp
            player1_exp = exp
            nextExp = (round(nextExp * 1.25))
            health = (round(baseHealth1 * 1.25))
            player1_healths = health
            return f"Congratulations {player1_name} you have leveled up to {player1_level}!!!!\nYour current exp is now {player1_exp}/{nextExp}\nYour health has been increase {player1_healths}"

    if health > baseHealth1:
        baseHealth1 = health
            

if proceed == "Yes":
    print("Welcome", playerList[1:], "you have now entered the dungeon!")

#Player Healing
def healing1(health_1):
    healthLimit = 50
    if health_1 <= healthLimit:
        heal = input(f"{player1_name} You're low on health, do you want to heal? Y/N\n")
        if heal == "Y":
            health_1 += randint(50, 100)
            player1_healths = health_1
            return f"Health: {player1_healths}"
        elif heal == "N":
            return "Pray for your survival!"

#First Encounter 1/4
mobcount = randint(1, 4)
base_mobhealth = 100
print(f"Danger has approached, {mobcount} trolls stand before you\nOne of you must eliminate them,\nWill it be {player1_name} or {player2_name} or {player3_name} or {player4_name}?")
decision = input("Choose: ")
if decision == player1_name:
    mobhealth = base_mobhealth
    while mobcount > 0:
        mobhealth -= randint(20, 50)
        print(f"troll#{mobcount}:", mobhealth)
        if mobhealth <= 0:
            mobhealth = base_mobhealth
            mobcount -= 1
            print(f"There are {mobcount} left")
        if mobcount == 0:
            break
        time.sleep(0.5)
        player1_healths -= randint(5, 10)
        print(f"{player1_name}:", player1_healths)
        print(healing1(player1_healths))
        time.sleep(1)

        
    

#Boss Fight
monster = ["Gargon", 1000]
monster_name, monster_health = monster

progress = input("Initiate Boss Fight? Yes/No\n")

if progress == "Yes":
    while monster_health > 0:
        print(monster_name + ":" ,monster_health)
        monster_health -= randint(50, 75)
        time.sleep(1.5)
        if monster_health <= 800 and monster_health >= 745:
            player1_healths -= randint(1, 25)
            print(player1_name ,player1_healths)
            print(healing1(player1_healths))
        elif monster_health < 745 and monster_health >= 730:
            print(f"{player1_name} dodged the attack!")
        
        if monster_health == monster_health <= 600 and monster_health >= 530:
            player2_healths -= randint(1, 25)
            print(player2_name ,player2_healths)
        elif monster_health < 545 and monster_health >= 530:
            print(f"{player2_name} dodged the attack!")
        
        if monster_health == monster_health <= 400 and monster_health >= 330:
            player3_healths -= randint(1, 25)
            print(player3_name ,player3_healths)
        elif monster_health < 345 and monster_health >= 340:
            print(f"{player3_name} dodged the attack!")
        
        if monster_health == monster_health <= 200 and monster_health >= 130:
            player4_healths -= randint(1, 25)
            print(player4_name ,player4_healths)
        elif monster_health < 145 and monster_health >= 140:
            print(f"{player4_name} dodged the attack!")
else:
    print("The Boss won't wait forever")


if monster_health <= 0:
    print(f"Congrats! {player1_name} {player2_name} {player3_name} {player4_name} You defeated the boss\nHere are your rewards!")
    player1_exp += randint(50, 75)
    player2_exp += randint(50, 75)
    player3_exp += randint(50, 75)
    player4_exp += randint(50, 75)
    print(f"{player1_name},{player1_level}: {player1_exp}\n{player2_name},{player2_level}: {player2_exp}\n{player3_name},{player3_level}: {player3_exp}\n{player4_name},{player4_level}: {player4_exp}")
    time.sleep(1)
    print(levelup(player1_exp, lvlExp, player1_level, player1_healths))
