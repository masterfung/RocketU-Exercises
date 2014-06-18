__author__ = 'Johnny Hung'
from __future__ import division

def temperature_converter():
	"""
	Convert temperature between F to C based on user input

	Temperature formulas:
	Tc=(5/9)*(Tf-32)
  	Tf=(9/5)*Tc+32
	"""
	first = float(raw_input('Enter a temperature: '))
	second = raw_input('Convert to (F)ahrenheit or (C)elsius?? ').lower()

	if second == 'f':
		convertedCtoF = (9/5)*first+32
		print '{} C = {} F'.format(first, convertedCtoF)
	elif second == 'c':
		convertedFtoC = (5/9)*(first-32)
		print '{} F = {} C'.format(first, convertedFtoC)
	else:
		print 'Please enter a valid response.'
		temperature_converter()

temperature_converter()