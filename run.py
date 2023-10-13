import random

from colorama import Fore, Style, init, deinit

import time

init()

def progressive_print(text, speed=0.05):
    """
    Print text progressively, letter by letter.

    Args:
        text (str): The text to be printed.
        speed (float, optional): The speed at which the letters are printed. 
            Smaller values result in faster printing. Default is 0.05.
    """
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)
    print()


def press_enter_to_continue(message="Press ENTER to continue..."):
    """
    Waits for the user to press ENTER.

    This function will display the specified message and prompt the user to press ENTER.
    It will not accept any other input. If the user presses any other key, an error message
    will be displayed. If the user presses CTRL+C, an error message will be displayed as well.

    Args:
        message (str, optional): The message to display when prompting the user. 
            Defaults to "Press ENTER to continue...".
    """
    while True:
        try:
            user_input = input(message)
            if user_input == "":
                return
            else:
                print("Please press only ENTER.")
        except KeyboardInterrupt:
            print("\nPlease press only ENTER.")

# Add introduction function
def intro():
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    print("@@@ INSIDE THE LABYRINTH @@@")
    print("    @@@@@@@@@@@@@@@@@@@@    ")
    progressive_print(
        "\n...you just wake up,\n\n"
        "its dark in here and you realize that you are inside of a Labyrinth..."
    )
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
    print(f"\nOk, {name}, how are you gonna get out from here?")
    ready_options = ["yes", "no"]
    ready = get_valid_input(ready_options, "Are you ready? (yes/no): ")

    if ready.lower() == "yes":
        print("\nGreat! Let's start the adventure.")
        press_enter_to_continue(message="Press ENTER to continue...")
        first_challenge(name)
    elif ready.lower() == "no":
        print("\nDefinitely, you're not the right person for this.")

def first_challenge(user_name):
    print("\nYou find yourself in a room with 2 different doors..")
    print("The first one has a shield"
          "with the drawing of a snake hanging over it,")
    print(
        "while the second one also displays a similar door" 
        "with a shield featuring a dragon."
    )
    door_options = ["snake", "dragon"]
    choice = get_valid_input(
        door_options, "\nWhich door do you want to open? (snake/dragon): "
    )

    if choice.lower() == "snake":
        print(
            "\nYou get into a room full of snakes,\nyou also see a sword hanging on the wall."
        )
        snakes_challenge(user_name)
    elif choice.lower() == "dragon":
        print("\nYou get in a room and you find a huge Dragon")
        dragons_challenge(user_name)


def dragons_challenge(user_name):
    print(f"\nIt's your lucky day {user_name}, the dragon is sleeping")
    print("\nThere's a long corridor in this room and a shield on the wall")
    shield_options = ["yes", "no"]
    choice = get_valid_input(
        shield_options, "Do you want to take the shield? (yes/no): "
    )

    if choice.lower() == "yes":
        print("\nNow you walk with a shield")
        input("Press ENTER to continue")
        print("\nThe dragon wakes up and starts breathing fire")
        
        press_enter_to_continue("Press ENTER to use the shield")

        print(
            "\nGreat! you stop the fire\nunfortunately the shield is useless now\nbut you save your life"
        )
        input("\nPress ENTER to cross the long corridor")
        jester_challenge(user_name)

    elif choice.lower() == "no":
        input("\n Press ENTER to continue")
        print("\nThe dragon wakes up and starts breathing fire")
        print("\nYou should had take the shield amigo, GAME OVER")


