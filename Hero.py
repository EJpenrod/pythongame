
from operator import inv
import random
import time
from monsters import monster_class


from Ascii import Monktext, Necrotext, Paladintext, Roguetext


class inventory():
    gold = 0
    bag = {"pickaxe": 1}
    left_hand = []
    right_hand = []
    chest = []
    head = []
    feet = []
    left_ring = []
    right_ring = []
    neck = []
    charm_1 = []
    charm_2 = []

    def __int__(self, gold, bag, left_hand, right_hand, chest, head, feet, left_ring, right_ring, neck, charm_1, charm_2):
        self.gold = gold
        self.bag = bag
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.chest = chest
        self.head = head
        self.feet = feet
        self.left_ring = left_ring
        self.right_ring = right_ring
        self.neck = neck
        self.charm_1 = charm_1
        self.charm_2 = charm_2


class player(inventory):

    Health = 100
    Damage = 10
    Strength = 10
    Speed = 10
    Vit = 10
    Int = 10
    Dex = 10
    name = ""
    real_user_damage = 0
    exp = 0
    Level = 0
    maxHealth = 100

    def __init__(self, Health, Damage, Strength, Speed, Vit, Int, Dex, Name, true_damage, exp, Level, maxHealth):

        self.Health = Health
        self.Damage = Damage
        self.Strength = Strength
        self.Speed = Speed
        self.Vit = Vit
        self.Int = Int
        self.Dex = Dex
        self.Name = Name
        self.real_user_damage = true_damage
        self.exp = exp
        self.Level = Level
        self.maxHealth = maxHealth

    def getHealth(self):
        return self.Health

    def getDamage(self):
        return self.Damage

    def getStrength(self):
        return self.Strength

    def getSpeed(self):
        return self.Speed

    def getVit(self):
        return self.Vit

    def getInt(self):
        return self.Int

    def getDex(self):
        return self.Dex

    def setHealth(self, newHealth):
        self.Health = newHealth
        return self.Health

    def setDamage(self, newDamage):
        self.Damage = newDamage
        return self.Damage

    def setStrength(self, newStrength):
        self.strength = newStrength
        return self.strength

    def setSpeed(self, newSpeed):
        self.Speed = newSpeed
        return self.Speed

    def setVit(self, newVit):
        self.Vit = newVit
        return self.Vit

    def setInt(self, newInt):
        self.Int = newInt
        return self.Int

    def setDex(self, newDex):
        self.Dex = newDex
        return self.Dex


def RandomStatRoll(NewPlayer):

    roll = input("Press enter to roll for stats: ")
    print("rolling dice...")
    time.sleep(0.2)
    NewPlayer.maxHealth += random.randint(90, 110)
    print("Your character has rolled", NewPlayer.maxHealth, " to total health. ")
    NewPlayer.Health = NewPlayer.maxHealth
    NewPlayer.Damage += random.randint(5, 10)
    print("Your character has rolled", NewPlayer.Damage, " to total damage. ")
    NewPlayer.Strength += random.randint(5, 10)
    print("Your character has rolled",
          NewPlayer.Strength, " to total strength. ")
    NewPlayer.Speed += random.randint(5, 10)
    print("Your character has rolled", NewPlayer.Speed, " to total speed. ")
    NewPlayer.Vit += random.randint(5, 10)
    print("Your character has rolled", NewPlayer.Vit, " to total vitality. ")
    NewPlayer.Int += random.randint(5, 10)
    print("Your character has rolled", NewPlayer.Int, " to total intelligence. ")
    NewPlayer.Dex += random.randint(5, 10)
    print("Your character has rolled", NewPlayer.Dex, " to total dexterity. ")


