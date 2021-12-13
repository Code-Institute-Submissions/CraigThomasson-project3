import random
import pyfiglet

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
        print(f'your current weapon list is: {weapon_list}.')
        print(f'{self.weapon.name} is equipped')
        weapon_choice = input(
            'type the  name of the weapon you would like'
            ' to equip: '
        )
        weapon_choice = weapon_input_validation(weapon_choice, weapon_list)
        for weapon in self.weapon_inventory:
            if weapon.name == weapon_choice:
                self.weapon = weapon


class Player(Entity):
    """
    This will handel all stats and info for the players character
    """
    def __init__(self, items):
        Entity.__init__(
            self, 17, 5, 5, "Player", Rusty_knife(),
            [Rusty_knife()]
        )
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


# game functions


def weapon_name_list(weapon):
    """
    creats a list of weapon.names in list of weapon classs
    """
    new_list = []
    for item in weapon.weapon_inventory:
        new_list.append(item.name)
    return new_list


def battle(player_character, enemy):
    if player_character.speed < enemy.speed:
        while player_character.health > 0 and enemy.health > 0:
            player_damage = player_character.make_atk()
            enemy_damage = enemy.make_atk()

            print(
                f'{player_character.name} attacks '
                f'{enemy.name} with '
                f'{player_character.weapon.name} for '
                f'{player_damage} damage'
            )
            enemy.health -= player_damage
            print(f"{enemy.name}'s health is now {enemy.health}\n")
            if enemy.health <= 0:
                print(f"you have slane the {enemy.name}")
                loot(player_character, enemy)
                return player_character
            print(
                f'{enemy.name} attacks '
                f'{player_character.name} with '
                f'{enemy.weapon.name} for '
                f'{enemy_damage} damage'
            )
            player_character.health -= enemy_damage
            print(
                f"{player_character.name}'s health is now"
                f'{player_character.health}\n'
            )
            if player_character.health <= 0:
                print(f"you have been slain by the {enemy.name}....\n")
                player_death(player_character)
            battle_option(player_character, enemy)


def battle_option(player, enemy):
    """
    Gives the player some options during combat
    """
    print(
        f"you are in combat with a {enemy.name}"
        f" you can: Attack or change weapon"
    )
    choice = input(
        "what will you do?:...\n To attack type: option 1\n"
        " To change weapon type: option 2: "
    )
    choice = input_validation(choice, "option1", "option2")
    print("")
    if choice == "option1":
        print("\n")
    if choice == "option2":
        player.change_weapon()


def loot(player_character, enemy):
    """
    allows player to take items and weapons from dead enemies.
    gets enemy.items and enemy.weapon_invemtory and adds them
    to player_character. items and player-character.weapon_inventory.
    prints what items and weapons have been looted.
    """
    print(f"{enemy.name} lies dead at your feet\n")
    choice = input(
        f"Type 'loot' if you would like to loot the {enemy.name}\n"
        "Type 'continue' to continue...:"
        )
    choice = input_validation(choice, "loot", "continue")
    if choice == "loot":
        for item in enemy.items:
            player_character.items.append(item)
        for weapon in enemy.weapon_inventory:
            player_character.weapon_inventory.append(weapon)
        enemy_weapon_list = weapon_name_list(enemy)
        print(*enemy.items, ' added to your inventory')
        print(*enemy_weapon_list, ' added to your weapon inventory')


def weapon_input_validation(choice, weapon_list):
    valid_choice = choice.rstrip().lstrip().lower().capitalize()
    if valid_choice in weapon_list:
        return valid_choice
    while valid_choice not in weapon_list:
        print(
            "Invalid choice please use one of the "
            "following options to continie", weapon_list
        )
        valid_choice = input(
            'Enter choice here..:'
        ).rstrip().lstrip().lower().capitalize()
        print("")
        if valid_choice in weapon_list:
            return valid_choice


