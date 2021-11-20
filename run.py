import random

# character and NPC classes

class Entity:
    """
    base class for all player and enemy classes 
    """
    def __init__(self, health, attack, speed, name, weapon):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.name = name
        self.weapon = weapon

    def make_atk(self): 
        """
        generates character attack value
        """
        damage = self.weapon.atk_mod() + self.attack
        return damage

class Player(Entity):
    """
    This will handel all stats and info for the players character
    """
    def __init__(self, items):
        Entity.__init__(self, 17, 5, 5, "Player", Rusty_knife())
        self.items = items

class Goblin(Entity):
    """
    Base class for all goblin type enemies
    """
    def __init__(self, items):
        Entity.__init__(self, 10, 2, 6, "Goblin", Scimitar())
        self.items = items
        items = []

class Goblin_archer(Goblin):
    """
    specilist goblin class
    """
    def __init__(self):
        Goblin.__init__(self, [])

# weapon classes

class Weapon:
    """
    this is the base class for all weapons 
    """
    def __init__(self, min_atk, max_atk, name):
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.name = name
    
    def atk_mod(self):
        dameage = random.randint(self.min_atk, self.max_atk)
        return dameage

class Rusty_knife(Weapon):
    def __init__(self):
        Weapon.__init__(self, 1, 5, "Rusty knife")

class Scimitar(Weapon):
    def __init__(self):
        Weapon.__init__(self, 1, 7, "Scimitar")

#game functions

def battel(player_character, enemy):
    print("batteling")
    if player_character.speed < enemy.speed:
        while player_character.health > 0 and enemy.health > 0:
            player_damage = player_character.make_atk()
            enemy_damage = enemy.make_atk()

            print(f'{player_character.name} attacks {enemy.name} with {player_character.weapon.name} for {player_damage} damage')
            enemy.health -= player_damage
            print(f"{enemy.name}'s health is now {enemy.health}\n")
            if enemy.health <= 0:
                print(f"you have slane the {enemy.name}")
                break
           
            print(f'{enemy.name} attacks {player_character.name} with {enemy.weapon.name} for {enemy_damage} damage')
            player_character.health -= enemy_damage
            print(f"{player_character.name}'s health is now {player_character.health}\n")
            if player_character.health <= 0:
                print(f"you have been slain by the {enemy.name}....\n")
                player_character = get_player_name()
# story functions

def goblin_ambush(player_character):
    print("you see an abandoned cart in the road.\n The cart has been looted\n you hear a rustling behind you as a goblin charges at you from cover.")

def ambush_goblin(player_character):
    print("as you sneak around you notice a goblin hiding behind a bush watching the road\n")
    battel(player_character, Goblin("chalk, rabit"))

def get_player_name():
    """
    used to initiat the game and get the players name inputted to the player class
    """
    player_character = Player(["fire starter", "spare clothes"])
    player_character.name = input("hello traveller what is your name?: ")
    print(f'well met {player_character.name}! take care on these roads there are goblins on the loose.\n')
    return player_character

def introduction(player_character):
    print("you are traveling alone to newtown when you see somthing in the road.\n")
    player_choice = input("type <option 1> to invstigate\n type <option 2> to sneak around:\n")
    if player_choice == "option 1":
        goblin_ambush(player_character)
    if player_choice == "option 2":
        ambush_goblin(player_character)


player_character = get_player_name()

introduction(player_character)




