from player import Player

def main():
    print("Welcome to The Shattered Realm!")
    running = True

    while running:
        command = input("\nWhat would you like to do? (type 'help' for options): ").strip().lower()

        if command == "help":
            print("\nCommands: move, stats, inventory, quit")
        elif command == "move":
            print("You move to a new location.")
        elif command == "stats":
            print(f"Your stats: Health: {player.health}, Mana: {player.mana}, Strength: {player.strength}")
        elif command == "inventory":
            if not player.inventory:
                print("Your inventory is empty")
            else:
                print(player.inventory)
        elif command == "quit":
            print("Thanks for playing!")
            running = False
        else:
            raise Exception ("Invalid command. Type 'help' to see available commands.")
        

        player_name = input("Enter your character's name: ")
        player = Player(player_name)
        print(f"\nGreetings, {player_name}! Your adventure begins...\n")

        if __name__ == "__main__":
            main()
        