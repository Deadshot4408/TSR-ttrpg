# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.strength = 10
        self.inventory = []

    def display_stats(self):
        return f"Name: {self.name}\nHealth: {self.health}\nMana: {self.mana}\nStrength: {self.strength}"
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