def jester_challenge(user_name):
    print("\nAlmost at the end of the corridor you find a Jester chained to the wall")
    input("Press ENTER to talk to the Jester")
    print("\n'Hi!, who are you amigo?, and why are you bound to those chains?'")
    input("Press ENTER to listen the Jester")
    print(
        "\n'Hi,well..my name doesnt matter and the reason i'm here..\nthat's a long story' says the Jester"
    )
    print("\n'I guess you are looking how to get out from here, right?'")
    input("Press ENTER to answer the Jester")
    print("\n'Yes please, that would be very helpful'")
    input("Press ENTER to listen the Jester")
    print(
        "\n'Ok, at the end of the corridor you'll find 2 doors,\nonly one of them will bring you closer to the exit'"
    )
    print(
        "'The other one will bring you to death'replies the Jester with an anoying smile"
    )
    print(
        "'I can tell you which one is the right one, but for that you have to play a game with me"
    )
    input("Press ENTER to reply the Jester")
    print("\n'Ok, i guess i have nothing to loose'")
    input("Press ENTER to discover the game")
    print(
        "\n'Sweet mate, let's play rock-paper-scissors, i guess you know how, right?'"
    )
    input("Press ENTER to play")

    # Add Rock, Paper, Scissors game
    choices = ["rock", "paper", "scissors"]
    while True:  # Loop in case of a Tie
        jester_choice = random.choice(choices)
        user_choice = get_valid_input(
            choices, "\nChoose: rock, paper, or scissors: "
        ).lower()

        if user_choice:
            print(f"\nYou chose {user_choice}, and the Jester chose {jester_choice}")

            if user_choice == jester_choice:
                print("\nIt's a tie!")
                continue  # Keep the loop to try again

            elif (
                (user_choice == "rock" and jester_choice == "scissors")
                or (user_choice == "scissors" and jester_choice == "paper")
                or (user_choice == "paper" and jester_choice == "rock")
            ):
                print("\nYou win!")
                print(
                    "\nOk mate,once you cross the corridor you have to open the door [2]"
                )
                input("\nPress ENTER to cross the corridor")
                numbered_doors_chalenge(user_name)
                break

            else:
                print("\nYou lose! The Jester is a tricky one.")
                print("Ha Ha Ha, good luck with the labyrinth, you'll need it")
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
    choice = get_valid_input(
        door_option, "\nWhich door do you want to open? ([1]/[2]): "
    )

    if choice == "1":
        print("\nYou opened the door [1], its completely dark")
        input("\nPress ENTER to get in")
        print("Upon entering, there is a leap into the void, and you fall. GAME OVER.")

    elif choice == "2":
        print("\nYou opened the door [2], its completely dark")
        input("\nPress ENTER get in")
        print("\nOnce you enter, a light turns on, illuminating the entire room,")
        print("now you see two paths, one going upstairs another one going downstairs.")
        path_options = ["up", "down"]
        choice = get_valid_input(
            path_options, "\nWhich one are taking amigo? (up/down)"
        )

        if choice.lower() == "up":
            even_odd_challenge(user_name)

        elif choice.lower() == "down":
            print("\nYou go downstairs,")
            print("and another dragon is waiting for you")
            input("\nPress ENTER to continue")
            print("\nSaddly this time you have no shield, flames everywhere")
            print("\nGAME OVER")


def even_odd_challenge(user_name):
    print("\nYou follow the stairs and you get into another room")
    print("\nInside the room there's a guy holding a knife,")
    print("and behind him a door")
    input("\nPress ENTER to listen this guy")
    print("\nHi pal, you almost have it")
    print("but as you can guess i can't let you cross that door,")
    print("at least not without playing a game")
    input("\nPress ENTER to play")
    print("\nlet's play 'even or odd'")
    print("if you win you get the door but if you loose..")
    print("you get the knife, and not as a present\n")

    user_choice = get_valid_input(["even", "odd"], "Choose 'even' or 'odd': ")

    if user_choice == "even":
        print("\nYou've chosen 'even'.")
    elif user_choice == "odd":
        print("\nYou've chosen 'odd'.")
    else:
        print("\nInvalid Choice. This shouldn't happen.")

    # Both players choose a number
    player1_number = int(
        get_valid_input(["1", "2", "3", "4", "5"], "Player 1, choose a number (1-5): ")
    )

    # Ensure that the user's chosen number is between 1 and 5
    while not (1 <= player1_number <= 5):
        print("Please choose a number between 1 and 5.")
        player1_number = int(
            get_valid_input(
                ["1", "2", "3", "4", "5"], "Player 1, choose a number (1-5): "
            )
        )

    player2_number = random.randint(1, 5)
    print(f"Player 2 (Computer) chose {player2_number}.")

    # Both players show fingers
    player1_fingers = player1_number
    player2_fingers = player2_number

    print(f"\nPlayer 1 shows {player1_fingers} fingers.")
    print(f"Player 2 (Computer) shows {player2_fingers} fingers.")

    # Calculate the total
    total_fingers = player1_fingers + player2_fingers

    # Determine the winner
    if (total_fingers % 2 == 0 and user_choice == "even") or (
        total_fingers % 2 != 0 and user_choice == "odd"
    ):
        print(f"\nYou win! The total was {total_fingers}, which is {user_choice}.")
        print("Ok mate, you can open the door")
        print("Good luck with the last challenge")
        input("\nPress ENTER to face the final challenge")
        last_challenge(user_name)

    else:
        print(f"\nYou lose. The total was {total_fingers}, which is not {user_choice}.")
        print("GAME OVER")


