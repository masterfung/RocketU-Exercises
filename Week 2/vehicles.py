__author__ = '@masterfung'

# MIXINS #

class CarMixin(object):
	def start_wipers(self):
		self.wipers = 'on'

	def stop_wipers(self):
		self.wipers = 'False'

class RadioMixin(object):
	def start_radio(self):
		self.radio = 'on'

	def stop_radio(self):
		self.radio = 'off'

# CLASSES #

#-MAIN-#

class Vehicle(object):
	def __init__(self, color):
		self.speed = 0
		self.direction = 0
		self.color = color

	# def __repr__(self):
	# 	print 'Your car has the speed of {} and the color of {}.'.format(self.speed, self.color)

	def accelerate(self):
		self.speed += max(0, 1)

	def brake(self):
		self.speed -= max(0, 1)

	def turn_left(self):
		self.direction -= 90

	def turn_right(self):
		self.direction += 90

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

class AutoCar(AutoTrans):
	pass

class ManualCar(ManualTrans):
	def __init__(self, color):
		super(ManualTrans, self).__init__(color)  # must abide by Vehicle init requirements

	def change_gear(self):
		gears = ['r', 1, 2, 3, 4, 5]
		gear_choice = raw_input('What gear setting do you want {}: ').format(gears)
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




class StreetCar(ManualCar):
	pass


class RaceCar(ManualCar, CarMixin):
	def __init__(self,color):
		super(RaceCar, self).__init__(color)

# manual = ManualCar('red')
# print manual.color
# print manual.accelerate
#
# vehicle = Vehicle('orange')


