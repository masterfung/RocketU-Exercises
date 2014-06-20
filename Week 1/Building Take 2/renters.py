__author__ = 'htm'

class Renter(object):
	def __init__(self, name, age, apartment):
		self.name = name
		self.age = age
		self.apartment = apartment #every time you make a person, you should assign them to apartment

	def __repr__(self):
		return self.name