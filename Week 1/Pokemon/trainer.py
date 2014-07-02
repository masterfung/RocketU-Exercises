__author__ = '@masterfung'

class Trainer(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.met_pokemon = []

	def __repr__(self):
		return name