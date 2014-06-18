__author__ = 'Johnny Hung'
from random import shuffle

shirt_collection = range(1,20)
shuffle(shirt_collection)

def shirt_change(send_back):
	while len(shirt_collection) > 0:
		if send_back == False:
			choice = shirt_collection.pop()
			print choice
			if len(shirt_collection) == 0:
				print('Time to do laundry! Please use eco-friendly products only!')
			else:
				print "You still have these shirts left: {}".format(shirt_collection)
		elif send_back == True:
			choice = shirt_collection.pop()
			print "We will return this {} shirt back to the collection".format(choice)
			shirt_collection.append(choice)
			shuffle(shirt_collection)
			choice2 = shirt_collection.pop()
			print 'Your choice now is: {}'.format(choice2)
			if len(shirt_collection) == 0:
				print('You know the drill. Please use only eco-friendly products.')
			else:
				print "You still have these shirts left: {}".format(shirt_collection)



#shirt_change(False)
shirt_change(False)


# Make sure it takes user input
# make sure it takes new laundry
# make sure it return if i dont like