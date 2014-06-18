__author__ = 'Johnny Hung'

import math

def calculator():
	preface = raw_input('Would you like to use the (simple) or (advanced) calculator? ').lower()
	if preface == 'simple':
		response = raw_input('Would you like to (add), (subs), (mul), (div), (q) to quit? ').lower()
		if response == 'add':
			user_num1 = float(raw_input('What is your first number? '))
			user_num2 = float(raw_input('What is your second number? '))
			print user_num1 + user_num2
			calculator()
		elif response == 'subs':
			user_num1 = float(raw_input('What is your first number? '))
			user_num2 = float(raw_input('What is your second number? '))
			print user_num1 - user_num2
			calculator()
		elif response == 'mul':
			user_num1 = float(raw_input('What is your first number? '))
			user_num2 = float(raw_input('What is your second number? '))
			print user_num1 * user_num2
			calculator()
		elif response == 'div':
			user_num1 = float(raw_input('What is your first number? '))
			user_num2 = float(raw_input('What is your second number? '))
			if user_num1 == 0 and user_num2 == 0:
				print 'Cannot divide zero by zero. Please try other number.'
			else:
				print user_num1 / user_num2
			calculator()
		elif response == 'q':
			print 'Thanks for using the Simple Calculator. Come back again.'
		else:
			print 'The input you enter is incorrect. Please try again.'
			calculator()
	elif preface == 'advanced':
		response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
		while response != 'q':
			output = 0
			if response == 'add':
				numbers = raw_input('What numbers would you like to add? (separate with a space) ')
				numbers = numbers.split(' ') #split @ the designated char, in this case its the space. You can use 'x' to others
				for number in numbers:
					output += float(number)
				print output
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
			elif response == 'sub':
				numbers = raw_input('What numbers would you like to substract? Please place in the order you like your operation (separate with a space) ')
				numbers = numbers.split(' ') #split @ the designated char, in this case its the space. You can use 'x' to others
				output = float(numbers[0]) * 2
				for number in numbers:
					output -= float(number)
				print output
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
			elif response == 'mul':
				numbers = raw_input('What numbers would you like to multiply? Please place in the order you like your operation (separate with a space) ')
				numbers = numbers.split(' ') #split @ the designated char, in this case its the space. You can use 'x' to others
				output = float(numbers[0])
				for number in numbers[1:]:
					output *= float(number)
				print output
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
			elif response == 'div':
				numbers = raw_input('What numbers would you like to multiply? Please place in the order you like your operation (separate with a space) ')
				numbers = numbers.split(' ') #split @ the designated char, in this case its the space. You can use 'x' to others
				output = float(numbers[0])
				for number in numbers[1:]:
					if number == 0:
						print 'Please try again. Need not be zero.'
						numbers = raw_input('What numbers would you like to multiply? Please place in the order you like your operation (separate with a space) ')
					output = (output / float(number))
				print output
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
			elif response == 'remainder':
				first = float(raw_input('What is the first number: '))
				second = float(raw_input('What is the second number in which you want your first number to be divided by to determine remainder: '))
				print first % second
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
			elif response == 'expo':
				first = float(raw_input('What is the first number: '))
				second = float(raw_input('Enter a second number to have it raised to that power: '))
				print first ** second
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()
			elif response == 'sq':
				first = float(raw_input('Please enter a number to be square rooted: '))
				print math.sqrt(first)
				response = raw_input('Would you like to (add), (subs), (mul), (div), (remainder), (expo), (sq), (q) to quit? ').lower()

calculator()