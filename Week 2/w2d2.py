from vehicles import RaceCar

__author__ = '@masterfung'

#List Comprehension

words = [word.lower() for word in ["Try", "tHiS", "OUT"]]
print words

squaring = [(num*num) for num in [1, 2, 3, 4, 5]]
print squaring

f_to_c_conversion = [(num-32)/(1.8) for num in [104, 32, 68]]
print f_to_c_conversion

#Filter

def three_or_less(x):
	return len(x) > 3

new_lists = filter(three_or_less, ["Some", "words", "to", "test"])
print new_lists

def no_evens(x):
	return x % 2 == 1

odds = filter(no_evens, [1, 2, 3, 4, 5])
print odds

def got_no_red(x):
	return x.color != 'red'

no_red_racecar = filter(got_no_red, [RaceCar("black"), RaceCar("blue"), RaceCar("red")])
print no_red_racecar

'''
def __repr__(self):
return '{} - {}'.format(self.__class__.__name__,self.color) __class__ gets the class, sim to __name__
return the string formatting of:
Filter out all RaceCars that are the color red,
[RaceCar("black"), RaceCar("blue"), RaceCar("red")] should be [RaceCar("black"), RaceCar("blue")]
'''

#Lambda

divisible = filter(lambda x : x % 3 == 0, [6, 8, 11, 12, 15])
print divisible

lowercase = filter(lambda x : x != x.capitalize(), ["Todd", "jane", "George"])
print lowercase

food_list = [('meat lovers', ['sausage', 'pepperoni', 'bacon', 'ham']),
			 ('cheese', ['cheese']), ('veggie', ['mushrooms', 'onion', 'peppers'])]

meat = sorted(food_list, key=lambda food_list:food_list[1], reverse = True)
#the food_list[1] means that it is looking inside the numbers of meat lovers (4), cheese (1), and veggie (3)
#without the food_list then it will sort in the order of cheese, meat, veggie...since with reverse...it will be backwards
print meat