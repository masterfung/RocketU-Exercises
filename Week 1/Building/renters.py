__author__ = '@masterfung'

class Renter(object):
	def __init__(self, name, len_of_stay):
		self.name = name
		self.len_of_stay = len_of_stay

	def __repr__(self):
		return self.name, self.len_of_stay


