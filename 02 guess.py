#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

guessesTaken = 0

print('Konnichiwa! What is your name?')
myName = input()

#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
number = random.randint(1,20)
print('Nice to meet you ' + myName + ' , I am thinking of a number between 1 and 20.')

for guessTaken in range(6):
		print('Take a guess')
		guess = input()
		try:
				guess = int(guess)
				
				if guess > number:
					print('Guessed too high!')
					
				if guess < number:
					print('Guessed too low!')
					
				if guess == number:
						break

		except ValueError:
			print('Please enter a whole number.')
		
if guess == number:
		guessesTaken = str(guessesTaken + 1)
		print('Nice, ' + myName +'! You guessed my number in ' + guessesTaken + ' guesses!')
		
if guess != number:
		number = str(number)
		print('Sorry. THe number I was thinking of was ' + number +'.')
		
