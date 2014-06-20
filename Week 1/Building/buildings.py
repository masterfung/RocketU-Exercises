from apartments import Apartment

__author__ = '@masterfung'

class Building(object):
	def __init__(self, vacancy, build_num, total_occupants):
		self.vacancy = vacancy
		self.build_num = build_num
		self.total_occupants = total_occupants
		self.apartment = []
		self.location = []

	def renter(self):
		pass