def last_challenge(user_name):
    print("\nYou made it, you are almost there amigo")
    print("You find yourself in a room, there's an iron door")
    print("and 5 keys hanging on the wall.")
    print("\nYou have 2 chances to open that door")
    print("but only 1 of those keys open it")
    print("\nIf you open it you'll be free")
    print("but if you don't, you'll get locked in that room forever\n")

    attempts = 0

    while attempts < 2:
        user_choice = get_valid_input(
            ["key1", "key2", "key3", "key4", "key5"],
            "Choose 'key1', 'key2', 'key3', 'key4', 'key5': ",
        )

        # Check if the chosen key is correct
        if user_choice == "key3":
            print("\nCongratulations! You've chosen the correct key.")
            print("You've successfully opened the door and escaped the labyrinth!")
            return  # Exit the function, the game is won

        else:
            print("\nWrong choice! The door remains locked.")
            attempts += 1
            if attempts < 2:
                print(f"You have {2 - attempts} attempt(s) left.")
            else:
                print(
                    "You've used up all your attempts. You are now trapped in the room forever."
                )
                return  # Exit the function, the game is lost


def snakes_challenge(user_name):
    print("you can either: ")
    print("\nTake the sword and fight the snakes,")
    print("\nor run away leaving the sword behind ")
    fight_options = ["fight", "run"]
    choice = get_valid_input(fight_options, "\nWhat do you want to do? (fight/run): ")

    if choice.lower() == "fight":
        print(
            "\nUnfortunately, there are too many snakes and you get bitten. GAME OVER."
        )
    elif choice.lower() == "run":
        print("\nYou leave the sword behind but you also save your life")
        print(
            "\nYou pass a long corridor..\nyou find another door and a magician next to it."
        )
        magician_challenge(user_name)


def door_logic(user_name):
    print("\nThe Magician steps aside and opens the door for you")
    print("\n'Have a nice journey' says the Magician")
    print(
        "\nYou get into another room, there you find 2 different paths\nIt's time to make up your mind again.."
    )
    door_options = ["left", "right"]
    choice = get_valid_input(
        door_options, "\nWhere do you want to go? : (left/right): "
    )

    if choice.lower() == "left":
        input("\nPress ENTER to continue")
        print("\nYou took the longest way amigo")
        input("\nPress again ENTER to continue")
        numbered_doors_chalenge(user_name)
    elif choice.lower() == "right":
        print("\nLooks like you cant get rid of those snakes")
        print("there are way too many and you get bitten. GAME OVER.")


def magician_challenge(user_name):
    talk_to_magician = False

    print("\nWhat do you want to do now amigo?")
    print("Talk to the magician or open the door?: ")
    magician_options = ["talk", "door"]
    choice = get_valid_input(magician_options, "(talk/door): ")

    if choice.lower() == "talk":
        print("\n 'Who are you young boy?' asks the magician")

        while True:
            new_name = input(" ")
            if new_name.lower() == user_name.lower():
                break
            else:
                print(
                    f"\nSorry, but {new_name} doesn't match your original name. Try again."
                )

        print(f"\n ok {new_name}, I guess you don't like the labyrinth, right?")
        print("\n I can help you to get out from here")
        print("\n Do you want to play a little game with me?")
        play_options = ["play", "pass"]
        choice = get_valid_input(play_options, "play/pass: ")

        if choice.lower() == "play":
            print("\nThe magician gives you a dice\n")
            print("\n 'OK, let's do that'")
            print(
                " Throw the daze, if your score is 4 or more I will open a magic door\n which will bring you closer to the exit"
            )
            print(
                " But, if you score less than 4,..well, you won't like that young boy"
            )
            input("\nPress ENTER to roll the dice...")

            dice_roll = random.randint(1, 6)
            print(f"\nYou rolled a {dice_roll}!")

            if dice_roll >= 4:
                print(
                    f"\n CONGRATULATIONS {new_name}, let me open that magic door for you"
                )
                print("The Magician uses his power to open a magic door")
                print("that will bring you straigt to the last challenge")
                input("\nPress ENTER to face the final challenge")
                last_challenge(user_name)

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
