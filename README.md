# INSIDE THE LABYRINTH

**Inside the labyrinth** is a _Python terminal game_ running in the Code Institute mock terminal from Heroku.

The User has to escape from a virtual labyrinth, in the search for the exit, the user will interact with the computer, which will put the user to the test through different challenges, including decision-making and games of chance.


![Mock Up](/media/mockup.png)


[Live Version of the project](https://inside-the-labyrinth-d3a038d774c6.herokuapp.com/)

## HOW TO PLAY?

After a small introduction, the computer instance the User to introduce the name that will use for this adventure.

After introducing user’s name, the computer will double check if the user is ready to start, and then the game will start.

During the process towards finding the exit, the user will encounter various _interactions with the computer._ **Decision-making** will be the most recurring challenge in the game. For example, choosing doors, paths, or using objects. In each decision-making instance, one of the options will allow the user to continue playing, while the other option will either delay the path to the maze's exit or defeat them directly.

The user will also face some **Games of chance**, such as 'Even or Odd' or 'Rock-Paper-Scissors'. Just like with the decision-making challenges, the user's luck will determine whether he encounters more obstacles before reaching the exit."

If the user achieves to pass all the challenges will win the game, and will set free from the Labyrinth.

## DESIGN:

I used an **_ASCII art_** library to create the main header. To add a bit more dynamism to the story, I also used the **_Colorama_** library to change the color of some texts.

- **WHITE:** Used for narrating the story.
- **BLUE:** It is used in the game for selecting options in the different challenges that the user faces. 
- **GREEN:** Used to emphasize when the user has successfully overcome a trial.
- **RED:** Used when the user fails to defeat a challenge.
- **MAGENTA:** Used when there is an interaction between the user and a character in the labyrinth.
- **YELLOW:** Finally, in yellow, we find the warnings, such as when the user enters an invalid field.

## FEATURES:

### Existing Features:

**1 - Introduction:**
After entering our username, the computer will ask us if we are truly prepared for the challenge of escaping the maze; in case the answer is negative, the game will end instantly.

![Intro](/media/intro2.png)

**2 - First Challenge:**
The first decision the user will have to make is the path to follow. Here, two paths will be presented to us: the path of the snake or the path of the dragon. Depending on the choice, the user will face different challenges.

![First Challenge](/media/first_challenge.png)

**3 - The Dragon’s Challenge:**
If we choose the path of the dragon, we will encounter another decision to make. Whether to take the shield or, on the contrary, leave it. The dragon will awaken whether we take the shield or not, so if we leave it on the wall, the game will end.

![Dragon Challenge](/media/dragon-challenge.png)

**4 - The Jester Challenge:**
If we successfully pass the Dragon’s Challenge, the new challenge the user will face is the “Jester”. The jester will offer us assistance with the next challenge only if we play a game of chance. In this case, the jester challenges us to play 'Rock, Paper, Scissors'. In case of losing, the game will not end, but we will not receive the clue to pass the next challenge.

![Jester Challenge](/media/jester-challenge.png)

**5 - The Numbered Door Challenge:**
Once we have left the jester behind, we will encounter a new choice of doors, this time labeled as 1 and 2. If we manage to defeat the jester beforehand, we will have no difficulty in knowing which one will lead us to the next challenge, as one of the two contains a deadly trap.

![Numbered Doors Challenge](/media/door-challenge.png)

If we choose wisely, another decision lies ahead of us: to choose whether to go up the stairs or down them. Just like in the previous door choice, one of the paths leads to a deadly trap.

**6- The Even Odd Challenge:**
If we manage to outsmart death twice in a row, the labyrinth will lead us to another character in the story. A kind of guardian-executioner who will urge us to play 'odds or evens.' This way, chance will determine whether we continue searching for the exit or, on the contrary, end the game.

![Even Odd](/media/even-odd.png)

**7- The Last Challenge:**
If the user manages to defeat the guardian, they will face the final challenge. In it, we find ourselves in a room with an iron door, and we must open that door to exit the maze. We will be given 5 keys for this task. Only one of them unlocks the door, and we have 2 attempts to open it.

![Key Challenge](/media/last-challenge.png)

**8- The Snake Challenge:**
In the oder hand, if you decide to open the Snake’s door, we will have to make up our mind and decide if we take the sword hanging on the wall to fight the snakes on that room or if we decide to run and leave the sword behind. This decision will be capital to keep alive in the labyrinth.

![Snake Chalenge](/media/snake.png)

**9- The Magician Challenge:**
If we still alive another challenge will be in front of us. The caracter of a Magician interacts with the user if the user wants to. In this case, the magician will request again the user’s name and then will invite us to play a game with a huge reward. We will have to throw a dice and depending on our score the user will, either end up at the dragon’s room or facing the last challenge. If the user’s option is to take the door instead interacting with the Magician, this door will bring him to another room full of snakes and the game will finish.

![Magician Challenge](/media/magician-challenge.png)

### Future Features:

I was thinking about implementing new thigs to the game. A new path with new challenges and characters, would make the game a bit more complicated and therefor funnier.

Also i was thinking about implementig a new functionality to the _ENTER_ key, since i added the _progressive print function_, i think it would be great that if the user doesn't want to wait for the strings to be printed, a good functinality would be to give the optio of printing the whole string if the user press _ENTER_ while the statement is getting printed. I think this functionality would increase the quality of the user's experience.

New challenges like, _"The Hangman"_ or _"Guessing a number"_ would be also implemented in the game.

I also would like to add a _timer_ in order to make it a bit more challenging. To set a timer for 3 or 4 minutes and challenge the user to complete the labyrinth before time runs out. It could be implemented as _"optional"_, leving this choice to the user.

Along with the addition of the timer, it would also be interesting to gather all those data and create a _Leaderboard_ to see which user has completed the maze in the shortest possible time.

## DATA MODEL:

### User:
- The game starts by asking the user to enter their name.
### Doors:
- At the beginning of the game, the user must choose between two doors: one with a snake and another with a dragon. This choice affects the game's path.
### User Choices:
- Throughout the game, the user makes decisions such as whether they are ready to play, which door to open, whether to take a shield, etc.
### Outcomes of User Choices:
- Depending on the user's choices, they will face different challenges, such as facing snakes, a dragon, a jester, a magician, etc.
### Challenges:
- Challenges are represented by functions like **snakes_challenge**, **dragons_challenge**, **jester_challenge**, **even_odd_challenge**, **numbered_doors_challenge**, etc.
### Game States:
- Game states include whether the user won or lost the game, if they are trapped in a room, etc.

## TECHNOLOGIES USED:

**The programming language** used for the development of _"Inside the Labyrinth"_ has been **_Python_**.

### PROGRAMS AND LIBRARIES USED: ###

- [Gitpod](https://gitpod.io/) - IDE used to create the site.
- [Visual Studio Code](https://code.visualstudio.com/) - IDE used to create the site.
- [Github](https://github.com/) - To save and store the files for the website.
- [Heroku](https://heroku.com/) - To deploy the project.
- [Colorama Library](https://pypi.org/project/colorama/) - To add colors to the project.
- [Art Library](https://pypi.org/project/art/) - To add the Ascii Art for the header.
- [Random Library](https://docs.python.org/3/library/random.html) - To add a random number in some challenges.
- [Time Library](https://docs.python.org/3/library/time.html) - Used to create the _progressive print_ letter by letter.
- [Black library](https://pypi.org/project/black/) - To format the code.
- [W3SChools](https://www.w3schools.com/python/default.asp) - Was a good help to develope my code
- [ChatGPT](https://chat.openai.com/) - Helped me rephrasing part of the story and also was a great tool to understand some concepts.

## TESTING:

The project was manually tested by doing:
- The code was passed through **_PEP8_** and confirmed there are no problems.

![PEP8](/media/pep8-Validator.png)

- Some valid inputs were giving: I need it to _add docstrings_ to some of the functions of the game. I also had many _lines that were too long_, more than 79 characters. Encounter also that some _blanklines contained whitespaces._
- Tested in the _Code Institute Heroku terminal_ and in my local terminal.

### VALIDATOR TESTINGS:

- **PEP8**
No errors were returned from Pep8online.com

### MANUAL VALIDATION:

- **INTRODUCTION:**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User's Name Request | Accept User's Name (letters/numbers) | Introduced a Name | Username Accepted / Welcome message | Pass
| Readiness Check "yes" | Prompt "Are you ready? (yes/no) displayed | Entered "yes" | GREAT! Let's start the Adventure. | Pass
| Readiness Check "no" | Prompt "Are you ready? (yes/no) displayed | Entered "no" | Definitely, you're not the right person for this. | Pass
| Readiness Check "Invalid Input" | Prompt "Are you ready? (yes/no) displayed | Entered "Invalid Input" | Invalid Choice Amigo | Pass

- **FIRST CHALLENGE:**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Door Choice (Snake) | Prompt "Which door do you want to open? (snake/dragon):" displayed | Entered "snake" for test case. | Get in the Dragon's room | Pass |
| Door Choice (Dragon) | Prompt "Which door do you want to open? (snake/dragon):" displayed | Entered "dragon" for test case. | Get in the Snake's room | Pass |
| Door Choice | Prompt "Which door do you want to open? (snake/dragon):" displayed | Entered Ivalid Input. | Invalid Choice Amigo | Pass |

- **SHIELD (DRAGON'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Shield Choice (Yes) | Prompt "Do you want to take the shield? (yes/no):" displayed | Entered "yes" for test case. | CONGRATULATIONS!, you sa | Pass |
| Shield Choice (No) | Prompt "Do you want to take the shield? (yes/no):" displayed | Entered "no" for test case. | GAME OVER | Pass |
| Shield Choice (Invalid Input) | Prompt "Do you want to take the shield? (yes/no):" displayed | Entered "Invalid Inpput" for test case. | Invalid Choice Amigo | Pass |

- **THE JESTER CHALLENGE (DRAGON'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Rock, Paper, Scissors Game (Rock) | Prompt "Choose: rock, paper, or scissors:" displayed | Entered "rock" for test case. | You choose Rock | Pass |
| Rock, Paper, Scissors Game (Paper)    | Prompt "Choose: rock, paper, or scissors:" displayed | Entered "paper" for test case. | You choose Paper | Pass |
| Rock, Paper, Scissors Game (Scissors) | Prompt "Choose: rock, paper, or scissors:" displayed | Entered "scissors" for test case. | You choose scissors | Pass |
| Rock, Paper, Scissors Game (Invalid Input) | Prompt "Choose: rock, paper, or scissors:" displayed | Entered "Invalid Input" for test case. | Invalid Choice Amigo | Pass |

- **NUMBERED DOORS CHALLENGE (DRAGON'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Choosing Door 1 | Prompt "Which door do you want to open?([1]/[2]):" displayed | Entered 1 for test case. | GAME OVER | Pass |
| Choosing Door 2 | Prompt "Which door do you want to open?([1]/[2]):" displayed | Entered 2 for test case. | Next Challenge (up/down) | Pass |
| Choosing Door "Invalid Input" | Prompt "Which door do you want to open?([1]/[2]):" displayed | Entered "Invalid Input" for test case. case. | Invalid Choice Amigo | Pass |

- **GOING UPSTAIRS/DOWNSTAIRS (DRAGON'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Choosing to Go (Up) | Prompt "Which one are you taking? (up/down):" displayed | Entered "up" for test case. | Next Challenge | Pass |
| Choosing to Go (Down) | Prompt "Which one are you taking? (up/down):" displayed | Entered "down" for test case. | GAME OVER | Pass |
| Choosing to Go (Invalid Input) | Prompt "Which one are you taking? (up/down):" displayed | Entered "Invalid Input" for test case. | Invalid Choice Amigo | Pass |

- **EVEN OR ODD CHALLENGE (DRAGON'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Even or Odd Game 'even'| Prompt "Choose 'even' or 'odd':" displayed | Entered "even" for test case. | You've chose 'even' | Pass |
| Even or Odd Game 'odd' | Prompt "Choose 'even' or 'odd':" displayed | Entered "odd" for test case.  | You've chose 'odd' | Pass |
| Even or Odd Game 'Invalid Input' | Prompt "Choose 'even' or 'odd':" displayed | Entered "Invalid Input" for test case.  | Invalid Choice Amigo | Pass |
| Player 1 chooses a number | Prompt "Player 1, choose a number (1-5):" displayed | Entered valid number for test case.   | Player 1 shows "?" fingers. (The number of fingers will depend on the number introduced previously) | Pass |

- **THE LAST CHALLENGE:**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Player chooses a key | Prompt "Choose 'key1', 'key2', 'key3', 'key4', 'key5':" displayed | Entered valid key ('key3') for test case. | YOU WIN! | Pass |
Player chooses a key | Prompt "Choose 'key1', 'key2', 'key3', 'key4', 'key5':" displayed | Entered ('key1', 'key2', 'key4', 'key5',) for test case. | GAME OVER | Pass |
Player chooses a key | Prompt "Choose 'key1', 'key2', 'key3', 'key4', 'key5':" displayed | Entered (Invalid Input) for test case. | Invalid Choice Amigo | Pass |

- **THE SWORD (SNAKE'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Snake's Room | Prompt "Fight or Run?: " displayed | Entered "fight" for test case. | GAME OVER| Pass |
| Snake's Room | Prompt "Fight or Run?: " displayed | Entered "run" for test case. | You save your life! | Pass |
| Snake's Room | Prompt "Fight or Run?: " displayed | Entered "Invalid Input" for test case. | Invalid Choice Amigo | Pass |

- **ENCOUNTER WITH THE MAGICIAN (SNAKE'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Player decides to talk | Prompt "Talk to the magician or open the door?: " displayed | Entered valid choice (e.g., 'talk') for test case. | Challenge: Decision to play or pass | Pass |
| Player decides to open door | Prompt "Talk to the magician or open the door?: " displayed | Entered valid choice (e.g., 'door') for test case. | Challenge: Choose left or right | Pass |
| Player introduces Invalid Input | Prompt "Talk to the magician or open the door?: " displayed | Entered valid Invalid input for test case. | Invalid Choice Amigo | Pass |

- **TALK WITH THE MAGICIAN (SNAKE'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Name matches | Prompt "Who are you young boy?', asks the magician" displayed | Entered matching name provided at the beginning of the game.| Play or Pass Decision | Pass |
| Name does not match | Prompt "Who are you young boy?', asks the magician" displayed | Entered (jiji) different name than the one provided at the beginning. | Sorry, but jiji doesn't matchyour original name. Try again. | Pass |

- **DECISION TO PLAY OR PASS (SNAKE'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| We have to decide if we play with the Magician | Play | Entered Play | The Magician Challenge | Pass |
| We have to decide if we play with the Magician | Pass | Entered Pass | Challenge: Choose left or right | Pass |
| We have to decide if we play with the Magician | Invalid Input | Entered Pass | Invalid Choice Amigo | Pass |


- **THE MAGICIAN CHALLENGE / THE DICE (SNAKE'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Roll Dice (Score >= 4) | Prompt "Roll the dice, if you score 4 or more i'll bring you closer to the exit | Pressed ENTER, rolled dice and obtained a score of 4 or more. | The Final Challenge | Pass |
| Roll Dice (Score < 4) | Prompt "Roll the dice, if you score 4 or more i'll bring you closer to the exit | Pressed ENTER, rolled dice and obtained a score of less than 4. | The Dragon's Challenge | Pass |
| ENTER to roll the dice | Prompt "Press ENTER to roll the dice" | Pressed Enter | Dice Result | Pass |
| ENTER to roll the dice | Prompt "Press ENTER to roll the dice" | Pressed Invalid Input before Enter | Please press only ENTER. | Pass |

- **CHOOSE LEFT PATH OR RIGHT PATH (SNAKE'S PATH):**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Player chooses left | Prompt "Where do you want to go?(left/right): " displayed | Entered valid choice (e.g., 'left') for test case. | Numbered Door Challenge | Pass |
| Player chooses right | Prompt "Where do you want to go?(left/right): " displayed | Entered valid choice (e.g., 'right') for test case. | GAME OVER | Pass |
| Player introduces Invalid Input | Prompt "Where do you want to go?(left/right): " displayed | Entered Invalid choice (e.g., 'right') for test case. | Invalid Choice Amigo | Pass |

### BUGS:

**Solved Bugs:**

- When i run my project i discovered that when a challenge instance the user to click _ENTER_ the program run anyway no matter if we had introduced another key before. In order to fix that problem and to provide the user with a better experience, i created the _TRY/EXCEPT_ statement. The user can **only** use the _ENTER_ key to proceed with the game when the program specifically requests it. If any key is pressed _before ENTER,_ the statement will be executed.

![Try / Except](/media/try-except%20statement.png)

- I've also added a function that _checks the valid inputs,_this functionality will prompt the user to enter a choice from a list of options. It continues to prompt the user until a valid choice is provided. I've created this function in order to avoid the user to put invalid inputs.

![Get Valid Inputs](/media/get-valid-inputs.png)

- I discovered another error in the _"Rock-Paper-Scissors"_ function. The error occurred when the user's choice matched the one randomly generated by the computer, in other words, when there was a _tie_. To fix this, I used a _WHILE LOOP._ With this, the play between the user and the computer will continue until the tie is broken. Additionally, in the case of a tie, a message will appear on the screen prompting the user to replay.

![While Loop in case of a Tie](/media/while-loop.png)

- As mentioned before many _"line is too long"_ were encuntered when passsing the code through the _PEP8 Validator_,in order to fix that i had to either refactor my code or convert strings that were too long to something suitable for the max amount of 79 characters.

![Docstrings](/media/docstrings.png)

- _PEP8 Validator_ also adviced me that some of the functions had no _Docstrings_,i fixed this by adding them and explining the functionality of those functions.

- I also wanted to mention that on sunday while writing my code i run out of Gitpod hours, being sunday, it was imposible for me to get in contact with someone in order to get more so i decided to clone the proyect on my computer and keep working on my local enviroment.

**Remaining Bugs**

- No bugs remaining.

## DEPLOYMENT:

This project was deployed with _Heroku_

- **STEPS FOR DEPLOYMENT:**
- _Fork or clone this repository_
- _Create a new Heroku App_
- _Set the buidbacks to Python and Node JS in that order_
- _Link the Heroku app to the repository_
- _Click on **Deploy**_

## CREDITS:

- I took inspiration for creating my Readme from the one added to the Love Sandwiches project. I also found very helpful the one written by _Kera Cudmore_ (https://github.com/kera-cudmore/TheQuizArms) in her JavaScript project for _Code Institute._

- The deployment method was also taken from the _Love Sandwiches project_.

- I drew inspiration for writing the game's story from those _Choose-your-own-adventure_ books I used to read when I was a child.

- On freeCodeCamp.org, I found a video showcasing 12 Beginner Python Projects.
[Youtube](https://www.youtube.com/watch?v=8ext9G7xspg)