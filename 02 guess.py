#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

chances = 0

myName = input('Konnichiwa! What is your name?')

#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
number = random.randint(1,20)
print('Nice to meet you ' + myName + ' , I am thinking of a number between 1 and 20.')

for chances in range(10):
		guess = input('take a guess:')
		try:
				guess = int(guess)
				
				if guess > number:
					print('Guessed too high!')
					
				elif guess < number:
					print('Guessed too low!')
					
				elif guess == number:
					print('Yay! You guessed it right!')
						break

		except ValueError:
			print('Please enter a whole number.')
		
if guess == number:
		chances = str(chances+1)
		print('Nice, ' + myName +'! You guessed my number in ' + chances+1 + ' guesses!')
		
if guess != number:
		number = str(number)
		print('Sorry. THe number I was thinking of was ' + number +'.')
		
