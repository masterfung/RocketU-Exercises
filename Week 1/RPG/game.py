import random
from random import randint

__author__ = '@masterfung'

class Nirvana(object):
	def __init__(self, name = 'John Doe'):
		self.name = name

	def __repr__(self):
		return 'Howdy! {}'.format(self.name)

	# Math quiz begins

	def math_quiz(self):
		math_types = ['add', 'subtract', 'multiply', 'divide']
		random_math_types = random.choice(math_types)
		return random_math_types

	def computer_random(self):
		options = ['simple', 'intermediate']
		rand_difficulty = random.choice(options)
		return rand_difficulty
	
	def numbers_of_math_questions(self):
		questions_range = randint(1, 5)
		return questions_range

	def math_welcome_message(self, response, random_math_types):
		print 'The gods have challenge you to a {} {} math quiz. Get ready!'.format(response, random_math_types)

	def results(self, correct, questions_range, rand_difficulty, random_math_types):
		if correct == questions_range:
			print 'You have impressed the gods for now.'
			return True
		elif correct != (questions_range * .75):
			print 'You are doomed! This is bad!'

	def math_question_setter(self, opprand, questions_range, random_math_types):
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
			return float(n1 / n2)
		elif random_math_types == 'add':
			return n1 + n2
		elif random_math_types == 'subtract':
			return n1 - n2

	def math_compiled_methods(self, rand_difficulty, random_math_types, questions_range, opprand):
		self.math_welcome_message(rand_difficulty, random_math_types)
		correct = self.math_question_setter(opprand, questions_range, random_math_types)
		self.final_outcomes(questions_range, correct)
		self.results(correct, questions_range, rand_difficulty, random_math_types)
		return self, correct

	def final_outcomes(self, questions_range, correct):
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
			correct = self.math_compiled_methods(rand_difficulty, random_math_types, questions_range, opprand)
		elif random_math_types == 'divide':
			correct = self.math_compiled_methods(rand_difficulty, random_math_types, questions_range, opprand)
		elif random_math_types == 'subtract':
			correct = self.math_compiled_methods(rand_difficulty, random_math_types, questions_range, opprand)
		elif random_math_types == 'add':
			correct = self.math_compiled_methods(rand_difficulty, random_math_types, questions_range, opprand)
		elif random_math_types == 'q':
			print 'Please come back soon. Practice makes perfect.'
		else:
			self.quiz(self, questions_range, rand_difficulty, random_math_types)
		return correct

	#Math quiz ends

	def demons(self):
		good_evil = ['good', 'evil']
		demons = {
			'good': ['Clancy the Good', 'Terrance the Brave', 'Jorge the Trustworthy', 'Penguina the Prudent', 'Susie the Fair', 'Maggie the Kind'],
			'evil': ['Sauron the Greedy', 'Phillip Morris the Kingslayer', 'Hittles the Adolf of Men Doom', 'Yvette the Evil', 'Maleficent the malicious', 'Alexandra the Whore']
			}

		g_e = random.choice(good_evil)
		demon = random.choice(demons[g_e])
		return demon, g_e

	def demon_randomizer(self):
		demon_choice = self.demons()
		demon_appearing = randint(0, 1)
		if demon_appearing == 1:
			return demon_choice

	def mystery_box(self):
		good_evil = ['good', 'evil']
		mystery_present = {
			'good': ['angelic dust', 'holy water', 'blessed sword',
					 'protection spell', 'invisibility cloak', 'antibiotics'],
			'evil': ['death spell', 'rabies', 'wolves', 'decapitated',
					 'internal bleeding', 'dysentery']
		}
		g_e = random.choice(good_evil)
		mystery = random.choice(mystery_present[g_e])
		return mystery, g_e

	def random_event_generator(self): #could do more in the future
		pass

	def seven_sins(self):
		seven_sins = [ 'envy', 'gluttony', 'pride', 'wrath',
					   'lust', 'sloth', 'greed']
		sins = random.choice(seven_sins)
		return sins

	def destinations(self):
		locations = ['Chicago', 'New York City', 'Vancouver', 'Paris', 'Tibet',
					 'Melbourne', 'Moscow', 'Rome', 'Tokyo', 'Taipei', 'Beijing',
					 'Cairo', 'Cape Town', 'Rio', 'London', 'Belize City']
		location = random.choice(locations)
		return location

	def get_user_response(self):
		return raw_input('Would you like to pursue the quest '
								  'to nirvana? (Y/N) ').lower()

	def game_play(self):
		user_response = self.get_user_response()
		self.name = raw_input('What is your name? ')

		i = 0
		enlightenment = 0
		while enlightenment < 5:
			if i == 0:
				hit_points = 10
				correct = 0
				i += 1

			print 'Welcome to the Nirvana game. {}, you will face a lot ' \
				  'challenges and evil. Be warned'.format(self.name)

			print 'Before entering the the nirvana quest, you must pass' \
					  ' the test of the gods, overcome demons and evils, and answer' \
					  ' all the questions correctly to achieve enlightenment. ' \
					  'A spirit appears and take through a portal.'

			while user_response != 'n':
				location = self.destinations()
				sin_land = self.seven_sins()
				print 'Your currently at this location: {}. The land of: {}!'.format(location, sin_land)
				print 'Suddenly, the ground shakes, and a mysterious ' \
					  'orb appears and prompt you to a series of math questions. Get ready!'
				print 'You have {} hitpoints. Dont let it get to zero! You will die!'.format(hit_points)
				random_math_types = self.math_quiz()
				rand_difficulty = self.computer_random()
				questions_range = self.numbers_of_math_questions()
				final_score = self.quiz(questions_range, rand_difficulty, random_math_types, correct)
				demon, g_e = self.demons()
				if final_score < questions_range: #need to fix this condition
					hit_points -= 1
				else:
					enlightenment += 1
				print 'Your current health is at: {}/10 ' \
					  'and your enlightenment is at: {}/5.'.format(hit_points, enlightenment)
				print 'All of a sudden, a demon named: {} appears. ' \
					  'You can either attack or accept the mystery gift.' \
					  ' When youu accept the mystery gift, you have to open it.'.format(demon)
				attack_open_gift = raw_input('(A)ccept the gift or A(t)tack the demon? ').lower()
				if attack_open_gift == 'a':
					mystery, good_or_evil = self.mystery_box()
					print 'The mystery gift you received is: {}.'.format(mystery)
					if good_or_evil == 'evil':
						hit_points -= 1
						print 'Evil mystery gift. Bad demon! Your hitpoint goes down!' \
							  ' Current hitpoint is: {}.'.format(hit_points)
					else:
						hit_points += 1
						print 'Good stuff you got there! You gain an extra health point!' \
							  ' Current hitpoint is: {}.'.format(hit_points)
				elif attack_open_gift == 't':
					chance_of_hit = randint(0, 1)
					if chance_of_hit == 1:
						print 'You defeated the demon {} without a scratch on you!'.format(demon)
					else:
						hit_points -= 1
						print 'Your attempt failed. Your hitpoints suffer. ' \
							  'It is now @: {} hit points.'.format(hit_points)
				if hit_points == 0:
					print 'Game Over!'
					break
				if enlightenment == 5:
					break
				else:
					print 'You did not achieve enlightenment. Try again in another life!'
					break

			if enlightenment == 5:
				print 'You achieved nirvana state!'
				play_again = raw_input('Do you want to play again? (Y/N) ').lower()
				if play_again == 'y':
					self.game_play()
				elif play_again == 'n':
					break
				else:
					print 'Come back again to achieve nirvana!'
					break