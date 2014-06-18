__author__ = 'Johnny Hung'

#Examples for Week 1 Day 3

def drink_juices(juices, name):
	dirty_juice = False
	for juice in juices:
		if juice['name'] == name:
			try:
				juice['exp_date']
			except:
				print 'No expiration date found for {}.'.format(juice['name'])
				dirty_juice = True
			else:
				index = juices.index(juice)
				juices.pop(index)

	print juices
	return dirty_juice

juices = [
	{'name': 'apple', 'expiration': 'july'},
	{'name': 'orange', 'expiration': 'dec'},
	{'name': 'pomegranate'},
	{'name': 'pineapple', 'expiration': 'july'},
	{'name': 'mango'},
]

drink_juices(juices, 'mango')