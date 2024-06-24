# ConsoleMenu.py

import WarGame

def main():
    while True:
        print("\nCard Game Menu")
        print("1. Play War")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            WarGame.War().play()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

