import random
import sys
from colorama import Fore, Style, init, deinit

init()

def intro():
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("@@@ INSIDE THE LABYRINTH @@@")
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("\n...you just wake up,\n\n its dark in here and you realize that you are inside of a Labyrinth...")
    name = input("What's your name?: ") 
    return name

def main():
    name = intro()
    print(f'\nOk, {name}, how are you gonna get out from here?')
    ready = input("Are you ready for this? (yes/no): ")

    if ready.lower() == "yes":
        print("\nGreat! Let's start the adventure.")
        input("Press ENTER to begin...")
        first_challenge(name)
    elif ready.lower() == "no":
        print("\nDefinitely, you're not the right person for this.")
    else:
        print("Wrong answer amigo\n")

def first_challenge(user_name):
    print("\nYou find yourself in a room with 2 different doors..")
    print("\nThe first one has a shield with the drawing of a snake hanging over it,")
    print("\nwhile the second one also displays a similar door with a shield featuring a dragon.")
    choice = input("\nWhich door do you want to open? (snake/dragon): ")

    if choice.lower() == "snake":
        print("\nYou get into a room full of snakes,\nyou also see a sword hanging on the wall.")
        snakes_challenge(user_name)
    elif choice.lower() == "dragon":
        print("\nYou get in a room and you find a huge Dragon")
    else:
        print("\nInvalid choice, please try again")
        choice = input("Which door do you want to open? (snake/dragon): ")

def snakes_challenge(user_name):
    print("\nyou can either: ")
    print("\n Take the sword and fight the snakes, ")
    print("\n or run away leaving the sword behind ")
    choice = input("\nWhat do you want to do? (fight/run): ")

    if choice.lower() == "fight":
        print("\n Unfortunately, there are too many snakes and you get bitten. GAME OVER.")
    elif choice.lower() == "run":
        print("\n You leave the sword behind but you also save your life")
        print("\n You pass a long corridor..\nyou find another door and a magician next to it.")
        magician_challenge(user_name)
    else:
        print("\nInvalid choice, please try again")
        choice = input("What do you want to do? (fight/run): ")


def door_logic(user_name):
    print("\nThe Magician steps aside and opens the door for you")
    print("\n'Have a nice journey' says the Magician")
    print("\nYou get into another room, there you find 2 different paths\nIt's time to make up your mind again..")
    choice = input("\nWhere do you want to go? : (left/right): ")

    if choice.lower() == "left":
        input("\n Press ENTER to continue")
        print("You took the longest way 'amigo'")
        input("\n Press again ENTER to continue")
        print("")
    else:
        print("\nInvalid choice, please try again")
        door_logic(user_name)

def magician_challenge(user_name):
    talked_to_magician = False

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

        print(f"\n ok {new_name}, I guess you don't like the labyrinth, right?")
        print("\n I can help you to get out from here")
        print("\n Do you want to play a little game with me?")
        choice = input("play/pass: " )

        if choice.lower() == "play":
            print("\nThe magician gives you a daze\n")
            print("\n 'OK, let's do that'")
            print(" Throw the daze, if your score is 4 or more I will open a magic door\n which will bring you closer to the exit")
            print(" But, if you score less than 4,..well, you won't like that young boy")
            input("\nPress ENTER to roll the dice...")

            dice_roll = random.randint(1, 6)
            print(f"\nYou rolled a {dice_roll}!")

            if dice_roll >= 4:
                print(f"\n CONGRATULATIONS {new_name}, let me open that magic door for you")
                # Magic door needs to be added

            else:
                print(f"\nOh no! {new_name}, you lose, I hope you like snakes")
                input("\n Press ENTER to continue")
                print("\nThe Magician has brought you again to the snake's room")
                snakes_challenge(user_name)

        elif choice.lower() == "pass":
            door_logic(user_name)

    elif choice.lower() == "door":
        door_logic(user_name)

    else:
        print("\nInvalid choice, Please try again")

if __name__ == "__main__":
    main()
