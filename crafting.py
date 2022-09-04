import monsters
from Ascii import SlimePic, UserMenuText, skeleart, banditart, monster_menu
from random import *
from Hero import *
from Slime import slime_
from text import Adventure_Text
import time
import copy

# Here we are going to define a pick axe.


def pickaxe(character):
    pickaxe = 10
    for hit in pickaxe:
        pickaxe -= 1
        print("Your pickaxe has has lost 1 durability")
        if pickaxe == 0:
            print("Your pickaxe has broken")
            character.bag.pop("pickaxe")
            print(character.bag)
            break


# we are going to program a mining action which is something that can be done from the town menu


def mining(character):
    if character.bag == {"pickaxe"}:
        choice = input("would you like to:\n1.)Go mining\n2.)return to town")
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
        print("You return to town")
        return
