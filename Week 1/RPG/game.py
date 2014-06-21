import random
from random import randint

__author__ = 'htm'


class Nirvana(object):
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Howdy! {}'.format(self.name)

	def character(self):
		print 'Welcome to the Nirvana game. {}, will face a lot challenges and evil.'.format(self.name)
		user_response = raw_input('Would you like to pursue the quest to nirvana? (Y/N) ').lower()
		while user_response != 'n':
			pass


	def demons(self):
		demons = [
			['Clancy the Good', 'Terrance the Brave', 'Jorge the Trustworthy', 'Penguina the Prudent', 'Susie the Fair', 'Maggie the Kind'],
				  ['Sauron the Greedy', 'Phillip Morris the Kingslayer', 'Hittles the Adolf of Men Doom', 'Yvette the Evil', 'Maleficent the malicious', 'Alexandra the Whore']
		]
		demon_type = random.choice(demons)
		demon = random.choice(demon_type)
		return demon



	def mystery_box(self):
		mystery_present = [
			'angelic dust', 'holy water', ''
		]

	def random_event_generator(self):
		pass

	def seven_sins(self):
		seven_sins = [ 'envy', 'gluttony', 'pride', 'wrath',
					   'lust', 'sloth', 'greed']
		sins = random.choice(seven_sins)

	def reincarnation(self):
		'''
		Used for end game reincarnation.
		'''
		pass

	def destinations(self):
		pass