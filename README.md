# Project Overview

This project is a text-based ‘choose your own adventure’ game designed to run as a Python terminal game. The game has been deployed to Heroku and uses the Code Institute mock terminal. 
The aim of this game is for the user to navigate through a small starter adventure, with multiple paths to progress the story, and multiple endings. 

## User Goals 
To be able to play a game with multiple options to progress
To play a simple game 
To be able to replay the game and have different outcomes
To play a game with a chance of failure so that choices matter 

## Programmer Goals
To create a game the user wants to play again
To create a game that has some level of challenge and random chance
To create a game that is satisfying for the user to play and complete

## program/story flow charts

[program planner](documentation/images/app_flowchart.PNG)
This was my initial plan for my program. Although the shape of the program is similar, and this was a great guide in the programming process. I have realised in reflection that when planning this project, I underestimated the about of functionality I would need.  I have definitely learn the benefits of proper and realistic planning this project. 

[story planner](/documentation/images/story_planner.PNG)

This story planner really helped me not only with the story but also in anticipating how the code will shape out. This along side the above flow chart where a real boon to my coding process. 


## Game Features 
Title screen
The title screen uses Pyfiglet to create a styles banner that gives the app a more game-like feel.
The player is then greeted and asked to supply their name in the hopes of drawing them straight into the narrative of the game. 

## Delay Print 
Time and sys are imported to create a delay print function. This code was taken directly from Stackoverflow and is not my own. This was implemented for 2 reasons: to give the user a feeling that the story is being created as they play, and to allow them to track the progression of the game easily with printed out text. Without this function, a large block of narrative may be printed at once meaning the user can easily lose where they are in the game. 

## Use of classes for PC and NPCs
A main entity class was created with the bass stats and functions that are shared between the player character and enemy characters. This means that the generation of new enemies or player classes is very simple. It also makes it easy to expand the game in the future. 
The entity class contains a function to make an attack that uses the player base stats plus the ‘attack damage’ of the weapon they have equipped. 
There is also a ‘change weapon’ function that can be called to allow the player to change between weapons in their weapon inventory. 

## Classes for Weapons
As well as using classes for game characters, they are also used to create weapons. There is a base weapon class that has all the basic stats and functions for weapons. This means, just like with the entity class, it is very easy to make new weapon sub classes and expand the game in the future. It also helps make the code more readable as large chunks of code are not needlessly re-used. 
All weapons have an atk-mod function that is used to minimise and maximise damage of the weapon, and random.randint to create a random attack modifier each time the weapon is used. 
I used this system of generating random damage as it emulated dice roll based RPGS such as DnD that has been tried and tested over the decades. 
Weapon_name_list 
I made this function when refactoring my loot function. This means that the loot function is easier to read and also means that this function can be used when expanding in the future.  For instance, in a pick pocket/stealing function.  

## Battle Function
This function holds the main loop that runs all combat in the game. The function initiates one round of combat then gives the player the option to change weapons or continue to fight. The function prints out how much damage is being dealt, who is attacking and who is taking damage. This means that the player can get some real feedback about the combat and feel more immersed in the game.
The While loop is broken when the character or enemy falls below 0 health. If the player dies, they are sent to the player death function. If they win, they are given the option to loot and the player/character stats are returned. 
Battle-option
The battle option gives the player some choices during combat that can change the outcome of the game. If the player chooses to change weapon, the change weapon function of the player class is called. Changing to stronger weapons is the only way a player can kill all the enemies in the game, and survive if they choose to engage with every combat. It also breaks up what would otherwise be a completely automated cycle. 

## Loot 
This function iterates through the list of weapons and items of the player and the enemy, and prints the enemy’s items out. It then gives the player the chance to add the enemy’s items to their own inventory. 

##  Weapon_input_validation
This function is used to iterate through the player’s weapons list and check if the player input matches any weapons they have. If the player input does not match, a message is printed out telling them what their options are again and asks for a new input. When a valid input is given, it returns that valid input. 

## Input Validation
This is a much simpler validation process than the previous process and uses much less lines of code. This is not suitable for weapon validation hence having two types of validation functions. The function uses *args so that it can validate user input for multiple choices and not just a set number of choices. This gives the game much more flexibility for future expansion. 

## Story Function
The following functions deal with the narrative of the story and lead the play through a series of choices that can lead to different outcomes at the end of the game. 
Get_player_name
This function creates the player character class and gives the name the player inputs. This begins our adventure and allows the player to personalise their journey from the very beginning. 
Narrative Choice Functions
The majority of the functions in this section give small snippets of story to provide the player with options for what to do next, using ‘if statements’ and input validation. The player will be sent to the appropriate function based on their choices.
Examples of these functions:
	Goblin_cave_entrance and hidden_path

# Story Combat Functions
These functions set the player to fight different types of enemies and add some narrative to the combat. They use the battle function to run the combat and send them to the next function if they win. 
Examples:
	Goblin_ambush, wolf_fight

## Progress Checkers
There are 2 functions in the game that check the progress of the player and send them to the correct function based on what choices they made earlier in the game. They do this by checking the values assigned to the player_character.cave_save and the player_character.newtown-save, which are attributes of the player class. This means that if a player heads to Newtown before they clear the cave, they will be given different scenarios to deal with. 
If I was to expand the game and have multiple levels, I would create level classes that would hold save game info instead of storing it in the player class. 

## Endings
There are 4 possible ending functions that can be called depending on the player choices.
These endings all call the play again function so the player can start again if they wish.

## Play again
This function gives the player the option to replay if they die or complete the game, which gives the player more agency.  

Player death function is called if the player dies in combat and calls the play_again function.

## quit_game.
Allows the player to quit the game if they die or complete the game.

## Main
This is used to run the main games.

## Testing and Bugs
To test the game I would play through the option locally and on the Heroku live page.
I ran the code through [pep8](documentation/testing/result_20211216_011434.txt) validation and there were some line spacing issues, which meant I had to reduce the length of line in the story sections. 
While play testing I came across a bug in my loot function that caused the game to crash.
The loot function did not return the player_character when the player chose to continue.  
I am unaware of any further bugs. 

## Deployment
1. Fork or clone this repository to your own GitHub repository
2. Create a new Heroku App
3. Set the buildbacks to Python and NodeJS in that order.
4. Add Config Var keys  
     - PORT, 8000
     - KEY, VALUE
5. Link the Heroku app to repository
6. Click on Deploy

## Technologies used
Python3

## Libraries 
import random
import pyfiglet
import time
import sys

# Credits 

## Acknowledgements
My mentor Chris Quin is a constant inspiration. He is the steady hand on the tiller that means this boat never drifts too far into troubled waters. 

## sources

used pyfiglet to create title banner
https://www.devdungeon.com/content/create-ascii-art-text-banners-python

copied this code to print out test charascter by character. 
https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line