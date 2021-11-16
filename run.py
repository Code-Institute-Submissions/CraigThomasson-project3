import random
class Entity:
    """
    base class for all player and enemy classes 
    """
    def __init__(self, hp, attack, name, weapon):
        self.hp = hp
        self.attack = attack
        self.name = name
        self.weapon = weapon

    def attack(self):
        damage = randint(3, 9)
        print(damage)


class Player(Entity):
    """
    This will handel all stats and info for the players character
    """
    def __init__(self, items):
        Entity.__init__(self, 10, 3, "Player", "Rusty Knife")
        self.items = items

class Goblin(Entity):
    """
    Base class for all goblin type enemies
    """
    def __init__(self, items):
        Entity.__init__(self, 5, 2, "Goblin", "scimatar")
        self.items = items
        items = []

class Goblin_archer(Goblin):
    """
    specilist goblin class
    """
    def __init__(self):
        Goblin.__init__(self, [])

def goblin_ambush(player_character):
    print("you see an abandoned cart in the road.\n you see that its contents has been looted\n you hear a rustling behind you as an arrow if fired at you buy a goblin as it emerges from cover.")

def ambush_goblin(player_character):
    print("as you sneak around you notice a goblin hiding behind a bush watching the road\n")

def get_player_name():
    """
    used to initiat the game and get the players name inputted to the player class
    """
    player_character = Player(["fire starter", "spare clothes"])
    player_character.name = input("hello traveller what is your name?: ")
    print(f'well met {player_character.name}! take care on these roads there are goblins on the lose.\n')
    return player_character

def introduction(player_character):
    print("you are traveling alone to newtown when you see somthing in the road.\n")
    player_choice = input("type <option 1> to invstigate\n type <option 2> to sneak around:\n")
    if player_choice == "option 1":
        goblin_ambush(player_character)
    if player_choice == "option 2":
        ambush_goblin(player_character)

player_character = get_player_name()

# introduction(player_character)

player_character.attack()