import random
import string
from vehicles import RaceCar

__author__ = '@masterfung'

# List Comprehension

words = [word.lower() for word in ["Try", "tHiS", "OUT"]]
print words

squaring = [(num * num) for num in [1, 2, 3, 4, 5]]
print squaring

f_to_c_conversion = [(num - 32) / (1.8) for num in [104, 32, 68]]
print f_to_c_conversion

# Filter

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

# Lambda

divisible = filter(lambda x: x % 3 == 0, [6, 8, 11, 12, 15])
print divisible

lowercase = filter(lambda x: x != x.capitalize(), ["Todd", "jane", "George"])
print lowercase

food_list = [('meat lovers', ['sausage', 'pepperoni', 'bacon', 'ham']),
			 ('cheese', ['cheese']), ('veggie', ['mushrooms', 'onion', 'peppers'])]

meat = sorted(food_list, key=lambda food_list: food_list[1], reverse=True)
#the food_list[1] means that it is looking inside the numbers of meat lovers (4), cheese (1), and veggie (3)
#without the food_list then it will sort in the order of cheese, meat, veggie...since with reverse...it will be backwards
print meat

# Decorators
# Decorators always return a function!

def double(function):
	def twice():
		return function() * 2

	return twice


@double
def numbers():
	return 10


print numbers()

# ----- #

def stringify(function):
	def sentence():
		return ' '.join(function())

	return sentence


@stringify
def word_list():
	return ['This', 'is', 'a', 'sentence']


print word_list()

# ----- #

def currency(function):
	def magic():
		return '${:.2f}'.format(function())

	return magic


@currency
def money():
	return 30


print money()


# Generators

def evens():
	i = 1
	while i < 22:
		if i % 2 == 0:
			yield i
		i = i + 1


for int in evens():
	print int

# doubling #

def doubling():
	i = 1
	while True:
		if i % 1 == 0:
			yield i
		i += 2


double = doubling()
print double.next()
print double.next()
print double.next()
print double.next()

# a-z #

def alpha_return():
	alpha = list('abcdefghijklmnopqrstuvwxyz')  #turns each letter into a separate substance for use
	used = []
	i = random.choice(alpha)
	while True:
		alpha.remove(i)
		used.append(i)
		yield i


# Recursion

def max(list):
	if len(list) == 1:
		return list[0]
	else:
		m = max(list[1:])
		return m if m > list[0] else list[0]


print max([0, 6, 3, 12, 5])

# instructor's way #
def get_max(integers, max=0):
	if len(integers) == 0:
		return max
	else:
		num = integers.pop()
		if num > max:
			max = num
		return get_max(integers, max)


print get_max([0, 6, 3, 12, 5])


def list_flatten(a):
	results = []
	for x in a:
		if isinstance(x, list):
			results += list_flatten(x)
		else:
			results.append(x)
	return results


print list_flatten([1, [2, 3], [[4, 5], 6]])


# instructor's view #
def flatten_list(list_to_flatten, new_list=None):
	if new_list is None:
		new_list = []
	if len(list_to_flatten) == 0:
		return new_list
	else:
		item = list_to_flatten.pop(0)
		if isinstance(item, list):
			new_list = flatten_list(item, new_list)
		else:
			new_list.append(item)

		return flatten_list(list_to_flatten, new_list)

print flatten_list([1, [2, 3], [[4, 5], 6]])


def reverse_word(str):
	if str == '':
		return str
	else:
		return reverse_word(str[1:]) + str[0]


print reverse_word('string is awesome')