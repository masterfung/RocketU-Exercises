import random
from random import randint

__author__ = '@masterfung'

# CLASSES #

# -MAIN-#

class Vehicle(object):
	def __init__(self, color):
		self.speed = 10
		self.name = 'Sexy Car'
		self.direction = 0
		self.color = color

	def __repr__(self):
		return self.color

	@staticmethod
	def random_car_color():
		colors = ['red', 'silver', 'yellow', 'orange', 'white', 'black']
		return random.choice(colors)

	@staticmethod
	def vehicle_rand_direction():
		return random.randint(-180, 180)

	@classmethod
	def new_random_color_car(cls):
		return cls(cls.random_car_color())


	def start_engine(self):
		start_engine = raw_input('Do you want to start the engine? (y/n) ').lower()
		if start_engine == 'y':
			print 'Your engine has started!'
		elif start_engine == 'n':
			print 'The engine is off!'
		else:
			print 'Not sure what you mean!'

	def accelerate(self):
		self.speed += max(0, 1)
		print 'Car speed increase, zoom zoom zoom...'

	def brake(self):
		self.speed -= max(0, 1)
		print 'Brake light shine red for a bit to warn others!'

	def stop(self):
		self.speed = 0
		print 'Your vehicle has come to a stop.'

	def turn_left(self):
		self.direction -= 90
		print 'Left signal turned on b/c you are turning left.'

	def turn_right(self):
		self.direction += 90
		print 'Right signal turned on b/c you are turning right.'


# MIXINS #

class CarMixin(object):
	def start_wipers(self):
		self.wipers = 'on'

	def stop_wipers(self):
		self.wipers = 'False'

	def check_raining(self):
		is_raining = raw_input('Is it raining? Want to turn on the windshield wipers? (y/n) ').lower()
		if is_raining == 'y':
			self.start_wipers()
		else:
			self.stop_wipers()


class RadioMixin(object):
	def start_radio(self):
		self.radio = 'on'

	def stop_radio(self):
		self.radio = 'off'

	def check_radio(self):
		channels = ['rock', 'alternative', 'pop', 'country', 'punk', 'foreign']
		user_channel_choice = raw_input('What channel do you want: {} '.format(channels)).lower()

		if user_channel_choice in channels:
			print 'You are now listing to: {}.'.format(user_channel_choice)


#-2nd Tier Starts-#

class ManualTrans(Vehicle):
	def __init__(self, color):
		super(ManualTrans, self).__init__(color)
		self.clutch_in = False

	def engage_clutch(self):
		self.clutch_in = True

	def disengage_clutch(self):
		self.clutch_in = False

	def brake(self):
		self.break_light = True
		self.engage_clutch()
		super(ManualTrans, self).brake()
		self.disengage_clutch()
		self.break_light = False


class AutoTrans(Vehicle):
	pass


class Boat(AutoTrans):
	pass


class AutoCar(AutoTrans, CarMixin):
	pass


class ManualCar(ManualTrans):
	def __init__(self, color):
		super(ManualTrans, self).__init__(color)  # must abide by Vehicle init requirements

	def change_gear(self):
		gears = ['r', 1, 2, 3, 4, 5]
		gear_choice = raw_input('What gear setting do you want {}: '.format(gears))
		self.clutch_in = True
		if gear_choice == 'r':
			print 'You are now in reverse mode. Look behind for any objects/pedestrians.'
		elif gear_choice == '1' or gear_choice == '2':
			print 'Power gears in place. Good for slopes.'
		else:
			print 'Normal gears.'
		self.clutch_in = False


#-2nd Tier End-#
#-3rd Tier Start-#

class Motorbike(ManualTrans):
	def brake(self):
		super(ManualTrans, self).brake()  # if you want to call ManualCar brake,

	# then it should be Motorbike rather than ManualTrans. Hence,
	# this calls the Vehicle brake method


class StreetCar(ManualCar, CarMixin, RadioMixin):
	def password_auth(self):
		password_request = raw_input('Before you can start the car, what is the password? ')
		if password_request == 'Pokemon':
			print 'Welcome Pikachu!'
			self.start_engine()
		else:
			print 'Your in guest mode. Certain features will not work.'
			self.start_engine()

	def brake(self):
		super(ManualTrans, self).brake()
		print 'You stepped on the break, slowing down by 1.'

	def use_nitro(self):
		use_nitro = raw_input('Do you want to use nitro? (y/n) ').lower()
		if use_nitro == 'y':
			print 'You are not using nitro! 3X the speed.'
			self.accelerate()
			self.accelerate()
			self.accelerate()
		else:
			print 'No nitro is engaged. Normal speed.'
			self.accelerate()

	@classmethod
	def new_class_creation(cls, vehicle):
		new_vehicle = cls(vehicle.color) #color from init method
		new_vehicle.speed = vehicle.speed
		new_vehicle.direction = vehicle.direction
		return new_vehicle


class RaceCar(ManualCar, CarMixin):
	def __init__(self, color):
		super(ManualCar, self).__init__(color)


# street_car = StreetCar('white')
# street_car.name = 'Hittles of Goods'
# street_car.color = Vehicle.random_car_color() #calling the staticmethod
# print street_car.color
# street_car.password_auth()
# street_car.check_radio()
# street_car.use_nitro()
# street_car.brake()
# street_car.check_raining()
# street_car.stop()
# street_car.direction = Vehicle.vehicle_rand_direction()
# print street_car.direction
# street_car.turn_left()
# street_car.change_gear()
# street_car.accelerate()
# street_car.accelerate()
# street_car.accelerate()
# street_car.accelerate()
# street_car.accelerate()
# street_car.accelerate()
# street_car.accelerate()
#
# print 'Your car name is: {}, color: {}, and end ' \
# 	  'acceleration is: {}.'.format(street_car.name,
# 									street_car.color,
# 									street_car.speed)

my_car = Vehicle.new_random_color_car()
print my_car

child_car = StreetCar.new_class_creation(my_car)
print child_car
print child_car.speed

