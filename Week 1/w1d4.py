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
	def __init__(self, color, make, direction, speed=0):
		if color == 'red':
			self.color = 'white'
		else:
			self.color = color
		self.make = make
		self.direction = direction
		self.speed = speed

	def __repr__(self):
		'''
		Prints out cooly like line 67, when called
		'''
		return '{} {}'.format(self.color, self.make)

	def accelerate(self):
		self.speed += 100

	def brake(self):
		self.speed -= 10

	def turning(self):
		if self.direction == 'left':
			self.direction = -90
		elif self.direction == 'right':
			self.direction = 90


new_car = Car('red', 'Tesla', 'left')
print new_car.color
print new_car.make
print new_car

new_car.accelerate()
new_car.accelerate()
new_car.accelerate()
new_car.accelerate()
new_car.accelerate()
new_car.accelerate()
new_car.brake()
new_car.brake()
new_car.turning()

print new_car.speed
print new_car.direction


class Bike(object):
	def __init__(self, style, frame_size, type, price, speed, direction, condition = 'new'):
		self.style = style
		self.frame_size = frame_size
		self.type = type
		self.price = price
		self.speed = speed
		self.direction = direction
		self.accessory = {
			'maintenance': [],
			'swag': [],
		}
		self.condition = condition

	def __repr__(self):
		return 'You selection yielded: {} style bike,' \
			   ' {}cm size, {} type, ${} price per unit, ' \
			   '{} condition. You have {} accessories.'.format(self.style, self.frame_size, self.type, self.price, self.condition, len(self.accessory))

	def accelerate(self):
		self.speed += 100

	def brake(self):
		self.speed -= 10

	def turning(self):
		if self.direction == 'left':
			self.direction = -90
		elif self.direction == 'right':
			self.direction = 90

	def accessories(self, acc_type, accessory):
		pass


my_bike = Bike('Adult', 53, 'road', 4000, 0, 0, )
print my_bike
my_bike.accessories()
print my_bike.accessories