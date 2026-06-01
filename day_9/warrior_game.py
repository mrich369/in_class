class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return f"{self.name} attacks!"
    
    def __str__(self):
        return f"{self.name} (HP: {self.hp})"
    

class Warrior(Character):
    def __init__(self, name, hp, armor):
        super().__init__(name, hp)
        self.armor = armor

    def attack(self):
        return f"{self.name} swings sword!"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Armor: {self.armor}]"


class Mage(Character):
    # magic attacks, mana attribute, attack() costs mana
    def __init__(self, name, hp, mana=30):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self):
        self.mana -= 5
        return f"{self.name} casts a spell!"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Mana: {self.mana}]"


class Healer(Character):
    # restores hp, heal_power attribute, attack() heals allies
    def __init__(self, name, hp, heal_power=100):
        super().__init__(name, hp)
        self.heal_power = heal_power
    
    def attack(self):
        self.heal_power -= 10
        return f"{self.name} heals allies!"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Heal Power: {self.heal_power}]"
    
party = [
    Character("Villager", 50),
    Warrior("Aragon", 120, 25),
    Mage("Gandalf", 80, 100),
    Healer("Elrond", 90, 40)
]

for hero in party:
    print(hero)
    print(hero.attack())
    print(hero)
    print("\n")