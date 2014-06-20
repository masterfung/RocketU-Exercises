from apartments import Apartment

__author__ = '@masterfung'

class Building(object):
	def __init__(self, address, vacancy, build_num, total_occupants):
		self.address - address
		self.vacancy = vacancy
		self.build_num = build_num
		self.total_occupants = total_occupants
		self.apartment = []
		self.location = []

	def __repr__(self):
		return self.total_occupants

	def renter(self):
		pass

