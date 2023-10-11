import random
import sys
from colorama import Fore, Style, init, deinit

init()

def intro():
    """
    Introducing the game and request the user's name
    """
    print(f"{Fore.MAGENTA}    @@@@@@@@@@@@@@@@@@@@    ")
    print("@@@ INSIDE THE LABYRINTH @@@")
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("...you just wake up,\n its dark in here and you realize that you are inside of a Labyrinth...")
    """
    Intro message
    User's name stored in varable 'name'
    """
    name = input("What's your name?: ") # Prompt for user's name
    return name

def main(): # Main function of the game
    
    name = intro()
    print(f'\nOk, {name}, how are you gonna get out from here?')
    ready = input("Are you ready for this? (yes/no): ") # Call the first challenge function

    if ready.lower() == "yes":
        print("Great! Let's start the adventure.")
        input("Press Enter to beggin...")
        first_challenge(name)
    
    elif ready.lower() == "no":
        print("Definitely, you're not the right person for this.")
    
    else:
        print("Wrong answer amigo\n")

def first_challenge(user_name): # Snake and Dragon function
    print("\nYou find yourself in a room with 2 different doors..")
    print("\n The first one has a shield with the drawing of a snake hanging over it,")
    print("\n while the second one also displays a similar door with a shield featuring a dragon.")
    choice = input("\nWhich door do you want to open? (snake/dragon): ")

    if choice.lower() == "snake":
        print("\nYou get into a room full of snakes,\nyou also see a sword hanging on the wall.")
        snakes_challenge(user_name) # Call the snakes challenge
    elif choice.lower() == "dragon":
        print("\nYou get in a room and you find a huge Dragon")
    else:
        print("\nInvalid choice, please try again")
        choice = input("Which door do you want to open? (snake/dragon): ")
    
def snakes_challenge(user_name): #Snake function
    print("\nyou can either: ")
    print("\n Take the sword and fight the snakes, ")
    print("\n or run away leaving the sword behind ")
    choice = input("\nWhat do you want to do? (fight/run): ")

    if choice.lower() == "fight":
        print("\n Unfortunately, there are too many snakes and you get bitten. Game over.")
    elif choice.lower() == "run":
        print("\n You leave the sword behind but you also save your life")
        print("\n You pass a long corridor..\n and you find another door and a magician next to it.")
        magician_challenge(user_name)
    else:
        print("\nInvalid choice, please try again")
        choice = input("What do you want to do? (fight/run): ")





def magician_challenge(user_name): #Magician function
    print("What do you want to do now amigo?") 
    print("Talk to the magician or open the door?: ")
    choice = input("(talk/door): ")

    if choice.lower() == "talk":
        print("\n 'Who are you young boy?' asks the magician")

        while True:
            new_name = input(" ")
            if new_name.lower() == user_name.lower():
                break
            else :
                print(f"\nSorry, but {new_name} doesn't match your original name. Try again.")

        print(f"\n ok {new_name}, i guess you dont like the labyrinth, right?")
        print("\n I can help you to get out from here")
        print("\n Do you want to play a little game with me?")
        choice = input("play/pass: " )

        if choice.lower() == "play":
            print("\n The magician gives you a daze\n")
            print("\n 'OK, let's do that'")
            print("Throw the daze, if your score is 4 or more i will open a magic door\n wich will bring closer to the exit")
            print("But, if you score less than 4,..well, you won't like that young boy")
            input("\nPress ENTER to roll the dice...")

            dice_roll = random.randint(1, 6)
            print(f"\nYou rolles a {dice_roll}!")

            if dice_roll >= 4:
                print(f"\n CONGRATULATIONS {new_name}, let me open that magic door for you")
            
            else:
                print(f"\n Oh no! {new_name}, you loose, i hope you like snakes")
                snakes_challenge(user_name)







if __name__ == "__main__":
    main()

