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
    """
    Intro message
    User's name stored in varable 'name'
    """
    name = input("What's your name?: ")
    return name

def main(): # Main function of the game
    
    name = intro()
    print(f'\nOk, {name}, how are you gonna get out from here?')
    ready = input("Are you ready for this? (yes/no): ")

    if ready.lower() == "yes":
        print("Great! Let's start the adventure.")
        input("Press Enter to beggin...")
        first_challenge()
    
    elif ready.lower() == "no":
        print("Definitely, you're not the right person for this.")
    
    else:
        print("Wrong answer amigo\n")

def first_challenge(): # Snake and Dragon function
    print("\nYou find yourself in a room with 2 different doors..")
    print("\n The first one has a shield with the drawing of a snake hanging over it,")
    print("\n while the second one also displays a similar door with a shield featuring a dragon.")
    choice = input("\nWhich door do you want to open? (snake/dragon): ")

    if choice.lower() == "snake":
        print("\nYou get into a room full of snakes,\nyou also see a sword hanging on the wall.")
        snakes_challenge()
    elif choice.lower() == "dragon":
        print("\nYou get in a room and you find a huge Dragon")
    else:
        print("\nInvalid choice, please try again")
        choice = input("Which door do you want to open? (snake/dragon): ")
    
def snakes_challenge(): #Snake function
    print("\nyou can either: ")
    print("\n Take the sword and fight the snakes, ")
    print("\n..or run away leaving the sword behind ")
    choice = input("What do you want to do? (fight/run): ")

    if choice.lower() == "fight":
        print("\n Unfortunately, there are too many snakes and you get bitten. Game over.")
    elif choice.lower() == "run":
        print("\n You leave the sword behind but you also save your life")
        print("\n You pass a long corridor..\n and you find another door and a magician next to it.")
        magician_challenge()
    else:
        print("\nInvalid choice, please try again")
        choice = input("What do you want to do? (fight/run): ")

def magician_challenge(): #Magician function
    print("What do you want to do now amigo?") 
    print("Talk to the magician or open the door?: ")
    choice = input("(talk/door): ")

    if choice.lower() == "talk":
        print("\n 'Who are you young boy?' asks the magician")
        



if __name__ == "__main__":
    main()

