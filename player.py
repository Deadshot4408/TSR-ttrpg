# Player class to represent the player's character and stats
class Player:
    def __init__(self, name):
        # Initialize player attributes
        self.name = name
        self.health = 100
        self.mana = 50
        self.strength = 10
        self.inventory = [] # Start with an empty inventory

    def display_stats(self):
        # Return a string representation of the player's current stats
        return f"Name: {self.name}\nHealth: {self.health}\nMana: {self.mana}\nStrength: {self.strength}"
    
    def add_to_inventory(self, item):
        # Add an item to the player's inventory
        self.inventory.append(item)
