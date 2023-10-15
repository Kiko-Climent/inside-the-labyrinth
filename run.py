"""
This module contains functions for the labyrinth game.
"""
import random
import time
from colorama import Fore, Style, init, deinit
from art import text2art

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
        print(letter, end="", flush=True)
        time.sleep(speed)
    print()


def press_enter_to_continue(message="Press ENTER to continue..."):
    """
    Waits for the user to press ENTER.

    This function will display the specified message and prompt the user
    to press ENTER. It will not accept any other input. 
    If the user presses any other key, an error message
    will be displayed. If the user presses CTRL+C,
    an error message will be displayed as well.

    Args:
        message to display when prompting the user.
            Defaults to "Press ENTER to continue...".
    """
    while True:
        try:
            user_input = input(message)
            if user_input == "":
                return
            else:
                print(f"{Fore.YELLOW}\nPlease press only ENTER.")
        except KeyboardInterrupt:
            print(f"\nPlease press only ENTER.{Style.RESET_ALL}")


def intro():  # Add introduction function
    
    print("*" * 124)
    result = text2art("\nINSIDE THE LABYRINTH")
    print(result)
    print("*" * 124)
    progressive_print(
        "\n...you just wake up,\n\n"
        "its dark in here and you realize that you are inside of a Labyrinth.."
    )
    name = input(Fore.BLUE + "What's your name?: " + Style.RESET_ALL)
    return name


