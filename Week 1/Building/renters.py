__author__ = '@masterfung'

class Renter(object):
	def __init__(self, name = 'unoccupied', dob='', len_of_stay = 'undefined'):
		self.name = name
		self.dob = dob
		self.len_of_stay = len_of_stay

	def __repr__(self):
		return '{} plans to stay {}. {}\'s dob is: {}.'.format(self.name, self.dob, self.len_of_stay)


