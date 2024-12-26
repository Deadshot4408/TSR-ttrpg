# Import required classes from other modules
from player import Player
from world import Location

def main():
    # Introduction to the game
    print("Welcome to The Shattered Realm!")

    # Initialize locations
    # Create the starting town and forest, and connect them
    town = Location("Ashenford", "A peaceful village with green fields.")
    forest = Location("Whispering Woods", "A dark, eerie forest filled with whispers.")
    emberforge = Location("Emberforge Keep", "A ruined fortress surrounded by molten lava and jagged rocks.")
    frozen_wastes = Location("Frozen Wastes", "A desolate tundra with snow and icy winds.")

    # Connecting Locations
    town.connect("north", forest)
    forest.connect("south", town)
    forest.connect("east", emberforge)
    emberforge.connect("west", forest)
    emberforge.connect("north", frozen_wastes)
    frozen_wastes.connect("south", emberforge)

    # Initialize player and starting location
    player_name = input("Enter your character's name: ")
    player = Player(player_name) # Create a Player Object
    print(f"\nGreetings, {player.name}! Your adventure begins...\n")
    current_location = town # Set the starting location

    # Main game loop
    running = True
    while running:
        # Display the current location name and description
        print(f"\nYou are at {current_location.name}")
        print(current_location.describe())  # Show the description of the location

        # Get player input for their next action
        command = input("\nWhat would you like to do? (type 'help' for options): ").strip().lower()

        # Handle various commands
        if command == "help":
            # Display available commands
            print("\nCommands: move <direction>, stats, inventory, map, quit")
        elif command.startswith("move"):
            # Handle movement by extracting the direction
            try:
                direction = command.split(" ")[1]  # Get the second word as the direction
                if direction in current_location.connections:
                    # Update the current location if the direction is valid
                    current_location = current_location.connections[direction]
                    print(f"You move {direction} to {current_location.name}.")
                else:
                    print("You can't go that way!")
            except IndexError:
                # Handle case where the direction is not specified
                print("Specify a direction. Example: move north")
        elif command == "stats":
            # Display the player's current stats
            print(player.display_stats())
        elif command == "inventory":
            # Display the player's inventory
            if not player.inventory:
                print("Your inventory is empty.")
            else:
                print("Your inventory:", ", ".join(player.inventory))
        elif command == "map":
            print("\nMap of the area:")
            for direction, location in current_location.connections.items():
                print(f"{direction.title()}: {location.name}")
        elif command == "quit":
            # Exit the game
            print("Thanks for playing!")
            running = False
        else:
            # Handle invalid commands
            print("Invalid command. Type 'help' to see available commands.")

        if current_location.name == "Whispering Woods":
            print("You hear strange whispers around you... Something might be hidden here.")
            if "Ancient Chest" not in player.inventory:
                print("You find an Ancient Chest!")
                player.add_to_inventory("Ancient Chest")
        elif current_location.name == "Emberforge Keep":
            print("The heat from the molton lava makes it hard to breathe.")

        if current_location.name == "Emberforge Keep":
            if "Fire-Resistance Cloak" not in player.inventory:
                print("The heat is unbearable! You cannot explore further without a Fire-Resistance Cloak.")
                current_location = current_location.connections["west"] # Move the player back
            else:
                print("Thanks to the Fire-Resistance Cloak, you can explore further.")
            


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