def get_valid_input(options, prompt="Please enter a valid choice: "):
    """
    Waits for valid user input from a list of options.

    This function prompts the user to enter a choice from a list of options.
    It continues to prompt the user until a valid choice is provided.

    Args:
        options (list): A list of valid choices.
        prompt (str, optional): The message to display when prompting the user.
            Defaults to "Please enter a valid choice: ".

    Returns:
        str: The user's valid input.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print(f"{Fore.YELLOW}\nInvalid Choice Amigo{Style.RESET_ALL}")


def main():
    name = intro()
    progressive_print(f"\nOk, {name}, how are you gonna get out from here?")
    ready_options = ["yes", "no"]
    ready = get_valid_input(
        ready_options, f"{Fore.BLUE}Are you ready? (yes/no): {Style.RESET_ALL}"
    )
    if ready.lower() == "yes":
        progressive_print(
            f'''{Fore.GREEN}
            GREAT! Let's start the Adventure.
            {Style.RESET_ALL}'''
        )
        press_enter_to_continue(message="Press ENTER to continue...")
        first_challenge(name)
    elif ready.lower() == "no":
        progressive_print(
                f"{Fore.RED}\nDefinitely, "
                f"you're not the right person for this.{Style.RESET_ALL}"
        )


def first_challenge(user_name):
    progressive_print("\nYou're standing in a room with two distinct doors.")
    progressive_print(
        "The first one is decorated with a shield bearing a snake emblem,"
    )
    progressive_print(
        "\nwhile the second door "
        "\nfeatures a shield adorned with the image of a dragon."
    )
    door_options = ["snake", "dragon"]
    choice = get_valid_input(
        door_options,
        f"{Fore.BLUE}\nWhich door do you want to open? "
        f"(snake/dragon):{Style.RESET_ALL} ",
    )

    if choice.lower() == "snake":
        progressive_print(
            "\nYou get into a room full of snakes,"
            "\nyou also see a sword hanging on the wall."
        )
        snakes_challenge(user_name)
    elif choice.lower() == "dragon":
        progressive_print("\nYou get in a room and you find a huge Dragon")
        dragons_challenge(user_name)


def dragons_challenge(user_name):
    progressive_print(f"It's your lucky day "
                      f"{user_name}, the dragon sleeps.")
    progressive_print("\nYou also see a long corridor "
                      "and a shield hanging on the wall")
    shield_options = ["yes", "no"]
    choice = get_valid_input(
        shield_options,
        f"{Fore.BLUE}Do you want to take the shield? "
        f"(yes/no): {Style.RESET_ALL}",
    )

    if choice.lower() == "yes":
        progressive_print("\nNow you walk with a shield")
        press_enter_to_continue(message="Press ENTER to continue...")
        progressive_print("\nThe dragon wakes up and starts breathing fire")

        press_enter_to_continue("Press ENTER to use the shield")

        progressive_print(
            f"{Fore.GREEN}\nGREAT! you stop the fire{Style.RESET_ALL}\nsaddly"
            " the shield is useless now, "
            "but you save your life\n"
        )
        press_enter_to_continue(message="Press ENTER "
                                        "to cross the long corridor")
        jester_challenge(user_name)

    elif choice.lower() == "no":
        press_enter_to_continue(message="\nPress ENTER to continue")
        progressive_print(
            f"\n{Fore.RED}The dragon wakes up and "
            f"starts breathing fire{Style.RESET_ALL}"
        )
        progressive_print(
            f"{Fore.RED}You should had taken the shield amigo,"
            f"\nGAME OVER{Style.RESET_ALL}"
        )


def jester_challenge(user_name):
    progressive_print("\nAlmost at the end of the corridor "
                      "you find a Jester chained to the wall")
    press_enter_to_continue(message="Press ENTER to talk to the Jester")
    print(
        f"{Fore.MAGENTA}\n'Hi!, who are you amigo?, and why are you bound "
        f"to those chains?'\n{Style.RESET_ALL}"
    )
    press_enter_to_continue(message="Press ENTER to listen the Jester")
    progressive_print(
        f"{Fore.MAGENTA}\n'Hi,well..my name doesnt matter "
        f"and the reason i'm here..\nthat's a long story' "
        f"{Style.RESET_ALL}, says the Jester"
    )
    progressive_print(f"{Fore.MAGENTA}\n'I guess you are looking how"
                      " to get out from here, right?'")
    progressive_print(
        "\n'At the end of the corridor you'll find 2 doors,"
        "\nonly one of them will bring you closer to the exit'"
    )
    progressive_print(
        f"\n'The other one will bring you to death'{Style.RESET_ALL},"
        " replies the Jester with an anoying smile."
    )
    progressive_print(
        f"{Fore.MAGENTA}'I can tell you which one is the right one, "
        f"but for that you have to play a game with me.'{Style.RESET_ALL}\n"
    )
    press_enter_to_continue(message="Press ENTER to discover the game")
    progressive_print(
        f"{Fore.MAGENTA}\n'Sweet mate, let's play rock-paper-scissors, i guess you know how, right?'\n{Style.RESET_ALL}"
    )
    press_enter_to_continue(message="Press ENTER to play")

    # Add Rock, Paper, Scissors game
    choices = ["rock", "paper", "scissors"]
    while True:  # Loop in case of a Tie
        jester_choice = random.choice(choices)
        user_choice = get_valid_input(
            choices, f"{Fore.BLUE}\nChoose: rock, paper, or scissors: {Style.RESET_ALL}"
        ).lower()

        if user_choice:
            progressive_print(f"\nYou chose {user_choice}, and the Jester chose {jester_choice}")

            if user_choice == jester_choice:
                print(f"{Fore.YELLOW}\nIT'S A TIE{Style.RESET_ALL}")
                continue  # Keep the loop to try again

            elif (
                (user_choice == "rock" and jester_choice == "scissors")
                or (user_choice == "scissors" and jester_choice == "paper")
                or (user_choice == "paper" and jester_choice == "rock")
            ):
                print(f"{Fore.GREEN}\nYOU WIN!{Style.RESET_ALL}")
                progressive_print(
                    f"{Fore.MAGENTA}\n'Ok mate,once you cross the corridor you have to open the door [2]'{Style.RESET_ALL}"
                )
                press_enter_to_continue(message="\nPress ENTER to keep walking")
                numbered_doors_chalenge(user_name)
                break

            else:
                print(
                    f"{Fore.RED}\nYOU LOSE! "
                    f"The Jester is a tricky one.{Style.RESET_ALL}"
                )
                progressive_print(
                    f"{Fore.MAGENTA}'Ha Ha Ha, good luck with the labyrinth, "
                    f"you'll need it'{Style.RESET_ALL}"
                )
                press_enter_to_continue(
                    message="\nPress ENTER to keep walking")
                numbered_doors_chalenge(user_name)
                break


# Add numbered options challenge
def numbered_doors_chalenge(user_name):
    progressive_print("\nFinally you made it "
                      "to the end of the corridor")
    progressive_print("\nYou find now two doors, "
                      "the first one with a number [1] on it")
    progressive_print("The second one with a number [2] on it")
    progressive_print("\nTime to choose again")
    door_option = ["1", "2"]
    choice = get_valid_input(
        door_option,
        f"{Fore.BLUE}Which door do you want to open?"
        f"([1]/[2]): {Style.RESET_ALL}",
    )

    if choice == "1":
        print("\nYou opened the door [1], its completely dark")
        press_enter_to_continue(message="\nPress ENTER to get in")
        progressive_print(f"{Fore.RED}There is a leap into the void, "
                          f"and you fall.\nGAME OVER.{Style.RESET_ALL}")

    elif choice == "2":
        print("\nYou opened the door [2], its completely dark")
        press_enter_to_continue(message="\nPress ENTER get in")
        progressive_print("\nOnce you enter, a light turns on, "
                          "illuminating the entire room,")
        progressive_print("now you see two paths, one going upstairs "
                          "another one going downstairs.")
        path_options = ["up", "down"]
        choice = get_valid_input(
            path_options, f"{Fore.BLUE}\nWhich one are taking?"
                          f" (up/down): {Style.RESET_ALL}"
        )

        if choice.lower() == "up":
            even_odd_challenge(user_name)

        elif choice.lower() == "down":
            progressive_print("\nYou go downstairs,")
            progressive_print("and another dragon is waiting for you")
            press_enter_to_continue(message="\nPress ENTER to continue...")
            progressive_print(
                f"{Fore.RED}\nSaddly this time you have"
                f" no shield, flames everywhere")
            print(f"\nGAME OVER{Style.RESET_ALL}")


def even_odd_challenge(user_name):
    progressive_print("\nYou follow the stairs and you get into another room.")
    progressive_print("\nInside the room there's a guy holding a knife,")
    progressive_print("and behind him a door.")
    press_enter_to_continue(message="\nPress ENTER to listen to this guy")
    progressive_print(f"{Fore.MAGENTA}\nHi pal, you almost have it")
    progressive_print("but as you can guess i can't let you cross that door,")
    progressive_print(f"at least not without playing a game{Style.RESET_ALL}")
    press_enter_to_continue(message="\nPress ENTER to play")
    print(f"{Fore.MAGENTA}\n'let's play 'even or odd'")
    print("if you win you get the door but if you loose..")
    print(f"you get the knife, and not as a present\n{Style.RESET_ALL}")

    user_choice = get_valid_input(
        ["even", "odd"], f"{Fore.BLUE}Choose 'even' or 'odd': "
                         f"{Style.RESET_ALL}")

    if user_choice == "even":
        progressive_print("\nYou've chosen 'even'.")
    elif user_choice == "odd":
        progressive_print("\nYou've chosen 'odd'.")
    else:
        print(f"{Fore.YELLOW}\nInvalid Choice.{Style.RESET_ALL}")

    # Both players choose a number
    player1_number = int(
        get_valid_input(
            ["1", "2", "3", "4", "5"], 
            "Player 1, "
            f"{Fore.BLUE}choose a number (1-5): {Style.RESET_ALL}")
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
        print(f"\nYOU WIN! The total was {total_fingers}, which is {user_choice}.")
        print("Ok mate, you can open the door")
        print("Good luck with the last challenge")
        press_enter_to_continue(message="\nPress ENTER to face the final challenge")
        last_challenge(user_name)

    else:
        print(f"\nYOU LOSE. The total was {total_fingers}, which is not {user_choice}.")
        print("GAME OVER")


def last_challenge(user_name):
    progressive_print("\nYou made it, you are almost there amigo")
    progressive_print("You find yourself in a room, there's an iron door")
    progressive_print("and 5 keys hanging on the wall.")
    progressive_print("\nYou have 2 chances to open that door")
    progressive_print("but only 1 of those keys open it")
    progressive_print("\nIf you open it you'll be free")
    progressive_print("but if you don't, you'll get locked in that room forever\n")

    attempts = 0

    while attempts < 2:
        user_choice = get_valid_input(
            ["key1", "key2", "key3", "key4", "key5"],
            "Choose 'key1', 'key2', 'key3', 'key4', 'key5': ",
        )

        # Check if the chosen key is correct
        if user_choice == "key3":
            progressive_print(f"{Fore.GREEN}\nCONGRATULATIONS! "
                              "You've chosen the correct key.")
            progressive_print("You've successfully opened"
                              f"the door and escaped the labyrinth!"
                              f"{Style.RESET_ALL}")
            return  # Exit the function, the game is won

        else:
            progressive_print(f"{Fore.RED}\nWrong choice!"
                              f"The door remains locked.{Style.RESET_ALL}")
            attempts += 1
            if attempts < 2:
                print(f'{Fore.YELLOW}\nYou have {2 - attempts} attempt(s) left.{Style.RESET_ALL}')
            else:
                progressive_print(
                    f"{Fore.RED}\nYou've used up all your attempts."
                    f"You are now trapped in the room forever."
                    f"GAME OVER{Style.RESET_ALL}"
                )
                return  # Exit the function, the game is lost


def snakes_challenge(user_name):
    progressive_print("you can either: ")
    progressive_print("\nTake the sword and fight the snakes,")
    progressive_print("or run away leaving the sword behind ")
    fight_options = ["fight", "run"]
    choice = get_valid_input(
        fight_options, f'{Fore.BLUE}\nWhat do you want to do? (fight/run): '
                       f'{Style.RESET_ALL}')

    if choice.lower() == "fight":
        progressive_print(
            f"{Fore.RED}\nUnfortunately, there are too many snakes"
            f"\nand you get bitten. GAME OVER.{Style.RESET_ALL}"
        )
    elif choice.lower() == "run":
        progressive_print("\nYou leave the sword behind but you also save your life")
        progressive_print(
            "\nYou pass a long corridor..\nyou find another door and a magician next to it."
        )
        magician_challenge(user_name)


def door_logic(user_name):
    print("\nThe Magician steps aside and opens the door for you")
    print(f"{Fore.MAGENTA}\n'Have a nice journey'{Style.RESET_ALL}"
           " says the Magician")
    print(
        "\nYou get into another room, there you find 2 different paths\nIt's time to make up your mind again.."
    )
    door_options = ["left", "right"]
    choice = get_valid_input(
        door_options, "\nWhere do you want to go? : (left/right): "
    )

    if choice.lower() == "left":
        press_enter_to_continue(message="\nPress ENTER to continue...")
        print("\nYou took the longest way amigo")
        press_enter_to_continue(message="\nPress again ENTER to continue")
        numbered_doors_chalenge(user_name)
    elif choice.lower() == "right":
        print("\nLooks like you cant get rid of those snakes")
        print("there are way too many and you get bitten. GAME OVER.")


def magician_challenge(user_name):
    
    progressive_print("\nWhat do you want to do now amigo?")
    print("Talk to the magician or open the door?: ")
    magician_options = ["talk", "door"]
    choice = get_valid_input(
        magician_options, f"{Fore.BLUE}(talk/door): "
                          f"{Style.RESET_ALL}")

    if choice.lower() == "talk":
        progressive_print(f"{Fore.MAGENTA}\n'Who are you young boy?,'{Style.RESET_ALL}"
                          f" asks the magician\n")

        while True:
            new_name = input(" ")
            if new_name.lower() == user_name.lower():
                break
            else:
                print(
                    f"{Fore.YELLOW}\nSorry, but {new_name} doesn't match"
                    f"your original name. Try again.\n{Style.RESET_ALL}"
                )

        progressive_print(f"{Fore.MAGENTA}\n'ok {new_name},"
                           "I guess you don't like the labyrinth, right?")
        progressive_print("I can help you to get out from here")
        progressive_print(f"Do you want to play a little game with me?'")
        play_options = ["play", "pass"]
        choice = get_valid_input(play_options, f"{Fore.BLUE}(play/pass): "
                                               f"{Style.RESET_ALL}")

        if choice.lower() == "play":
            progressive_print("\nThe magician gives you a dice\n")
            print(f"{Fore.MAGENTA}\n'OK, let's do that'\n")
            progressive_print(
                f"'Throw the daze, if your score is 4 or more"
                f"\nI will open a magic door "
                f"\nthat will bring "
                f"you closer to the exit'{Style.RESET_ALL}"
            )
            progressive_print(
                f"{Fore.MAGENTA}'But, if you score less than 4,..well,"
                f"\nyou won't like that young boy'{Style.RESET_ALL}"
            )
            press_enter_to_continue(message="\nPress ENTER to roll the dice")

            dice_roll = random.randint(1, 6)
            progressive_print(f"\nYou rolled a {dice_roll}!")

            if dice_roll >= 4:
                progressive_print(
                    f"{Fore.GREEN}\nCONGRATULATIONS {new_name},"
                    f"{Fore.MAGENTA}'let me open that magic door for you'{Style.RESET_ALL}"
                )
                progressive_print("\nThe Magician uses his power to open a magic door")
                progressive_print("that brings you straigt to the last challenge")
                press_enter_to_continue(
                    message="\nPress ENTER to face the final challenge"
                )
                last_challenge(user_name)

            else:
                print(f"{Fore.RED}\nOh no! {new_name}, YOU LOSE"
                      f"{Fore.MAGENTA} 'I hope you like "
                      f"fire young boy'{Style.RESET_ALL}")
                press_enter_to_continue(message="\nPress ENTER to continue...")
                progressive_print("\nThe Magician has brought you to the dragon's room")
                dragons_challenge(user_name)

        elif choice.lower() == "pass":
            door_logic(user_name)

    elif choice.lower() == "door":
        door_logic(user_name)

    else:
        print("\nInvalid choice, Please try again")


if __name__ == "__main__":
    main()
deinit()
