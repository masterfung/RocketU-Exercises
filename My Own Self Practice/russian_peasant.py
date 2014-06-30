__author__ = '@masterfung'

import time

def russian_peasant(a, b):
	'''
	<< and >> are binary shifts. Since this mathematical formula works through base 2,
	the most important thing to remember is this:

	17 in the base 2:
	10001  = 17 (from right to left count, 0 then 2, 4, 8, 16 + 1) = 17
	 >> 1 means remove one from the right
	 1000 = 8
	 8 instead of 8.5 beacause of integers.

	10001
	<< 1
	100010 = 34  32 + 2 = 34
	'''
	sum = 0
	while a > 0:
		if a % 2 == 1: sum += b
		b = b << 1
		a = a >> 1
	return sum

def test_russian():
	start_time = time.time()
	print russian_peasant(238, 13)
	print russian_peasant(13, 13)
	print russian_peasant(1002193, 1123133)
	print 'These entire processs took %f.' % (time.time()-start_time)

test_russian()