def input_validation(choice, *args):
    """
    Takes player in put on mutilple givin options(args)
    and validates th input.
    If input is invalsid it promps the useer to input again.
    It then returns the validated input.
    """
    valid_choice = choice.replace(" ", "")
    valid_choice = valid_choice.lower()
    if valid_choice in args:
        return valid_choice
    while valid_choice not in args:
        print(
            "Invalid choice please use one of the "
            "following options to continie", args
        )
        valid_choice = input('Enter choice here..:').replace(" ", "").lower()
        if valid_choice in args:
            return valid_choice


# story functions


def banner():
    banner1 = pyfiglet.figlet_format("Wellcome to")
    banner2 = pyfiglet.figlet_format("Adventure game")
    print(banner1)
    print(banner2)

def get_player_name():
    """
    used to initiat the game and get the players name
    inputted to the player class
    """
    player_character = Player(["fire starter"])
    player_character.name = input("Hello traveller what is your name?: ")
    print(
        f'Well met {player_character.name}!'
        f' Take care on these roads there are goblins on the loose.\n'
    )
    return player_character


def introduction(player_character):
    """
    yes pyfiglet to create intro banner and runs a basic into for the player.
    """
    print(
        "You are traveling alone to newtown"
        " when you see somthing in the road.\n"
    )
    choice = input(
        "Type <option 1> to invstigate\n"
        "Type <option 2> to sneak around:\n"
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        goblin_ambush(player_character)
    if choice == "option2":
        ambush_goblin(player_character)


def goblin_ambush(player_character):
    print(
        "you see an abandoned cart in the road.\n"
        "The cart has been looted\n"
        "you hear a rustling behind you as"
        " a goblin charges at you from cover.\n"
    )


def ambush_goblin(player_character):
    """
    The function will run if the player chooses to be stealthy
    when they see the cart in the road.
    """
    print(
        "As you sneak around"
        " you notice a goblin hiding behind a bush watching the road\n"
    )
    choice = input(
        "What would you like to do?\n\n"
        "Type 'option 1' to attack\n Type 'option 2' to sneak past....:\n"
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        player_character = battle(player_character, Goblin(["chalk", "rabit"]))
    if choice == "option2":
        print("More content coming soon...")


def hidden_path(player_character):
    """
    the player is given a chioce to follow a hiden path or go on to town
    """
    print(
        "As you begin to head of down the road"
        "you notice a trail behind the bushes where the goblin was hiding."
    )
    choice = input(
        "Type 'option 1' to follow the hidden path"
        "Type 'option 2' to continue down the road to Newtown"
        "...: "
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        goblin_cave_entrance(player_character)
    if choice == "option2":
        newtown(player_character)


def goblin_cave_entrance(player_character):
    print(
        "You follow the track for over an hour before you come"
        "to the foot of a large hill."
        "The track leads up to a hidden cave opening"
    )
    choice = input(
        "Type 'option 1' to enter the cave"
        "Type 'option 2' to investigate the area"
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        wolf_fight(player_character)
    if choice == "option2":
        sneak_past_wolf(player_character)


def player_death(player_character):
    """
    This function should be called when ever the player dies.
    It gives them the option to play again or quit the game.
    """
    print(f'{player_character.name} has died!')
    choice = input(
        "Would you play again?\n"
        "Type 'yes' to play again "
        "or Type 'no' to quit...:"
        )
    choice = input_validation(choice, "yes", "no")
    if choice == "yes":
        main()
    if choice == "no":
        quit_game(player_character)


def quit_game(player_character):
    """
    This function should only be run when the player
    has chosen to end the game.
    It simply prints a message to the player once they decid to end the game.
    """
    print(
        f"It is with a heavy heart I bid the fairwell {player_character.name}"
        "I hope to see you again one day on a new adventure!"
        )


def main():
    banner()
    player_character = get_player_name()
    introduction(player_character)


main()