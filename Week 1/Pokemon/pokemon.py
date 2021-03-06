import random
from random import randint

__author__ = 'htm'



class Pokemon(object):
	def __init__(self):
		pass

	def __repr__(self):
		return self.name, self.type

	@staticmethod
	def randomizer():
		alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		vowels = 'AEIOU'
		mon = 'MON'

		types = ['grass', 'rock', 'water', 'fire',
				'ground', 'lightning', 'normal', 'ice']
		powers = {
			'grass': ['razor leaf', 'seed bomb', 'petal dance'],
			'rock': ['head smash', 'rollout', 'stealth rock'],
			'water': ['bubble', 'water gun', 'surf'],
			'fire': ['ember', 'blaze kick', 'flamethrower'],
			'ground': ['dig', 'boomerang', 'mud bomb'],
			'lightning': ['thunderbolt', 'spark', 'thunder punch'],
			'normal': ['headbutt', 'double hit', 'fury strike'],
			'ice': ['ice beam', 'ice punch', 'ice ball'],
		}
		weaknesses = {
			'grass': 'fire',
			'rock': 'water',
			'water': 'ground',
			'fire': 'water',
			'lightning': 'ground',
			'ice': 'fire',
			'normal': 'none',
			'ground': 'none',
 		}
		p = Pokemon()
		p.random_number = randint(1,15)
		p.name = ''.join(random.choice(alpha + vowels[1] + vowels + vowels) for i in range(p.random_number)) + mon
		p.type = random.choice(types)
		p.powers = random.choice(powers[p.type])
		p.weakness = weaknesses[p.type]
		p.super_effective = False
		for weakness in weaknesses:
			if weakness == p.type:
				p.super_effective = True
			else:
				p.super_effective = False

		p.health_points = randint(1,10)

		return p