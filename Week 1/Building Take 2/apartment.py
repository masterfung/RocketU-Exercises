from renters import Renter

__author__ = 'htm'

class Apartment(object):
	def __init__(self, unit, rent, sqft, num_bed, num_bath):
		self.unit = unit
		self.rent = rent
		self.sqft = sqft
		self.num_bed = num_bed
		self.num_bath = num_bath
		self.renters = []

	def __repr__(self):
		return self.unit