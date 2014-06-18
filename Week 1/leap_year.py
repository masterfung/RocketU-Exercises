__author__ = 'Johnny Hung'
def leap_year():
	'''
	Leap Year determination

	Nested conditional
	'''
	user_year = int(raw_input('What year: '))
	if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):
		print '{} is a leap year.'.format(user_year)
	else:
		print '{} is not leap year.'.format(user_year)

leap_year()