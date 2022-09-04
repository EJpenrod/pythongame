# File Name: Battlegame.py
# Created by: Ezekiel Penrod - Battle game is a game where you fight a dragon.
import monsters
from Ascii import SlimePic, UserMenuText, skeleart, banditart, monster_menu
from random import *
from Hero import *
from Slime import slime_
from text import Adventure_Text
import time
import copy
import crafting

# this is my monster bag

slimes = []
dragons = []
skeleton = []
werewolf = []
bandit = []
ogre = []
wyvern = []
chimera = []
minotaur = []
character = createClass()
monster_order = [(slimes), (skeleton), (bandit),
                 (wyvern), (werewolf), (dragons)]

# this is where i put monsters in the bag :D

for guyimfighting in range(randint(2, 3)):
    slimes.append(monster_class(40, 2, 1, 1, 1, 1, 1, 0,
                  random.randint(1, 5), random.randint(1, 5)))
for guyimfighting in range(randint(1, 1)):
    dragons.append(monster_class(200, 100, 10, 10, 10, 10, 10, 1,
                   random.randint(200, 1000), random.randint(200, 1000)))
for guyimfighting in range(randint(1, 3)):
    skeleton.append(monster_class(20, 3, 1, 1, 1, 1, 1, 2,
                    random.randint(10, 30), random.randint(1, 5)))
for guyimfighting in range(randint(1, 2)):
    werewolf.append(monster_class(125, 10, 1, 1, 1, 1, 1, 3,
                    random.randint(25, 100), random.randint(1, 5)))
for guyimfighting in range(randint(1, 3)):
    wyvern.append(monster_class(50, 25, 1, 1, 1, 1, 1, 4,
                  random.randint(25, 100), random.randint(1, 5)))
for guyimfighting in range(randint(1, 3)):
    bandit.append(monster_class(30, 10, 8, 5, 6, 4, 5, 5,
                  random.randint(10, 20), random.randint(10, 20)))
for guyimfighting in range(randint(1, 2)):
    ogre.append(monster_class(80, 20, 4, 2, 3, 4, 6, 6,
                random.randint(20, 50), random.randint(20, 30)))
for guyimfighting in range(randint(1, 2)):
    chimera.append(monster_class(140, 20, 10, 10, 10, 10, 4, 7,
                   random.randint(30, 100), random.randint(30, 100)))
for guyimfighting in range(randint(1, 2)):
    minotaur.append(monster_class(120, 10, 5, 5, 5, 4, 4, 8,
                    random.randint(20, 90), random.randint(30, 200)))


def mining(character):
    choice = input("would you like to:\n1.)Go mining\n2.)return to town")
    if character.bag == {"pickaxe"}:
        if choice == "1":
            print("You swing your pickaxe at a strange looking rock")
            hit = random.randint(1, 100)
            if hit <= 20:
                print("You've mined 1 ore")
                character.bag.update({"ore"})
                modify_key = "ore"
                character.bag[modify_key] = character.bag(
                    modify_key, 0) + 1
                pickaxe(character)
                print(character.bag({"ore"}))
            elif hit <= 2:
                print("you've found a gold nugget")
                character.bag.update({"gold nugget"})
                modify_key = "gold nugget"
                character.bag[modify_key] = character.bag(
                    modify_key, 0) + 1
                print(character.bag({"gold nugget"}))
            else:
                while choice != "1" and choice != "2":
                    print("Please choose 1 or 2")
                choice = input(
                    "It appears you didnt find anything this time.\n would you like to:\n1:Continue mining?\n2:Return to town")
                if choice == "1":
                    mining()
                if choice == "2":
                    return
    if choice == "2":
        print("You decide to try again some other time")
        return


def menuing():

    ExitMenu = False
    while ExitMenu == False:
        UserMenuText()
        selection = input(
            "What would you like to do: ?\n1.)Go to town\n2.)Adventure\n3.)Go mining ")
        while selection != "1" and selection != "2" and selection != "3":
            print("Please choose 1, 2, or 3")
            selection = input(
                "What would you like to do: ?\n1.)Go to town\n2.)Adventure onward!!\n ")
        if selection == "1":
            print(
                "You have arrived in a shoddy looking town, not much here except a tavern and a few locals")
            time.sleep(0.0)
            print("As the tavern doors squeak open, you see an overweight man behind the counter, a few customers.")
            print("and what appears to be a man in the corner with his pet pig")
            time.sleep(0.5)
            print(
                "'Oh look another adventurer' said the barkeep, 'or as i like to call em walking coin bags....")
            print("With a hearty laugh he looks at you expectantly")
            time.sleep(0.5)
            print("As you just look at the bar keeper he says:")
            print("Well don't go standing there go ahead and get some food and rest, he throws you the key its marked #2.")
            time.sleep(0.5)
            print("You go into the room marked #2, the bed is a grade above a bed of straw, but sleep calls, you answer.")
            print("~~~Resting~~~")
            time.sleep(0.5)
            character.Health = character.maxHealth
            print(
                f"You have rested, restoring your health back to:{character.maxHealth}")

        elif selection == "2":
            Adventure_Text
            ExitMenu = True
        elif selection == "3":
            mining(character)
            ExitMenu = True
        else:
            ExitMenu = True


