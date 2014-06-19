__author__ = '@masterfung'

#Today is about OO Programming

# Not Great Code:

# class Car(object):
# 	speed = 0
# 	direction = 'left'
# 	color = 'red'
#
# some_car = Car()
# print Car()
# print some_car.direction
# other_car = Car()
# other_car.direction = 'right'
# print other_car.direction

#Improving

# class Car(object):
# 	def __init__(self, color, type = 'ultra fast', speed = '300'):
# 		self.color = color
# 		self.type = type
# 		self.speed = speed
# new_car = Car('red', 'racing', '300')
# fast_car = Car('purple')
# print new_car.color
# print 'This {} car is {} and has a top-speed of {}mph.'.format(fast_car.type, fast_car.color, fast_car.speed)

# Mine
class Cake(object):
	def __init__(self, name, price, origin, serving, fluff = 'deliciousness', taste = 'knocks your socks off'):
		self.name = name
		self.price = price
		self.origin = origin
		self.serving = serving
		self.fluff = fluff
		self.taste = taste
	def craving(self):
		return 'We currently offer {}, which comes from the ' \
			  '{}, with a price of ${} per {} serving. This cake in particular' \
			  ' provides: {} taste, and a fluff content of: {}.'.format(
			self.name, self.origin, self.price, self.serving, self.taste, self.fluff
		)

cheesecake = Cake('cheesecake', '12', 'Artic Circle', 1)
print cheesecake.craving()

class Car(object):
	def __init__(self, color, make, speed=0):
		if color == 'red':
			self.color = 'white'
		else:
			self.color = color
		self.make = make
		self.speed = speed
	def __repr__(self):
		'''
		Prints out cooly like line 67, when called
		'''
		return '{} {}'.format(self.color, self.make)

new_car = Car('red', 'Tesla')
print new_car.color
print new_car.make
print new_car