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

# this is my empty monster bag

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

# this is where i put monsters in the bag :D

for guyimfighting in range(randint(2, 3)):
    slimes.append(monster_class(40, 2, 1, 1, 1, 1, 1, 0, random.randint(1, 5), random.randint(1, 5)))
for guyimfighting in range(randint(1, 1)):
    dragons.append(monster_class(200, 100, 10, 10, 10, 10, 10, 1, random.randint(200, 1000), random.randint(200, 1000)))
for guyimfighting in range(randint(1, 3)):
    skeleton.append(monster_class(20, 3, 1, 1, 1, 1, 1, 2, random.randint(10, 30), random.randint(1, 5)))
for guyimfighting in range(randint(1, 2)):
    werewolf.append(monster_class(125, 10, 1, 1, 1, 1, 1, 3, random.randint(25, 100), random.randint(1, 5)))
for guyimfighting in range(randint(1, 3)):
    wyvern.append(monster_class(50, 25, 1, 1, 1, 1, 1, 4, random.randint(25, 100), random.randint(1, 5)))
for guyimfighting in range(randint(1, 3)):
    bandit.append(monster_class(30, 10, 8, 5, 6, 4, 5, 5, random.randint(10, 20), random.randint(10, 20)))
for guyimfighting in range(randint(1,2)):
    ogre.append(monster_class(80, 20, 4, 2, 3, 4, 6, 6, random.randint(20, 50), random.randint(20, 30)))
for guyimfighting in range(randint(1,2)):
    chimera.append(monster_class(140, 20, 10, 10, 10, 10, 4, 7, random.randint(30, 100), random.randint(30, 100)))
for guyimfighting in range(randint(1,2)):
    minotaur.append(monster_class(120, 10, 5, 5, 5, 4, 4, 8, random.randint(20, 90),random.randint(30, 200)))

def menuing():

    ExitMenu = False

    while ExitMenu == False:
        selection = input("What would you like to do: ?\n1.)Go to town\n2.)Adventure onward!!\n ")
        while selection != "1" and selection != "2":
            print("Please choose 1 or 2")
            selection = input("What would you like to do: ?\n1.)Go to town\n2.)Adventure onward!!\n ")
        if selection == "1":
            print("You have arrived in a shoddy looking town, not much here except a tavern and a few locals")
            time.sleep(1.0)
            print("As the tavern doors squeak open, you see an overweight man behind the counter, a few customers.")
            print("and what appears to be a man in the corner with his pet pig")
            time.sleep(1.0)
            print("'Oh look another adventurer' said the barkeep, 'or as i like to call em walking coin bags....")
            print("With a hearty laugh he looks at you expectantly")
            time.sleep(1.0)
            print("As you just look at the bar keeper he says:")
            print("Well don't go standing there go ahead and get some food and rest, he throws you the key its marked #2.")
            time.sleep(1.0)
            print("You go into the room marked #2, the bed is a grade above a bed of straw, but sleep calls, you answer.")
            print("~~~Resting~~~")
            time.sleep(5.0)
            character.Health = character.maxHealth
            print(f"You have rested, restoring your health back to:{character.maxHealth}")

        elif selection == "2":
            Adventure_Text
            ExitMenu = True
        else:
            ExitMenu = True

def Adv_menu():
    ExitMenu = False
    while ExitMenu == False:
        print("You come back to the worn down town and go back to the inn, the bar keeper laughs")
        print("Didnt expect to see you back, you dont look any different from when you set off, what did you do, hide?")
        print("He laughs then looks at you more seriously. You know, what lies ahead of you is tough, why dont you do some more training")
        selection = input("What would you like to do?\n1.) Fight previous monsters.\n2.) Rest.\n3.) Continue Adventure.")
        if selection == "1":
            monster_menu()
            while True:
                battle = input("1.) Slimes\n2.) Skeletons\n3.) Bandits\n4.) Wyverns\n5.) Return\n")
                #while battle != "1" and battle != "2" and battle != "3" and battle != "4" and battle != "5":
                print("Please choose a valid option 1-5")
                battle = input("1.) Slimes\n2.) Skeletons\n3.) Bandits\n4.) Wyverns\n5.) Return\n")
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
            print("You explain that you just need some rest and the bar keeper gives you the #3 key")
            print("This room is worse then the last one you have its literally a bed of straw")
            print("~~~resting~~~")
            time.sleep(5.0)
            character.Health = character.maxHealth
            print(f"You have rested, restoring your health back to:{character.maxHealth}")
            break
        if selection == "3":
            Adventure_Text()
            ExitMenu = True



def Start_Game():
    print(character.gold)
    Game_Over = False

    while Game_Over == False:

        UserMenuText()
        menuing()
        SlimePic()
        print(f"slimes im fighting {len(slimes)}")
        slime_(slimes, character)
        if character.Health <=0:
            Game_Over = True
            break

        menuing()
        skeleart()
        print(f"skeletons im fighting {len(skeleton)}")
        slime_(skeleton, character)
        if character.Health <= 0:
            Game_Over = True
            break

        menuing()
        banditart()
        print(f" You are surrounded by {len(bandit)}")
        slime_(bandit, character)
        if character.Health <= 0:
            Game_Over = True
            break

        menuing()
        print(f"Wyverns im fighting {len(wyvern)}")
        slime_(wyvern, character)
        if character.Health <= 0:
            Game_Over = True
            break

        Adv_menu()
        print(f"werewolf im fighting {len(werewolf)}")
        slime_(werewolf, character)
        if character.Health <= 0:
            Game_Over = True
            break

        print(f"dragons im fighting {len(dragons)}")
        slime_(dragons, character)
        if character.Health <= 0:
            Game_Over = True
            break

Start_Game()