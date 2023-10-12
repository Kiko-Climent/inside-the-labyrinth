import random
import sys
from colorama import Fore, Style, init, deinit

init()
# Add introduction function
def intro():
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("@@@ INSIDE THE LABYRINTH @@@")
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("\n...you just wake up,\n\n its dark in here and you realize that you are inside of a Labyrinth...")
    name = input("What's your name?: ") 
    return name

# Add function to control all the invalid inputs
def get_valid_input(options, prompt="Please enter a valid choice: "): 
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print("\nInvalid Choice Amigo")

def main():
    name = intro()
    print(f'\nOk, {name}, how are you gonna get out from here?')
    ready_options = ['yes','no']
    ready = get_valid_input(ready_options, "Are you ready for this? (yes/no): ")

    if ready.lower() == "yes":
        print("\nGreat! Let's start the adventure.")
        input("Press ENTER to begin...")
        first_challenge(name)
    elif ready.lower() == "no":
        print("\nDefinitely, you're not the right person for this.")

def first_challenge(user_name):
    print("\nYou find yourself in a room with 2 different doors..")
    print("\nThe first one has a shield with the drawing of a snake hanging over it,")
    print("\nwhile the second one also displays a similar door with a shield featuring a dragon.")
    door_options = ["snake", "dragon"]
    choice = get_valid_input(door_options, "\nWhich door do you want to open? (snake/dragon): ")

    if choice.lower() == "snake":
        print("\nYou get into a room full of snakes,\nyou also see a sword hanging on the wall.")
        snakes_challenge(user_name)
    elif choice.lower() == "dragon":
        print("\nYou get in a room and you find a huge Dragon")
        dragons_challenge(user_name)

def dragons_challenge(user_name):
    print(f"\nIt's your luky day {user_name}, the dragon is sleeping")
    print("\nThere's a long corridor in this room and a shield on the wall")
    shield_options = ["yes", "no"]
    choice = get_valid_input(shield_options, "Do you want to take the shield? (yes/no): ")
    if choice.lower() == "yes":
            print("\nNow you walk with a shield")
            input("\n Press ENTER to continue")
            print("\nThe dragon wakes up and starts breathing fire")
            input("\n Press ENTER to use the shield")
            print("\nGreat! you stop the fire\nunfortunately the shield is useless now\nbut you save your life")
            input("\n Press ENTER to cross the long corridor")
            jester_challenge(user_name)

    elif choice.lower() == "no":
            input("\n Press ENTER to continue")
            print("\nThe dragon wakes up and starts breathing fire")
            print("\nYou should had take the shield amigo, GAME OVER")

def jester_challenge(user_name):
    print("\nAlmost at the end of the corridor you find a Jester chained to the wall")
    input("\nPress ENTER to talk to the Jester")
    print("\n'Hi!, who are you amigo?, and why are you bound to those chains?'")
    input("\nPress ENTER to listen the Jester")
    print("\n'Hi,well..my name doesnt matter and the reason i'm here..\nthat's a long story' says the Jester")
    print("\n'I guess you are looking how to get out from here, right?'")
    input("\nPress ENTER to answer the Jester")
    print("\n'Yes please, that would be very helpful'")
    input("\nPress ENTER to listen the Jester")
    print("\n'Ok, at the end of the corridor you'll find 2 doors,\nonly one of them will bring you closer to the exit'")
    print("\n'The other one will bring you to death'replies the Jester with an anoying smile")
    print("\n'I can tell you which one is the right one, but for that you have to play a game with me")
    input("\nPress ENTER to reply the Jester")
    print("\n'Ok, i guess i have nothing to loose'")
    input("Press ENTER to discover the game")
    print("\n'Sweet mate, let's play rock-paper-scissors, i guess you know how, right?'")
    input("\nPress ENTER to play")

    # Add Rock, Paper, Scissors game
    import random

    choices = ["rock", "paper", "scissors"]
     
    while True:  # Loop in case of a Tie
        jester_choice = random.choice(choices)
        user_choice = get_valid_input(choices, "\nChoose: rock, paper, or scissors: ").lower()

        if user_choice:
            print(f"\nYou chose {user_choice}, and the Jester chose {jester_choice}")

            if user_choice == jester_choice:
                print("\nIt's a tie!")
                continue  # Keep the loop to try again


            elif (user_choice == "rock" and jester_choice == "scissors") or (user_choice == "scissors" and jester_choice == "paper") or (user_choice == "paper" and jester_choice == "rock"):
                print("\nYou win!")
                print("\nOk mate,once you cross the corridor you have to open the door [2]")
                input("\nPress ENTER to cross the corridor")
                numbered_doors_chalenge(user_name)
                break


            else:
                print("\nYou lose! The Jester is a tricky one.")
                print("\nHa Ha Ha Ha, good luck with the labyrinth mate, you will need it")
                input("\nPress ENTER to cross the corridor")
                numbered_doors_chalenge(user_name)
                break

