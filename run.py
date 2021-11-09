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

class goblin_archer(Goblin):
    def __init__(self):
        Goblin.__init__(self, [])

dave = Player(["bread", "clothes"])

print("daves weapon", dave.weapon)
print("daves items", dave.items)
print("daves health is", dave.hp)

dave.weapon = "sword"
print("daves new weapon is a", dave.weapon)
dave.name = input("enter your name:")
print(dave.name)
enemy = goblin_archer()
enemy.weapon = "bow"
print(enemy.weapon)