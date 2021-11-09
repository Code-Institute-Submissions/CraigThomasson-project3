class Entity:
    def __init__(self, hp, attack, name, weapon):
        self.hp = hp
        self.attack = attack
        self.name = name
        self.weapon = weapon

class Player(Entity):
    def __init__(self, items):
        Entity.__init__(self, 10, 3, "Player", "Rusty Knife")
        self.items = items

class Goblin(Entity):
    def __init__(self, items):
        Entity.__init__(self, 5, 2, "Goblin", "scimatar")
        self.items = items
        items = []

class Goblin_archer(Goblin):
    def __init__(self):
        Goblin.__init__(self, [])

def get_player_name():
    player_characrer = Player(["fire starter", "spare clothes"])
    player_characrer.name = input("hello traveller what is your name?")
    print(player_characrer.name)

get_player_name()