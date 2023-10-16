# INSIDE THE LABYRINTH

**Inside the labyrinth** is a _Python terminal game_ running in the Code Institute mock terminal from Heroku.

The User has to escape from a virtual labyrinth, in the search for the exit, the user will interact with the computer, which will put the user to the test through different challenges, including decision-making and games of chance.

[SCREENSHOT LIVE VERSION]
[MOCK UP]

## HOW TO PLAY?

After a small introduction, the computer instance the User to introduce the name that will use for this adventure.

After introducing user’s name, the computer will double check if the user is ready to start, and then the game will start.

During the process towards finding the exit, the user will encounter various _interactions with the computer._ **Decision-making** will be the most recurring challenge in the game. For example, choosing doors, paths, or using objects. In each decision-making instance, one of the options will allow the user to continue playing, while the other option will either delay the path to the maze's exit or defeat them directly.

The user will also face some **Games of chance**, such as 'Even or Odd' or 'Rock-Paper-Scissors'. Just like with the decision-making challenges, the user's luck will determine whether he encounters more obstacles before reaching the exit."

If the user achieves to pass all the challenges will win the game, and will set free from the Labyrinth.

## FEATURES:

### Existing Features:

**1 - Introduction:**
After entering our username, the computer will ask us if we are truly prepared for the challenge of escaping the maze; in case the answer is negative, the game will end instantly.

**2- First Challenge:**
The first decision the user will have to make is the path to follow. Here, two paths will be presented to us: the path of the snake or the path of the dragon. Depending on the choice, the user will face different challenges.
3- The Dragon’s Challenge:
If we choose the path of the dragon, we will encounter another decision to make. Whether to take the shield or, on the contrary, leave it. The dragon will awaken whether we take the shield or not, so if we leave it on the wall, the game will end.

**4- The Jester Challenge:**
If we successfully pass the Dragon’s Challenge, the new challenge the user will face is the “Jester”. The jester will offer us assistance with the next challenge only if we play a game of chance. In this case, the jester challenges us to play 'Rock, Paper, Scissors'. In case of losing, the game will not end, but we will not receive the clue to pass the next challenge.

**5- The Numbered Door Challenge:**
Once we have left the jester behind, we will encounter a new choice of doors, this time labeled as 1 and 2. If we manage to defeat the jester beforehand, we will have no difficulty in knowing which one will lead us to the next challenge, as one of the two contains a deadly trap.

If we choose wisely, another decision lies ahead of us: to choose whether to go up the stairs or down them. Just like in the previous door choice, one of the paths leads to a deadly trap.

**6- The Even Odd Challenge:**
If we manage to outsmart death twice in a row, the labyrinth will lead us to another character in the story. A kind of guardian-executioner who will urge us to play 'odds or evens.' This way, chance will determine whether we continue searching for the exit or, on the contrary, end the game.

**7- The Last Challenge:**
If the user manages to defeat the guardian, they will face the final challenge. In it, we find ourselves in a room with an iron door, and we must open that door to exit the maze. We will be given 5 keys for this task. Only one of them unlocks the door, and we have 2 attempts to open it.

**8 -The Snake Challenge:**
In the oder hand, if you decide to open the Snake’s door, we will have to make up our mind and decide if we take the sword hanging on the wall to fight the snakes on that room or if we decide to run and leave the sword behind. This decision will be capital to keep alive in the labyrinth.

**9- The Magician Challenge:**
If we still alive another challenge will be in front of us. The caracter of a Magician interacts with the user if the user wants to. In this case, the magician will request again the user’s name and then will invite us to play a game with a huge reward. We will have to throw a dice and depending on our score the user will, either end up at the dragon’s room or facing the last challenge. If the user’s option is to take the door instead interacting with the Magician, this door will bring him to another room full of snakes and the game will finish.

### Future Features:
...
...

## DATA MODEL:
..
..

## TESTING:

The project was manueally tested by doing:
- The code was passe through **_PEP8_** and confirmed there are no problems.

![PEP8](/media/pep8-Validator.png)

- Some valid inputs were giving: I need it to _add docstrings_ to some of the functions of the game. I also had many _lines that were too long_, more than 79 characters. Encounter also that some _blanklines contained whitespaces._
- Tested in the _Code Institute Heroku terminal_ and in my local terminal.

### BUGS:

**Solved Bugs:**

- When i run my project i discovered that when a challenge instance the user to click _ENTER_ the program run anyway no matter if we had introduced another key before. In order to fix that problem and to provide the user with a better experience, i created the _TRY/EXCEPT_ statement. The user can **only** use the _ENTER_ key to proceed with the game when the program specifically requests it. If any key is pressed _before ENTER,_ the statement will be executed.

![Try / Except](/media/try-except%20statement.png)

- I've also added a function that _checks the valid inputs,_this functionality will prompt the user to enter a choice from a list of options. It continues to prompt the user until a valid choice is provided. I've created this function in order to avoid the user to put invalid inputs.

![Get Valid Inputs](/media/get-valid-inputs.png)

- I discovered another error in the _"Rock-Paper-Scissors"_ function. The error occurred when the user's choice matched the one randomly generated by the computer, in other words, when there was a _tie_. To fix this, I used a _WHILE LOOP._ With this, the play between the user and the computer will continue until the tie is broken. Additionally, in the case of a tie, a message will appear on the screen prompting the user to replay.

![While Loop in case of a Tie](/media/while-loop.png)

- As mentioned before many _line is too long_ were encuntered when passsing the code through the _PEP8 Validator_,in order to fix thati had to either refactor my code or convert strings that were too long and something suitable for the max amount of 79 characters.

![Docstrings](/media/docstrings.png)

- _PEP8 Validator_ also adviced me that some of the functions had no _Docstrings_,i fixed this by adding them and explining the functionality of those functions.

- I also wanted to mention that on sunday while writing my code i run out of Gitpod hours, being sunday it was imposible for me to get in contact with someone in order to get more so i decided to clone the proyect on my computer and keep working local.

### VALIDATOR TESTINGS:
- **PEP8**
No errors were returned from Pep8online.com


[def]: /media/try-except%20statement.png