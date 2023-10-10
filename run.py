import random
import sys

def intro():
    """
    Introducing the game and request the user's name
    """
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("@@@ INSIDE THE LABYRINTH @@@")
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("...you just wake up,\n its dark in here and you realize that you are inside of a Labyrinth...")
    # Intro message
    # User's name stored in varable 'name'
    name = input("What's your name?: ")
    return name

def main():
    """
    Main function of the game
    """
    name = intro()
    print(f'\nOk, {name}, how are you gonna get out from here?')
    ready = input("Are you ready for this? (yes/no): ")

    if ready.lower() == "yes":
        print("Great! Let's start the adventure.")
        input("Press Enter to beggin...")
    
    elif ready.lower() == "no":
        print("Definitely, you're not the right person for this.")
    
    else:
        print("Wrong character")

if __name__ == "__main__":
    main()