def createClass():
    NewPlayer = player(0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0)

    print("""
    WELCOME DARING ADVENTURER!!!, I tell ya there be stories of riches!
    small disclaimer: deathissomethingthatyouwillmostlikelyexpierencebutthatsariskimwillingtotake
    BUT DONT LET THAT STOP YOU!!!!, you're different! kind of like what i told all those other adventures...
    come to think of it, its probably best if you just dont do this....
    no? you want honor? GLORY? bah i say! tell ya what kid fill ya pockets with some coin, that;s a real hero!
    ok ok. ya convinced me, well here is the deal. there be dragons. 
    OH THE RICHES THEY HOLD!!!!
    just get your trusty fire extinguisher... erm. well just dont get hit by the fire... or claws... or teeth. 
    actually the tail is pretty.. ya know what? just wait until its sleeping and the steal its stuff.
    
    Well looks like that's all the time i got!
    just uh decide what class you want to be and get out there champ!   
    
    """)
    a = input(f"Do you fancy: \n1.)Upstanding citizens. \n2.)Dastardly heroes.\n ")
    while a != "1" and a != "2":
        print("Please choose your path. ")
        a = input("Are you more prone to be in: \n1.)The Light? \n2.)The Dark?\n ")

    if a == "1":
        b = input("How did you find your path?: \n1.)Intensive meditation and fasting, seeking enlightinment from within.\n2.)You path was ordaned from the church, you are on call from up high.\n ")
        while b != "1" and b != "2":
            print("please choose your path. ")
            b = input("1.)Intensive meditation and fasting, seeking enlightinment from within.\n2.)Your path was ordaned from the church, you are on call from up high.\n  ")
        if b == "1":
            print("Your class is:")
            Monktext()
            print("""
            You where always fascinated by inner strength. You started fasting to prove to yourself that you can ascend
            from bodily needs like food or water. Bah. The thing of mortals you said. after going 4 days and passing out
            only to be fed food and water by some one who scooped you off the street, you became obsessed with beating
            your own body. After years of failing to get past seven days, you did it. you finally did it. you made it to
            day eight. You are not sure what you saw or how you saw it. You felt embraced by warmth and strength.For
            some reason there is an impression of a gluttonous dragon. You must fell the best to prove that those who dont
            eat are infact superior.
            """)
            RandomStatRoll(NewPlayer)
        elif b == "2":
            print("Your class is:")
            Paladintext()
            print("""
            You as a young child where obsessed with knights. You dreamed of becoming one, the shiny armor, the big swords
            even their mounts awestruck you. However when you where a teen your dreams where shattered. instead of your
            parents sending you to the barracks to training in the sword they sent you to the church to take up the cloth.
            You vowed to yourself that this set back wouldn't hold you back from obtaining your dreams. After years of 
            working away for the church an opportunity arose. They are looking for young cadets to become a church's knight
            something called a pal or din. You didnt care what they called you, you where hooked at the word knight.
            you made it passed the exams and became a cadet, eventually a knight in training, to be ordaned by the church
            you must slay a beast of darkness. With that you have set off on your adventure to finally become a knight.         
            
            """)
            RandomStatRoll(NewPlayer)

    elif a == "2":
        b = input(
            "Are you more heroic reading books or hiding in ill lit alley ways?: \n1.)Dark Arts\n2.)Shadows\n ")

        while b != "1" and b != "2":
            print("please choose your class. ")
            b = input(
                "Have you studied the dark arts or the way of shadows: \n1.)sorcery?\n2.)shadows?\n ")

        if b == "1":
            Necrotext()
            print("""
            A fledgling Necromancer, you found what you thought was your great grannies cook book.
            Turns out it was incantations for cursed soup and the power you felt watching your bully get a case
            of the tummy aches after he stole your lunch (all planed by you, you devious person you!)
            you where enthralled by the power and now you lust for more!
            """)
            print("")
            RandomStatRoll(NewPlayer)

        if b == "2":
            Roguetext()
            print("""
            Once a black cat crossed your path. You where in a mood of sorts that day so you ignored the signs.
            The cat, most displeased by your actions attacked you from every shadow it could find for 2 weeks straight!
            after many scratches and a strange case of your hair constantly standing on end. You slowly adapted and learned
            the way of shadows. First it was shooting tomatoes from a local food stand with a sling shot. Poor shop keeper
            ended up closing down shop saying that particular location was cursed.
            With your loyal cat (all though cats are finicky so dont hold out hope for it being you life long companion)
            you have decided to enlist as an adventurer and put your ninja cat training to the test!
            
            """)
            print("")
            RandomStatRoll(NewPlayer)

    playerName = input("what is your name?: ")
    print("Welcome", playerName, "Your adventure is about to begin...")
    NewPlayer.real_user_damage = random.randint(1, NewPlayer.Damage)
    return player(NewPlayer.Health, NewPlayer.Damage, NewPlayer.Strength, NewPlayer.Speed, NewPlayer.Vit, NewPlayer.Int,
                  NewPlayer.Dex, playerName, NewPlayer.real_user_damage, NewPlayer.exp, NewPlayer.Level,
                  NewPlayer.maxHealth)


def currency(monsters, character):
    gold = 0
    for monster in monsters:
        gold += monster.gold
    character.gold = character.gold + gold
    print("You have obtained $", gold,
          "Your total amount of $ is:", character.gold)
    return character.gold


def player_level(monsters, character):
    total_exp = 0
    exp_to_lvl = [20, 30, 45, 68, 101, 152, 228,
                  342, 513, 769, 1153, 1730, 2595, 3892]
    for monster in monsters:
        total_exp += monster.exp
    character.exp = character.exp + total_exp
    hero_level = character.exp >= exp_to_lvl[character.Level]
    print("You have obtained:", total_exp,
          "Exp. Your total exp is:", character.exp)

    if hero_level:
        print("Congratulations you have leveled up!")
        character.Level = character.Level + 1
        character.maxHealth = int(character.maxHealth + character.Level + 5)
        print("You have gained :", character.Level + 5, "Health Points")
        print("Your new health total is:", character.maxHealth)
        character.Health = character.maxHealth
        character.Damage = int(character.Damage + character.Level + 3)
        print("You have gained :", character.Level + 3, "Damage Points")
        print("Your new Damage total is:", character.Damage)
        character.Dex = float(character.Dex + character.Level * 0.005)
        print(f"You are now LvL {character.Level}!")

        return character.Health, character.Damage, character.Dex, character.Level, character.exp

        # something something randranint stats + base stats = new stats then return them

# pprint(vars(character))
