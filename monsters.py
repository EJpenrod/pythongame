
import random


class monster_class:
    hp = 0
    damage = 0
    strength = 0
    spd = 0
    vit = 0
    intelligence = 0
    dex = 0
    type = 0
    name = ""
    namelist = ["Igran", "Qinzag", "Oqqiaz", "Caddarruik", "Iqqiz", "Tikkuac", "Ondi", "Vokked", "Ikag", "Uakot",
                "Threvu", "Avresik", "Krigrotux", "Drugzia", "Driangak", "Nudgiq", "Juirez", "Ratras", "Zuqqacad",
                "Tikkuac", "Jinnikron", "Irraq", "Grathaq", "Nihreih", "Tridgaud", "Igran", "Qinzag", "Toqos",
                "Vikzonuq", "Troqqiaccot", "Teinged", "Xorroz", "Vuthi", "Kagrito", "Andraz", "Grathaq", "Sollmulach",
                "Kolgan", "Ogdrag", "Ogdrillok", "Bor'gamon", "Dronorith", "Trorgren", "Koz'garag", "Mullmid",
                "Verthruzath", "Tag'tharez", "Bakan" "Izrurath", "Molmannith", "Zigrothan", "Ragthumon", "Migmathiz",
                "Olgonnoth", "Aggoman", "Trarzenath", "Gerthramak", "Darthronath", "Margos", "Darthrollech"]
    typelist = ["slime", "dragon", "skeleton", "werewolf", "wyvern", "bandit", "ogre", "chimera", "minotaur"]
    exp = 0

    def __init__(self, health, damage, strength, speed, vit, intelligence, dex, type, exp, gold):
        self.hp = health
        self.damage = damage
        self.strength = strength
        self.speed = speed
        self.vit = vit
        self.intelligence = intelligence
        self.Dex = dex
        self.type = type
        self.name = self.namelist[random.randint(0, len(self.namelist)-1)]
        self.name = self.name + " The " + self.typelist[type]
        self.exp = exp
        self.gold = gold

    def attributes(self):
        string = " health: " + str(self.hp) + " Damage: " + str(self.damage) + " strength: " + str(self.strength) + \
                 " speed: " + str(self.spd) + " vitality: " + str(self.vit) + " intelligence: " + \
                 str(self.intelligence) + " dexterity: " + str(self.dex) + "type" + str(self.type) + \
                 "Experience value" + str(self.exp) + "Gold Value" + str(self.gold)
        return string

    def is_dead(self):

        return self.hp <= 0

    def print_health(self, damage):
        print(F"{self.name}'s health is at : {self.hp}\n")
        print(f"{self.name} attacks for : {damage}")


slime = monster_class(40, 2, 1, 1, 1, 1, 1, 0, random.randint(1, 5), random.randint(1, 5))
black_dragon = monster_class(600, 50, 10, 10, 10, 10, 10, 1, random.randint(200, 1000), random.randint(200, 1000))
skeleton = monster_class(20, 3, 1, 1, 1, 1, 1, 2, random.randint(2, 6), random.randint(1, 5))
werewolf = monster_class(125, 10, 1, 1, 1, 1, 1, 3, random.randint(10, 30), random.randint(1, 5))
wyvern = monster_class(200, 20, 1, 1, 1, 1, 1, 4, random.randint(25, 100), random.randint(1, 5))
bandit = monster_class(30, 10, 8, 5, 6, 4, 5, 5, random.randint(10, 20), random.randint(10, 20))
ogre = monster_class(150, 20, 4, 2, 3, 4, 6, 6, random.randint(20, 50), random.randint(20, 30))
chimera = monster_class(400, 30, 10, 10, 10, 10, 4, 7, random.randint(30, 100), random.randint(30, 100))
minotaur = monster_class(220, 15, 5, 5, 5, 4, 4, 8, random.randint(20, 90),random.randint(30, 200))