def Adv_menu():
    ExitMenu = False
    while ExitMenu == False:
        print("You come back to the worn down town and go back to the inn, the bar keeper laughs")
        print("Didnt expect to see you back, you dont look any different from when you set off, what did you do, hide?")
        print("He laughs then looks at you more seriously. You know, what lies ahead of you is tough, why dont you do some more training")
        selection = input(
            "What would you like to do?\n1.) Fight previous monsters.\n2.) Rest.\n3.) Continue Adventure.")
        if selection == "1":
            monster_menu
            while True:
                battle = input(
                    "1.) Slimes\n2.) Skeletons\n3.) Bandits\n4.) Wyverns\n5.) Return\n")
                # while battle != "1" and battle != "2" and battle != "3" and battle != "4" and battle != "5":
                print("Please choose a valid option 1-5")
                battle = input(
                    "1.) Slimes\n2.) Skeletons\n3.) Bandits\n4.) Wyverns\n5.) Return\n")
                if battle == "1":
                    mob = copy.deepcopy(slimes)
                    SlimePic()
                    slime_(mob, character)
                elif battle == "2":
                    mob = copy.deepcopy(skeleton)
                    skeleart()
                    slime_(mob, character)
                elif battle == "3":
                    mob = copy.deepcopy(bandit)
                    banditart()
                    slime_(mob, character)
                elif battle == "4":
                    mob = copy.deepcopy(wyvern)
                    slime_(mob, character)
                elif battle == "5":
                    break
                else:
                    print("Please choose a valid option 1-5")
        if selection == "2":
            print(
                "You explain that you just need some rest and the bar keeper gives you the #3 key")
            print(
                "This room is worse then the last one you have its literally a bed of straw")
            print("~~~resting~~~")
            time.sleep(5.0)
            character.Health = character.maxHealth
            print(
                f"You have rested, restoring your health back to:{character.maxHealth}")
            break
        if selection == "3":
            Adventure_Text
            ExitMenu = True


def Start_Game():
    print("you have $", character.gold)
    Game_Over = False

    while Game_Over == False:

        menuing()

        if monster_order[0]:
            slime_(monster_order[0], character)
            if monster_order[0][0].health <= 0:
                print(f"you have defeated the {monster_order[0][0].name}")
            elif monster_order[0][1].health <= 0:
                print(f"you have defeated the {monster_order[0][1].name}")
            elif monster_order[0][2].health <= 0:
                print(f"you have defeated the {monster_order[0][2].name}")
            monster_order.pop(0)
            if character.Health <= 0:
                Game_Over = True

        if character.Health <= 0:
            Game_Over = True
            break


def mining(character):
    choice = input("would you like to:\n1.)Go mining\n2.)return to town")
    if character.bag == {"pickaxe"}:
        if choice == "1":
            print("You swing your pickaxe at a strange looking rock")
            hit = random.randint(1, 100)
            if hit <= 20:
                print("You've mined 1 ore")
                character.bag.update({"ore"})
                modify_key = "ore"
                character.bag[modify_key] = character.bag(
                    modify_key, 0) + 1
                pickaxe(character)
                print(character.bag({"ore"}))
            elif hit <= 2:
                print("you've found a gold nugget")
                character.bag.update({"gold nugget"})
                modify_key = "gold nugget"
                character.bag[modify_key] = character.bag(
                    modify_key, 0) + 1
                print(character.bag({"gold nugget"}))
            else:
                while choice != "1" and choice != "2":
                    print("Please choose 1 or 2")
                choice = input(
                    "It appears you didnt find anything this time.\n would you like to:\n1:Continue mining?\n2:Return to town")
                if choice == "1":
                    mining()
                if choice == "2":
                    return
    if choice == "2":
        print("You decide to try again some other time")
        return


Start_Game()
