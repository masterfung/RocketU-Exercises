from building import Building
from apartment import Apartment
from renters import Renter
__author__ = 'htm'

def add_building():
	name = raw_input('Name of building? ')
	address = raw_input('Address of building? ')
	num_floors = raw_input('Number of floors of building? ')
	doorman = raw_input('Has doorman? (t/f) ')
	if doorman == 't':
		doorman = True
	else:
		doorman = False
	building = Building(name=name, address=adddress,
						num_floors=num_floors, doorman=doorman)
	#the orange in building is from Building while white is in this main init file
	return building

def add_apartment(buildings):
	print 'Available buildings: {}'.format(buildings)
	building_name = raw_input('What building is the apartment in? ')
	building = buildings[building_name] #building dict with building name
	unit = raw_input('Unit number: ')
	rent = raw_input('Cost of rent per month? ')
	sqft = raw_input('Total square feet: ')
	num_bed = raw_input('How many bed rooms does it have? ')
	num_bath = raw_input('Total bath count: ')
	apartment = Apartment(building=building, unit=unit, rent=rent, sqft=sqft,
							  num_bed=num_bed, num_bath=num_bath)
	return apartment

def add_renter():
	# choose the building
	print 'Available buildings: {}'.format(buildings)
	building_name = raw_input('What building is the renter in? ')
	building = buildings[building_name] #building dict with building name

	# choose the apartment in the building
	print 'Apartments: {}'.format(building.apartments)
	unit_num = raw_input('What is the unit? ')
	apartment = building.apartments[unit_num]

	# check if the apartmetn is full
	if not apartment.is_full():
		# make the renter
		name = raw_input('Name: ')
		age = raw_input('Age: ')
		renter = apartment.make_renter(name, age) #apartment can make renter or assign renters
	else:
		renter = None
		print 'That apartment is full.'

	return renter

print 'Welcome to the building manager application!'

response = raw_input('Would you like to add a (b)uilding, (a)partment,'
					 ' (r)enter, or (q)uit? ')
buildings = {}

while response != 'q':
	if response == 'b':
		building = add_building()
		buildings[building.name] = building #when i make a new building, i put it into the dictionary, more effective than a list
		#match the key and return building when the user input the right string
		print 'Thanks for adding building {}.'.format(building)
	elif response == 'a':
		apartment = add_apartment(buildings)
		print 'Thanks, {} has been added.'.format(apartment)
	elif response == 'r':
		renter = add_renter(buildings)
	#impt to keep them in the loop to have a question
	response = raw_input('Would you like to add a (b)uilding, (a)partment,'
					 ' (r)enter, or (q)uit? ')