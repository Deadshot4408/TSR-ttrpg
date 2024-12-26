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
            print("Your stats: Health: 100, Mana: 50, Strength: 10")
        elif command == "inventory":
            print("Your inventory is empty")
        elif command == "quit":
            print("Thanks for playing!")
            running = False
        else:
            raise Exception ("Invalid command. Type 'help' to see available commands.")
        
        if __name__ == "__main__":
            main()
        