__author__ = 'htm'

class Renter(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return self.name