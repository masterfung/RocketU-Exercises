import math

__author__ = '@masterfung'

# Multiple of 3 and 5 #

def three_and_five():
	numbers = []
	i = 0
	while i < 1000:
		if i % 3 == 0 or i % 5 == 0:
			numbers.append(i)
		i += 1
	return sum(numbers)

total = three_and_five()
print total

#-reduction method using lambda-#
summary = reduce(lambda x, y: x+y, [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])
print summary



# Even Fibonacci numbers #

def even_fibonacci():
	a, b = 1, 1
	total = 0
	while a <= 4000000:
		if a % 2 == 0:
			total += a
		a, b = b, a+b  # the real formula for Fibonacci sequence
	return total

number = even_fibonacci()
print number





# Largest prime factor #






# Smallest multiple #

