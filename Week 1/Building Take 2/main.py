from building import Building

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


print 'Welcome to the building manager application!'

response = raw_input('Would you like to add a (b)uilding, (a)partment,'
					 ' (r)enter, or (q)uit? ')

while response != 'q':
	if response == 'b':
		building = add_building()
		print 'Thanks for adding building {}.'.format(building)
	elif response == 'a':
		pass
	elif response == 'r':
		pass
	#impt to keep them in the loop to have a question
	response = raw_input('Would you like to add a (b)uilding, (a)partment,'
					 ' (r)enter, or (q)uit? ')