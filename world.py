# Locations and Map Logic
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def connect(self, direction, location):
        self.connections[direction] = location

    def describe(self):
        return f"{self.name}\n{self.description}"