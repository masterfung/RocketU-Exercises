__author__ = 'Johnny Hung'
from random import randint

def guessing():
	computer = randint(1,100)
	guesses = 1
	user_input = int(raw_input('Please enter a number between 1 and 100: '))
	while user_input != computer:
		guesses += 1
		if user_input > computer:
			user_input = int(raw_input('Too high! Try Again: '))
		elif user_input < computer:
			user_input = int(raw_input('Too low. Try Again: '))
	print('Congratulations! You got it in {} guesses.').format(guesses)


guessing()