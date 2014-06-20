from renters import Renter

__author__ = 'htm'

class Apartment(object):
	def __init__(self, building, unit, rent, sqft, num_bed, num_bath):
		self.building = building
		self.unit = unit
		self.rent = rent
		self.sqft = sqft
		self.num_bed = num_bed
		self.num_bath = num_bath
		self.renters = []

		self.building.apartments[self.unit] = self #unit to put information into the building

	def __repr__(self):
		return self.unit

	def make_renter(self, name, age):
		p = Renter(name, age, self) #self is the specific instance of the Apartment
		self.renters.append(p)
		return p

	def is_full(self): #self is apt specific instance, is this apt full?
		if len(self.renters) < int(self.num_bed):
			return False
		else: return True