from apartment import Apartment

__author__ = 'htm'


class Building(object):
	def __init__(self, address, num_floors, doorman, name):
		self.address = address
		self.num_floors = num_floors
		self.doorman = doorman
		self.name = self.name

	def __repr__(self):
		return self.address