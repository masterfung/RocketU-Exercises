from renters import Renter

__author__ = '@masterfung'

class Apartment(object):
	def __init__(self, unit_num, rent_cost, location, vacancy, sq_ft = 300, nums_bed = 1, bath =1):
		self.unit_num = unit_num
		self.rent_cost = rent_cost
		self.location = location
		self.vacancy = vacancy
		self.sq_ft = sq_ft
		self.nums_bed = nums_bed
		self.bath = bath
		#self.renters = []
		self.ammetities = {
			'furnishes': [],
			'services': [],
		}

	def __repr__(self):
		return self.unit_num

	def movein(self, name, ):
		pass

	def moveout(self):
		pass