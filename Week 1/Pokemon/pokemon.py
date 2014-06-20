import random
from random import randint

__author__ = 'htm'

class Pokemon(object):
	def __init__(self)
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
			'grass': 'fire'
			'rock': 'water'
			'water': 'ground'
			'fire': 'water'
			'lightning': 'ground'
			'ice': 'fire'
			'normal': 'none'
			'ground': 'none'
 		}
		random_number = randint(1,15)
		self.name = ''.join(random.choice(alpha + vowels[1] + vowels + vowels) for i in range(random_number)) + mon
		self.type = random.choice(types)
		self.powers = random.choice(powers[self.type])
		self.weakness = weaknesses[self.type]
		self.super_effective = False
		for weakness in weaknesses:
			if weakness == self.type:
				self.super_effective = True
				return self.super_effective
			else:
				self.super_effective = False
				return self.super_effective

		self.health_points = randint(1,10)

	def __repr__(self):
		return self.name, self.type

	# def randomizer(self):
	# 	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# 	vowels = 'AEIOU'
	# 	mon = 'MON'
	#
	# 	types = ['grass', 'rock', 'water', 'fire',
	# 			'ground', 'lightning', 'normal', 'ice']
	# 	powers = {
	# 		'grass': ['razor leaf', 'seed bomb', 'petal dance'],
	# 		'rock': ['head smash', 'rollout', 'stealth rock'],
	# 		'water': ['bubble', 'water gun', 'surf'],
	# 		'fire': ['ember', 'blaze kick', 'flamethrower'],
	# 		'ground': ['dig', 'boomerang', 'mud bomb'],
	# 		'lightning': ['thunderbolt', 'spark', 'thunder punch'],
	# 		'normal': ['headbutt', 'double hit', 'fury strike'],
	# 		'ice': ['ice beam', 'ice punch', 'ice ball'],
	# 	}
	# 	weaknesses = {
	# 		'grass': 'fire'
	# 		'rock': 'water'
	# 		'water': 'ground'
	# 		'fire': 'water'
	# 		'lightning': 'ground'
	# 		'ice': 'fire'
	# 		'normal': 'none'
	# 		'ground': 'none'
 	# 	}
	# 	random_number = randint(1,15)
	# 	self.name = ''.join(random.choice(alpha + vowels[1] + vowels + vowels) for i in range(random_number)) + mon
	# 	self.type = random.choice(types)
	# 	self.powers = random.choice(powers[self.type])
	# 	self.weakness = weaknesses[self.type]
	# 	for weakness in weaknesses:
	# 		if weakness == self.type:
	# 			self.super_effective = True
	# 			return self.super_effective
	# 		else:
	# 			self.super_effective = False
	# 			return self.super_effective
	#
	# 	self.health_points = randint(1,10)
	# 	return self.name, self.type, self.powers, self.weakness, self.super_effective, self.health_points