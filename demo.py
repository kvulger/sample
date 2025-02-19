import os

def heading():
    """Displays the game heading and instructions."""
    print("GUESSING GAME")
    print("""
         
            Welcome to the guessing game
                Instructions:
                Help == 0
                Start == 1
                Stop == 2
    """)

def user_input():
    """Gets user input for the game action (Help, Start, or Stop)."""
    return int(input("Enter the Game key (0 for Help, 1 to Start, 2 to Stop): "))

def game():
    """Handles the core of the guessing game logic."""
    secret_number = int(input("Enter The number: "))
    if 19 <= secret_number <= 25:
        print("Congratulations! You won the prize!")
    else:
        print("try again.")

def display_help():
    """Displays help instructions."""
    print("""
         
            Welcome to the guessing game 
                Instructions:
                Help == 0
                Start == 1
                Stop == 2
    """)

def main():
    """Main function to control the flow of the game."""
    heading()
    while True:
        action = user_input()
        
        if action == 1:
            print("Starting the game...")
            game()
        elif action == 0:
            print("Opening Help...")
            display_help()
        elif action == 2:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid input. Please check the help by pressing 0.")

if __name__ == "__main__":
    main()