# Add numbered options challenge
def numbered_doors_chalenge(user_name):
    print("\nFinally you made it to get to the end of the corridor")
    print("\nYou find now two doors, the first one with a number [1] on it")
    print("\nThe second one with a number [2] on it")
    print("\nTime to choose again")
    door_option = ["1", "2"]
    choice = get_valid_input(door_option, "\nWhich door do you want to open? ([1]/[2]): ")

    if choice == "1":
        print("\nYou opened the door [1], its completely dark")
        input("\nPress ENTER get in")
        print("Upon entering, there is a leap into the void, and you fall. GAME OVER.")
    
    elif choice == "2":
        print("\nYou opened the door [2], its completely dark")
        input("\nPress ENTER get in")
        print("\nOnce you enter, a light turns on, illuminating the entire room,")
        print("\nnow you see two paths, one going upstairs another one going downstairs")
        path_options = ["up","down"]
        choice = get_valid_input(path_options, "\nWhich one are taking amigo? (up/down)")

        if choice.lower() == "up":
            even_odd_challenge(user_name)

        elif choice.lower() == "down":
            print("\nYou go downstairs")
            print("\nAnother dragon is waiting for you")
            input("\nPress ENTER to continue")
            print("\nSaddly this time you have no shield, flames everywhere")
            print("\nGAME OVER")
            

def even_odd_challenge(user_name):
    print("\nYou follow the stairs and you get into another room")
    print("\nInside the room there's a guy")              



def snakes_challenge(user_name):
    print("\nyou can either: ")
    print("\nTake the sword and fight the snakes,")
    print("\nor run away leaving the sword behind ")
    fight_options = ["fight", "run"]
    choice = get_valid_input(fight_options, "\nWhat do you want to do? (fight/run): ")

    if choice.lower() == "fight":
        print("\nUnfortunately, there are too many snakes and you get bitten. GAME OVER.")
    elif choice.lower() == "run":
        print("\nYou leave the sword behind but you also save your life")
        print("\nYou pass a long corridor..\nyou find another door and a magician next to it.")
        magician_challenge(user_name)


def door_logic(user_name):
    print("\nThe Magician steps aside and opens the door for you")
    print("\n'Have a nice journey' says the Magician")
    print("\nYou get into another room, there you find 2 different paths\nIt's time to make up your mind again..")
    door_options = ["left", "right"]
    choice = get_valid_input(door_options, "\nWhere do you want to go? : (left/right): ")

    if choice.lower() == "left":
        input("\nPress ENTER to continue")
        print("\n You took the longest way 'amigo'")
        input("\nPress again ENTER to continue")
        print("")
    elif choice.lower() == "right":
        print("\n")
       

def magician_challenge(user_name):
    talked_to_magician = False

    print("What do you want to do now amigo?") 
    print("Talk to the magician or open the door?: ")
    magician_options = ["talk", "door"]
    choice = get_valid_input(magician_options, "(talk/door): ")

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
        play_options = ["play", "pass"]
        choice = get_valid_input(play_options, "play/pass: " )

        if choice.lower() == "play":
            print("\nThe magician gives you a dice\n")
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
                print(f"\nOh no! {new_name}, you loose, i hope you like fire young boy")
                input("\n Press ENTER to continue")
                print("\nThe Magician has brought you to the dragon's room")
                dragons_challenge(user_name)

        elif choice.lower() == "pass":
            door_logic(user_name)

    elif choice.lower() == "door":
        door_logic(user_name)

    else:
        print("\nInvalid choice, Please try again")

if __name__ == "__main__":
    main()
