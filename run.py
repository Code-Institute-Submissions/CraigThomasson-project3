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
        Entity.__init__(self, 5, 2, "Golin")
        self.items = items

class Goblin_archer(Goblin):
    Entity.__init__(self, ["torch", "rotting meat"])
    weapon = "bow"


dave = Player(["bread", "clothes"])

print("daves weapin", dave.weapon)
print("daves items", dave.items)
print("daves health is", dave.health)

dave.weapon = "sword"
print("daves new weapon is a", dave.weapon)