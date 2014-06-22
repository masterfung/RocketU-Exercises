import random
from random import randint

__author__ = 'htm'


class Nirvana(object):
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Howdy! {}'.format(self.name)

	def game_play(self):
		print 'Welcome to the Nirvana game. {}, you will face a lot challenges and evil. Be warned'.format(self.name)
		user_response = raw_input('Would you like to pursue the quest to nirvana? (Y/N) ').lower()
		hit_points = 3
		enlightenment
		while user_response != 'n':
			hit_points = 3



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

	def reincarnation(self):
		'''
		Used for end game reincarnation.
		'''
		pass

	def destinations(self):
		locations = ['Chicago', 'New York City', 'Vancouver', 'Paris', 'Tibet',
					 'Melbourne', 'Moscow', 'Rome', 'Tokyo', 'Taipei', 'Beijing',
					 '']
