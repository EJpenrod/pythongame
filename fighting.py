import random
from Ascii import bottomline, topline, win, loss, line
from monsters import *
from Hero import *
from text import ran_texty


def slime_(monsters, character):

    gameover = False

    while gameover == False:
        True_damage = random.randint(1, character.Damage)

        # this is the line where you choose your attack action

        for guyimfighting in monsters:

            if guyimfighting.hp > 0:

                real_slime_damage = random.randint(1, guyimfighting.damage)
                character.Health = character.Health - real_slime_damage
                #classselection.user_hp = classselection.user_hp - real_slime_damage
                ran_texty()

                user_action = input(
                    "What would you like to do?\n1.) Attack\n:")

                if user_action == "attack" or user_action == "1" or user_action == "Attack":
                    topline()
                    if guyimfighting.Dex - character.Dex <= 0:
                    print(character.name, "attacks for :",
                          True_damage + (character.Strength / 2))

                    #print(F"{classselection.user_type} attacks for : {classselection.real_user_damage}")
                    guyimfighting.hp = guyimfighting.hp - \
                        (True_damage + character.Strength / 2)

                    # this is the monster health line

                    guyimfighting.print_health(real_slime_damage)

                    # this is the user health line
                    print(f"{character.Name} is at :{character.Health}")
                    bottomline()
                    # this is your loss condition

            if character.Health <= 0:
                loss("")
                print(f"you lost")
                print(f"{guyimfighting.name} wins!")
                gameover = True
                break

                # this is your win condition

            all_monsters_dead = True

            for guyimfighting in monsters:
                if guyimfighting.hp > 0:
                    all_monsters_dead = False

            if all_monsters_dead == True:
                win("")
                print(guyimfighting.name, "was felled by:", character.Name, "\n")
                player_level(monsters, character)
                gameover = True
                break
