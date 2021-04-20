# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.
# In this program, I took the initial file and fixed the bugs. All changes are notated.
# Peer Editor: Amy Schaeffer
# Review Date: 05/10/2020

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2': #Changed indenting
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return cave #Changed to proper variable name from "caves"

def checkCave(chooseCave): #Changed method name in attribute to correct name
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2) #Changes time slept from 3 to 2
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chooseCave == str(friendlyCave): #Changed to correct method title
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!') #Added parenthesis

playAgain = 'yes'
while playAgain == 'yes': #Removed playAgain = 'y' and added extra =
	displayIntro()
	caveNumber = chooseCave() #Typo in chooseCave
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for playing") #Changed "planing" to "playing"

