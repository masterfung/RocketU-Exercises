import  random
from random import randint

__author__ = 'Johnny Hung'

def welcome_message(response, choice):
	print 'Welcome to the {} {} math quiz. Get ready!'.format(response, choice)

def results(result_of_math, questions_total):
	if correct == questions_total:
		print 'Perfecto! Onto the next level!'
	elif correct > (questions_total * .75):
		print 'Well done! You gotta a lot correct correct.'
	elif correct < (questions_total/2):
		print 'Please practice more. We know you will improve.'
	else:
		print 'Please consult with you teacher. (S)he will be able to help you out. Be strong!'
	quiz()

def computer_random():
	options = ["add", "subtract", "multiply", "divide"]
	rand = random.randint(0, 3)
	return options[rand]

def get_parts(opprand, questions_total, choice):
	correct = 0
	computer_choice = computer_random()
	if choice == 'mixed':
		choice = computer_choice
	for i in range(questions_total):
		n1 = randint(1, opprand)
		n2 = randint(1, opprand)
		prod = get_solution(choice, n1, n2)

		ans = input("What is %d %r %d? " % (n1, choice, n2))
		if ans == prod:
			correct += 1
			print "That's right -- well done.\n"
		else:
			print "No, I'm afraid the answer is %r.\n" % prod
	return correct

def get_solution(choice, n1, n2):
	if choice == 'multiply':
		return n1 * n2
	elif choice == 'divide':
		return n1 / n2
	elif choice == 'add':
		return n1 + n2
	elif choice == 'subtract':
		return n1 - n2

def final_outcomes (questions_total, result_of_math):
	print "\nI asked you {} questions.  You got {} of them right.".format(questions_total, result_of_math)

def quiz():

	while True:
		try:
			questions_total = int(raw_input('How many questions do you want to answer today? '))
			break
		except ValueError:
			print 'Please use an integer so we can begin.'

	choice = raw_input('Do you want (multiply), (divide), (subtract), (add), or (mixed)? (q) to quit ').lower()
	response = raw_input('Do you want (simple), (intermediate), or (advanced) math quiz? ').lower()

	if response == 'simple':
		opprand = 10
	elif response == 'intermediate':
		opprand = 25
	elif response == 'advanced':
		opprand = 100

	if choice == 'multiply':
		welcome_message(response, choice)

		result_of_math = get_parts(opprand, questions_total, choice)

		final_outcomes(questions_total, result_of_math)

		results(result_of_math, questions_total)

	elif choice == 'divide':
		welcome_message(response, choice)

		result_of_math = get_parts(opprand, questions_total, choice)

		final_outcomes(questions_total, result_of_math)

		results(result_of_math, questions_total)
	elif choice == 'subtract':
		welcome_message(response, choice)

		result_of_math = get_parts(opprand, questions_total, choice)

		final_outcomes(questions_total, result_of_math)

		results(result_of_math, questions_total)
	elif choice == 'add':
		welcome_message(response, choice)

		result_of_math = get_parts(opprand, questions_total, choice)

		final_outcomes(questions_total, result_of_math)

		results(result_of_math, questions_total)
	elif choice == 'mixed':
		welcome_message(response, choice)

		result_of_math = get_parts(opprand, questions_total, choice)

		final_outcomes(questions_total, result_of_math)

		results(result_of_math, questions_total)
	elif response == 'q':
		print 'Please come back soon. Practice makes perfect.'
	else:
		quiz()
quiz()