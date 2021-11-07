class Entity:
    def __init__(self, health, attack, name):
        self.health = health
        self.attack = attack
        self.name = name

class Player(Entity):
    def __init__(self, weapon, items):
        Entity.__init__(self, 10, 3, "player")
        self.weapon = weapon
        self.items = items


dave = Player("knife", ["bread", "clothes"])

print("daves weapin", dave.weapon)
print("daves items", dave.items)
print("daves health is", dave.health)

dave.weapon = "sword"
print("daves new weapon is", dave.weapon)