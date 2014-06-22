import random
from random import randint

__author__ = 'htm'

class Nirvana(object):
	def __init__(self, name = 'John Doe'):
		self.name = name

	def __repr__(self):
		return 'Howdy! {}'.format(self.name)

	# Math quiz begins

	def math_quiz(self):
		math_questions_to_answer = randint(0, 10)
		math_types = ['add', 'subtract', 'multiply', 'divide']
		random_math_types = random.choice(math_types)
		return random_math_types

	def computer_random(self):
		options = ['simple', 'intermediate']
		rand_difficulty = random.choice(options)
		return rand_difficulty
	
	def question_randomizer(self):
		questions_range = randint(0, 5)
		return questions_range

	def welcome_message(self, response, random_math_types):
		print 'The gods have challenge you to a {} {} math quiz. Get ready!'.format(response, random_math_types)

	def results(self, correct, questions_range, rand_difficulty, random_math_types):
		if correct == questions_range:
			print 'You have impressed the gods for now.'
		elif correct != (questions_range * .75):
			print 'You are doomed! This is bad!'
		#self.quiz(questions_range, rand_difficulty, random_math_types, correct)


	def get_parts(self, opprand, questions_range, random_math_types):
		correct = 0
		computer_random_math_types = self.computer_random()
		if random_math_types == 'mixed':
			random_math_types = computer_random_math_types
		for i in range(questions_range):
			n1 = randint(1, opprand)
			n2 = randint(1, opprand)
			prod = self.math_engine(random_math_types, n1, n2)

			ans = input("What is %d %r %d? " % (n1, random_math_types, n2))
			if ans == prod:
				correct += 1
				print "That's right -- good job!\n"
			else:
				print "No, I'm afraid the answer is %r.\n" % prod
		return correct

	def math_engine(self, random_math_types, n1, n2):
		if random_math_types == 'multiply':
			return n1 * n2
		elif random_math_types == 'divide':
			return n1 / n2
		elif random_math_types == 'add':
			return n1 + n2
		elif random_math_types == 'subtract':
			return n1 - n2

	def final_outcomes (self, questions_range, correct):
		print "\nI asked you {} questions.  You got {} of them right.".format(questions_range, correct)

	def quiz(self, questions_range, rand_difficulty, random_math_types, correct):
		while True:
			try:
				questions_range
				break
			except ValueError:
				print 'Please use an integer so we can begin.'

		if rand_difficulty == 'simple':
			opprand = 10
		elif rand_difficulty == 'intermediate':
			opprand = 25

		if random_math_types == 'multiply':
			self.welcome_message(rand_difficulty, random_math_types)
			correct = self.get_parts(opprand, questions_range, random_math_types)
			self.final_outcomes(questions_range, correct)
			self.results(correct, questions_range, rand_difficulty, random_math_types)
		elif random_math_types == 'divide':
			self.welcome_message(rand_difficulty, random_math_types)
			correct = self.get_parts(opprand, questions_range, random_math_types)
			self.final_outcomes(questions_range, correct)
			self.results(correct, questions_range, rand_difficulty, random_math_types)
		elif random_math_types == 'subtract':
			self.welcome_message(rand_difficulty, random_math_types)
			correct = self.get_parts(opprand, questions_range, random_math_types)
			self.final_outcomes(questions_range, correct)
			self.results(correct, questions_range, rand_difficulty, random_math_types)
		elif random_math_types == 'add':
			self.welcome_message(rand_difficulty, random_math_types)
			correct = self.get_parts(opprand, questions_range, random_math_types)
			self.final_outcomes(questions_range, correct)
			self.results(correct, questions_range, rand_difficulty, random_math_types)
		elif random_math_types == 'q':
			print 'Please come back soon. Practice makes perfect.'
		else:
			self.quiz(self, questions_range, rand_difficulty, random_math_types)

	#Math quiz ends

	def demons(self):
		demons = [
			['Clancy the Good', 'Terrance the Brave', 'Jorge the Trustworthy', 'Penguina the Prudent', 'Susie the Fair', 'Maggie the Kind'],
			['Sauron the Greedy', 'Phillip Morris the Kingslayer', 'Hittles the Adolf of Men Doom', 'Yvette the Evil', 'Maleficent the malicious', 'Alexandra the Whore']
		]
		demon_type = randint(0,1)
		demon = random.choice(demons[demon_type])
		return demon

	def mystery_box(self):
		mystery_present = [
			['angelic dust', 'holy water', 'blessed sword', 'protection spell', 'invisibility cloak', 'antibiotics'],
			['death spell', 'rabies', 'wolves', 'decapitated', 'internal bleeding', 'dysentery']
		]
		mystery_random = randint(0,1)
		mystery = random.choice(mystery_present[mystery_random])
		return mystery

	def random_event_generator(self):
		pass

	def seven_sins(self):
		seven_sins = [ 'envy', 'gluttony', 'pride', 'wrath',
					   'lust', 'sloth', 'greed']
		sins = random.choice(seven_sins)
		return sins

	def destinations(self):
		locations = ['Chicago', 'New York City', 'Vancouver', 'Paris', 'Tibet',
					 'Melbourne', 'Moscow', 'Rome', 'Tokyo', 'Taipei', 'Beijing',
					 'Cairo', 'Cape Town']
		location = random.choice(locations)
		return location

	def game_play(self):
		hit_points = 10
		correct = 0
		enlightenment = 0
		location_count = 7
		print 'Welcome to the Nirvana game. {}, you will face a lot ' \
			  'challenges and evil. Be warned'.format(self.name)
		user_response = raw_input('Would you like to pursue the quest '
								  'to nirvana? (Y/N) ').lower()

		while user_response != 'n':
			location = self.destinations()
			print 'Before entering the the nirvana quest, you must pass' \
				  ' the test of the gods, overcome demons and evils, and answer' \
				  'all the questions correctly to achieve enlightenment.' \
				  'A spirit appears and take through a portal.'
			print 'Your currently at this location: {}.'.format(location)
			print 'Suddenly, the ground shakes, and a mysterious ' \
				  'orb appears and prompt you to a series of math questions. Get ready!'
			print 'You have {} hitpoints. Dont let it get to zero! You will die!'.format(hit_points)
			random_math_types = self.math_quiz()
			rand_difficulty = self.computer_random()
			questions_range = self.question_randomizer()
			self.quiz(questions_range, rand_difficulty, random_math_types, correct)
			if correct != questions_range:
				hit_points -= 1

			print hit_points
			print correct
			break

