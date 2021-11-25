import random

# character and NPC classes

class Entity:
    """
    base class for all player and enemy classes 
    """
    def __init__(self, health, attack, speed, name, weapon, weapon_inventory):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.name = name
        self.weapon = weapon
        self.weapon_inventory = weapon_inventory

    def make_atk(self): 
        """
        generates character attack value
        """
        damage = self.weapon.atk_mod() + self.attack
        return damage
    
    def change_weapon(self):
        """
        allows the player to see weapon list and change equipped weapon
        """
        weapon_list = []
        for weapon in self.weapon_inventory:
            weapon_list.append(weapon.name)
        print(f'your current weapon list is: {weapon_list}. {self.weapon.name} is equipped')
        weapon_choice = input(f'type the  name of the weapon you would like to equip: ')
        for weapon in self.weapon_inventory:
            if weapon.name == weapon_choice:
                self.weapon = weapon


class Player(Entity):
    """
    This will handel all stats and info for the players character
    """
    def __init__(self, items):
        Entity.__init__(self, 17, 5, 5, "Player", Rusty_knife(), [Rusty_knife(), Scimitar()])
        self.items = items

class Goblin(Entity):
    """
    Base class for all goblin type enemies
    """
    def __init__(self, items):
        Entity.__init__(self, 10, 2, 6, "Goblin", Scimitar(), [Scimitar()])
        self.items = items
        items = []

class Goblin_archer(Goblin):
    """
    specialist goblin subclass
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
        damage = random.randint(self.min_atk, self.max_atk)
        return damage

class Rusty_knife(Weapon):
    def __init__(self):
        Weapon.__init__(self, 1, 5, "Rusty knife")

class Scimitar(Weapon):
    def __init__(self):
        Weapon.__init__(self, 1, 7, "Scimitar")

#game functions

def battle(player_character, enemy):
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
            battle_option(player_character, enemy)

def battle_option(player, enemy):
    """
    Gives the player some options during combat. 
    """
    print(f"you are in combat with a {enemy.name} you can: Attack or change weapon")
    choice = input("what will you do?:...\n To attack type: option 1\n To change weapon type: option 2: ")
    if choice == "option 1":
        print("atck option")
    if choice == "option 2":
        print("weapon option")
        player.change_weapon()


# story functions

def goblin_ambush(player_character):
    print("you see an abandoned cart in the road.\n The cart has been looted\n you hear a rustling behind you as a goblin charges at you from cover.\n")

def ambush_goblin(player_character):
    print("as you sneak around you notice a goblin hiding behind a bush watching the road\n")
    choice = input("what would you like to do?\n type 'option 1' to attack\n type 'option 2' to sneak past....:\n")
    if choice == "option 1":
        battle(player_character, Goblin("chalk, rabit"))
    if choice == "option 2":
        print("more content coming soon...")

def get_player_name():
    """
    used to initiat the game and get the players name inputted to the player class
    """
    player_character = Player(["fire starter"])
    player_character.name = input("hello traveller what is your name?: ")
    print(f'well met {player_character.name}! take care on these roads there are goblins on the loose.\n')

    battle(player_character, Goblin("chalk, rabit"))
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




