# Locations class to represent places in the game world
class Location:
    def __init__(self, name, description):
        # Initialize location attributes
        self.name = name
        self.description = description
        self.connections = {}

    def connect(self, direction, location):
        # Connect this location to another in a specified direction
        self.connections[direction] = location

    def describe(self):
        # Return a string representation of the location's description
        return f"{self.name}\n{self.description}"
    