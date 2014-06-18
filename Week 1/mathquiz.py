from __future__ import division
from random import randint
__author__ = 'Johnny Hung'

def welcome_message(response, choice):
	print 'Welcome to the {} {} math quiz. Get ready!'.format(response, choice)

def results(correct,questions_total):
	if correct == questions_total:
		print 'Perfecto! Onto the next level!'
	elif correct > (questions_total * .75):
		print 'Well done! You gotta a lot correct correct.'
	elif correct < (questions_total/2):
		print 'Please practice more. We know you will improve.'
	else:
		print 'Please consult with you teacher. (S)he will be able to help you out. Be strong!'
	quiz()

def final_outcomes (questions_total, correct):
		print "\nI asked you {} questions.  You got {} of them right.".format(questions_total, correct)

def quiz():
	correct = 0
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

		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 * n2

			ans = input("What is %d times %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		results(correct, questions_total)
	if choice == 'divide':
		welcome_message(response, choice)

		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 / n2

			ans = input("What is %d divided by %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		results(correct, questions_total)
	if choice == 'subtract':
		welcome_message(response, choice)

		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 - n2

			ans = input("What is %d minus %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		results(correct, questions_total)
	if choice == 'add':
		welcome_message(response, choice)

		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 + n2

			ans = input("What is %d plus %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		results(correct, questions_total)
	if choice == 'mixed':
		welcome_message(response, choice)
		print 'First up is addition: '

		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 + n2

			ans = input("What is %d plus %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		results(correct, questions_total)

		print 'Second is subtraction: '

		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 - n2

			ans = input("What is %d minus %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		print 'Third is multiplication'
		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 * n2

			ans = input("What is %d times %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		print 'Finally, onto division'
		for i in range(questions_total):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = n1 / n2

			ans = input("What is %d divided by %d? " % (n1, n2))
			if ans == prod:
				print "That's right -- well done.\n"
				correct += 1
			else:
				print "No, I'm afraid the answer is %d.\n" % prod
		final_outcomes (questions_total, correct)
		results(correct, questions_total)
	elif response == 'q':
		print 'Please come back soon. Practice makes perfect.'
	else:
		quiz()
quiz()