import random
import pyfiglet
import time
import sys

# character and NPC classes


class Entity:
    """
    base class for all player and enemy classes
    """
    def __init__(self, health, attack, name, weapon, weapon_inventory):
        self.health = health
        self.attack = attack
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
        delay_print(f'your current weapon list is: {weapon_list}.')
        delay_print(f'{self.weapon.name} is equipped.')
        weapon_choice = input(
            ' Type the  name of the weapon you would like'
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
    def __init__(self, items, cave, newtown):
        Entity.__init__(
            self, 17, 5, "Player", Rusty_knife(), [Rusty_knife()])
        self.items = items
        self.cave = cave
        self.newtown = newtown


class Goblin(Entity):
    """
    Base class for all goblin type enemies
    """
    def __init__(self, items):
        Entity.__init__(self, 10, 2, "Goblin", Scimitar(), [Scimitar()])
        self.items = items
        items = []


class Goblin_boss(Entity):
    """
    big bad boss class
    """
    def __init__(self):
        Entity.__init__(self, 15, 3, "goblin Leader", Axe(), [Axe()])


class Wolf(Entity):
    """
    wolf class
    """
    def __init__(self):
        Entity.__init__(self, 11, 4, "wolf", Bite(), [])


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
        """
        calculates the attack damage based on the weapons min and max damage.
        genrated a random number between min and max atk
        """
        damage = random.randint(self.min_atk, self.max_atk)
        return damage


class Rusty_knife(Weapon):
    """
    basic starter weapon for player character
    """
    def __init__(self):
        Weapon.__init__(self, 1, 5, "Rusty knife")


class Scimitar(Weapon):
    """
    second tier weapon has a chance to do slightly more damage
    """
    def __init__(self):
        Weapon.__init__(self, 1, 7, "Scimitar")


class Axe(Weapon):
    """
    this weapon has the highest damage potential in the game
    """
    def __init__(self):
        Weapon.__init__(self, 1, 9, "Axe")


class Bite(Weapon):
    """
    Natural weapon should only be used by crutures with a natural bite force.
    """
    def __init__(self):
        Weapon.__init__(self, 2, 5, "Bite")


# game functions


# this code was copied fro stackoverflow.com
# links in read me
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


def weapon_name_list(weapon):
    """
    creats a list of weapon.names in list of weapon classs
    """
    new_list = []
    for item in weapon.weapon_inventory:
        new_list.append(item.name)
    return new_list


def battle(player_character, enemy):
    """
    main combat loop. this will sicle through cambate between
    player character and selcted enemy class.
    the loop will end when ether the player or the enemy has
    less then 0 health.
    """
    while player_character.health > 0 and enemy.health > 0:
        player_damage = player_character.make_atk()
        enemy_damage = enemy.make_atk()
        delay_print(
            f'{player_character.name} attacks '
            f'{enemy.name} with '
            f'{player_character.weapon.name} for '
            f'{player_damage} damage'
        )
        enemy.health -= player_damage
        delay_print(f" {enemy.name}'s health is now {enemy.health}\n")
        if enemy.health <= 0:
            delay_print(f"you have slane the {enemy.name} ")
            player_character = loot(player_character, enemy)
            return player_character
        delay_print(
            f'{enemy.name} attacks '
            f'{player_character.name} with '
            f'{enemy.weapon.name} for '
            f'{enemy_damage} damage'
        )
        player_character.health -= enemy_damage
        delay_print(
            f" {player_character.name}'s health is now "
            f'{player_character.health}\n'
        )
        if player_character.health <= 0:
            delay_print(f"you have been slain by the {enemy.name}....\n")
            player_death(player_character)
        battle_option(player_character, enemy)


def battle_option(player, enemy):
    """
    Gives the player some options during combat
    """
    delay_print(
        f"you are in combat with a {enemy.name}"
        f" you can: Attack or change weapon\n"
    )
    choice = input(
        "what will you do?:...\n To attack type: option 1\n"
        " To change weapon type: option 2.\n: "
    )
    choice = input_validation(choice, "option1", "option2")
    print("")
    if choice == "option1":
        return player
    if choice == "option2":
        player.change_weapon()
        return player


def loot(player_character, enemy):
    """
    allows player to take items and weapons from dead enemies.
    gets enemy.items and enemy.weapon_invemtory and adds them
    to player_character. items and player-character.weapon_inventory.
    prints what items and weapons have been looted.
    """
    print("")
    delay_print(f"{enemy.name} lies dead at your feet\n")
    choice = input(
        f"Type 'loot' if you would like to loot the {enemy.name}\n"
        "Type 'continue' to continue...:"
        )
    choice = input_validation(choice, "loot", "continue")
    if choice == "loot":
        # some enemys like wolves do not have items in there class
        # try and except is used to insure there are nno issues if
        # a player ties to loot a enemy with no items.
        try:
            for item in enemy.items:
                player_character.items.append(item)
            for weapon in enemy.weapon_inventory:
                player_character.weapon_inventory.append(weapon)
            enemy_weapon_list = weapon_name_list(enemy)
            delay_print(f'{enemy.items} added to your inventory\n')
            delay_print(f'{enemy_weapon_list} added to your weapon inventory\n')
            return player_character
        except AttributeError:
            delay_print(f'{enemy.name} has nothing to loot \n')


def weapon_input_validation(choice, weapon_list):
    """
    this checks what weapons are in the chracrers weapons list
    and validates weapon choice inputed by the player.
    """
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
    """
    uses Pyfiglet lybary to create a
    cool looking banner for the game title.
    """
    banner1 = pyfiglet.figlet_format("Wellcome to")
    banner2 = pyfiglet.figlet_format("Adventure game")
    print(banner1)
    print(banner2)


def get_player_name():
    """
    used to initiat the game and get the players name
    inputted to the player class
    """
    player_character = Player(["fire starter"], "no", "no")
    player_character.name = input("Hello traveller what is your name?: ")
    delay_print(
        f'Well met {player_character.name}!'
        f' Take care on these roads there are goblins on the loose.\n'
    )
    return player_character


def introduction(player_character):
    """
    runs a basic intro for the player.
    """
    delay_print(
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
    """
    runs player through an ambush senario and calls the battle function
    and then if they win calls the hidden_path function
    """
    delay_print(
        "you see an abandoned cart in the road.\n"
        "The cart has been looted\n"
        "you hear a rustling behind you as\n"
        "a goblin charges at you from cover.\n"
    )
    player_character = battle(player_character, Goblin(["chalk", "rabit"]))
    hidden_path(player_character)


def ambush_goblin(player_character):
    """
    The function will run if the player chooses to be stealthy
    when they see the cart in the road.
    """
    delay_print(
        "As you sneak around"
        " you notice a goblin hiding behind a bush watching the road\n"
    )
    choice = input(
        "What would you like to do?\n"
        "Type 'option 1' to attack\nType 'option 2' to sneak past....:\n"
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        player_character = battle(player_character, Goblin(["chalk", "rabit"]))
        hidden_path(player_character)
    if choice == "option2":
        delay_print("you see a hidden trial past the goblin.")
        goblin_cave_entrance(player_character)


def hidden_path(player_character):
    """
    the player is given a chioce to follow a hiden path or go on to town
    """
    delay_print(
        "As you begin to head of down the road "
        "you notice a trail behind the bushes where the goblin was hiding.\n"
    )
    choice = input(
        "Type 'option 1' to follow the hidden path \n"
        "Type 'option 2' to continue down the road to Newtown\n"
        "...: "
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        goblin_cave_entrance(player_character)
    if choice == "option2":
        newtown(player_character)


def goblin_cave_entrance(player_character):
    delay_print(
        "You follow the track for over an hour before you come "
        "to the foot of a large hill."
    )
    delay_print(
        "The track leads up to a hidden cave opening"
    )
    print("")
    choice = input(
        "Type 'option 1' to enter the cave/n"
        "Type 'option 2' to investigate the area"
    )
    choice = input_validation(choice, "option1", "option2")
    if choice == "option1":
        wolf_fight(player_character)
    if choice == "option2":
        sneak_past_wolf(player_character)


def wolf_fight(player_character):
    delay_print(
        "As you enter the cave you notice something pull against your leg\n"
        "as you set of a trip wire. \n"
        "You hear a metallic sound as the alarm sounds….\n"
        "followed by a deep growl coming from the shadows.\n"
        "A wolf leaps out from the darkness and attacks.\n"
    )
    player_character = battle(player_character, Wolf())
    goblin_boss_check(player_character)


def sneak_past_wolf(player_character):
    delay_print(
        "As you look around the entrance you\n"
        "notice a thin wire strung across.\n"
        "You take a closer look and see\n"
        "it's a trip wire that would trigger an alarm\n"
        "you now see in a small alcove just in\n"
        "the cave entrance a sleeping wolf.\n"
    )
    choice = input(
        "Type 'sneak' to sneak past the wolf\n"
        "Type 'attack' to attack the wolf\n: "
        )
    choice = input_validation(choice, "sneak", "attack")
    if choice == "sneak":
        delay_print(
            "you sneak past the wolf in to the cave.\n"
        )
        goblin_boss_check(player_character)
    if choice == "attack":
        delay_print(
            "You attack the wolf"
        )
        wolf_fight(player_character)


def goblin_boss_check(player_character):
    """
    check how the character avived at this point and
    sends them to the correct encounter
    """
    if player_character.newtown == "no":
        goblin_boss_fight(player_character)
    if player_character.newtown == "yes":
        goblin_boss_fight_late(player_character)


def goblin_boss_fight(player_character):
    delay_print(
        "You see a flickering light at the end of the tunnel.\n"
        "As you approach the tunnel bends and opens into a large cavern.\n"
        "There is a large cooking pot boiling what looks like stew\n"
        "on a large fire.\n"
        "A large goblin is currently trying to winch\n"
        "a bound man over and into the cooking pot\n"
        "The goblin looks up to see you and says 'just in time for dinner'\n"
        "as it grins and pulls out its axe.\n"
    )
    choice = input(
        'Fight the Goblin or flee?'
        'Type "fight" to fight or "flee" to flee/n:'
    )
    choice = input_validation(choice, "flee", "fight")
    if choice == "fight":
        player_character = battle(player_character, Goblin_boss())
        player_character.cave = "clear"
        delay_print(
            "You have slain to mighty goblin leader and saved the merchant!"
            "You escort the merchant and his wears back to new town."
        )
        newtown(player_character)
    if choice == "flee":
        delay_print("You flee the cave and head straight to Newtown")
        player_character.cave = "fled"
        newtown(player_character)


def goblin_boss_fight_late(player_character):
    delay_print(
        "You see a flickering light at the end of the tunnel.\n"
        "As you approach the tunnel bends and opens into a large cavern.\n"
        "There is a large empty cooking pot with what looks like\n"
        "human bones next to it\n"
        "A large goblin is currently rubbing its belly\n"
        "The goblin looks up to see you and says\n"
        "'looks like you missed dinner'\n"
        "as it grins and pulls out its axe.\n"
    )
    choice = input(
        'Fight the Goblin or flee?'
        'Type "fight" to fight or "flee" to flee/n:'
    )
    choice = input_validation(choice, "flee", "fight")
    if choice == "fight":
        player_character = battle(player_character, Goblin_boss())
        player_character.cave = "clear_late"
        delay_print(
            "You have slain to mighty goblin leader and saved the merchant!"
            "You escort the merchant and his wears back to new town."
        )
        newtown(player_character)
    if choice == "flee":
        delay_print("You flee the cave and head straight to Newtown")
        player_character.cave = "fled"
        newtown(player_character)


def newtown(player_character):
    delay_print(
        "Through the trees you see a small town of about two dozen buildings\n"
        "surrounded by a 7ft wooden wall the gate lies open.\n"
    )
    if player_character.cave == "no":
        newtown_no_cave(player_character)
    if player_character.cave == "fled":
        newtown_fled_cave(player_character)
    if player_character.cave == "clear":
        ending(player_character)
    if player_character.cave == "late_clear":
        ending(player_character)


def newtown_no_cave(player_character):
    delay_print(
        "As you  draw level with the gates a guard approaches.\n"
        "'Hail stranger “have you seen a merchant on the road?'\n"
        "'He was meant to arrive yesterday\n"
        "and we are in desperate need of supplies.\n'"
        "You: 'there was a abandoned cart on the road\n"
        "with a goblin watching it from, the bushes'.\n"
        "guard: 'You look like your capable would you investigate\n"
        "'and bring the merchant and his goods back for us?'\n"
    )
    choice = input(
        "Type: 'investigate' to go back to the cart in the road\n"
        "and investigate\n"
        "Type: 'stay' to give directions and stay in safe in town"
    )
    choice = input_validation(choice, "investigate", "stay")
    if choice == "stay":
        delay_print(
            "Guard: 'ok thanks for the information \n"
            "we will deal with it from here.'\n"
        )
        player_character.newtown = "stay"
        ending(player_character)
    if choice == "investigate":
        delay_print(
            "Guard: 'Thanks for helping \n"
            "we will pray for your speedy return' \n"
        )
        delay_print(
            "You head back to the cart in the road\n"
            "and follow the hidden trail."
        )
        player_character.newtown = "left"
        goblin_cave_entrance(player_character)


def newtown_fled_cave(player_character):
    delay_print(
        f"As {player_character.name} drew level with the gates\n"
        "a guard approached.\n"
        "'Hail stranger “have you seen a merchant on the road?'\n"
        "'He was meant to arrive yesterday\n"
        "and we are in desperate need of supplies.\n'"
        "You: 'there was a abandoned cart on the road\n"
        "with a goblin watching it from, the bushes'.\n"
        "and tracks that led to a cave.\n"
        "it look like the goblins where going to eat him\n"
        "guard: 'You look like you had a fright we will take it from here"
    )
    ending(player_character)


def ending(player_character):
    """
    checks how the player completed the game a
    nd gives them the apropriate ending.
    """
    if player_character.cave == "clear":
        ending_one(player_character)
    if player_character.cave == "fled":
        ending_two(player_character)
    if player_character.newtown == "stay":
        ending_three(player_character)
    if player_character.cave == "late clear":
        ending_four(player_character)


def ending_one(player_character):
    """
    the player will get this ending if they clear the
    cave before reaching newtown.
    """
    delay_print(
        "The guards see you enter the city with the merchant in tow.\n"
        "They see that you are battered and bruised and take you to\n"
        "the Wayfaring Inn to rest up.\n"
        "By the next morning the guard had gathered the much need goods\n"
        "from cave and seen that the merchant was looked after.\n"
        f"{player_character.name} was named hero in the town and \n"
        "offered a job as defender of the town.\n"
        "This came with a proper massive sward and Armor\n"
        "so you naturally accept./n"
        "its at that point fully clad as the towns defender\n"
        "that a mighty raw echoes across the town\n"
        "and a dragon flies over head.\n"
        f"The towns people looked to {player_character.name}\n"
        "there new defender……….\n"
        "'fu@#'"
        )
    play_again(player_character)


def ending_two(player_character):
    delay_print(
        f"The guards see {player_character.name} enter the town and asks\n"
        "if you have seen a merchant on the road\n"
        f"{player_character.name} tells the gurads what he saw in the cave\n"
        F"{player_character.name} is thanked for their help and offered\n"
        "a job as a scout for the town\n"
        f"Naturally {player_character.name} takes the job as they get\n"
        "a cool spear and armor\n"
        "While out on their first scouting mission"
        "they see a large dragon fly past\n"
        "And descend on the town"
        f"{player_character.name}: 'best give it an hour before I head back'"
    )
    play_again(player_character)


def ending_three(player_character):
    delay_print(
        f"{player_character.name} gets a job as a messanger in town.\n"
        "As they leave to deliver thire first message\n"
        "they see a large dragon desend on the town.\n"
        f"{player_character.name}: 'glad i didnt get that guard job!'"
    )
    play_again(player_character)


def ending_four(player_character):
    """
    the player will get this ending if they clear the
    cave before after leaving new town.
    """
    delay_print(
        f"The guards see {player_character.name} enter the city.\n"
        "They see that they are battered and bruised and take them to\n"
        "the Wayfaring Inn to rest up.\n"
        "By the next morning the guards had gathered the much need goods\n"
        "from cave.\n"
        f"{player_character.name} was named given a job \n"
        "as a town guard\n"
        "This came with a good pay and standard guard gear\n"
        "so you naturally accept./n"
        "it's at that point on your first guard shift\n"
        "that a mighty raw echoes across the town\n"
        "and a dragon flies over head.\n"
        "The towns people cry for the gaurds to do somthing"
        "there new defender……….\n"
        "'fu@#'"
        )
    play_again(player_character)


def play_again(player_character):
    """
    give the player the choice to play again or quit.
    """
    choice = input(
        f"{player_character.name}'s adventure has ended.\n"
        "Would you play again?\n"
        "Type 'yes' to play again "
        "or Type 'no' to quit...:"
    )
    choice = input_validation(choice, "yes", "no")
    if choice == "yes":
        main()
    if choice == "no":
        quit_game(player_character)


def player_death(player_character):
    """
    This function should be called when ever the player dies.
    It gives them the option to play again or quit the game.
    """
    delay_print(f'{player_character.name} has died!')
    play_again(player_character)


def quit_game(player_character):
    """
    This function should only be run when the player
    has chosen to end the game.
    It simply prints a message to the player once they decid to end the game.
    """
    delay_print(
        f"It is with a heavy heart I bid the fairwell {player_character.name}"
        "I hope to see you again one day on a new adventure!"
        )


def main():
    banner()
    player_character = get_player_name()
    introduction(player_character)


main()

# def test_bench():
#     player_character = Player(["fire starter"])
#     goblin_boss_fight(player_character)
#     print("wining")

# test_bench()