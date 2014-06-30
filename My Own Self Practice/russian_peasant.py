__author__ = '@masterfung'


def russian_peasant(a, b):
	sum = 0
	while a > 0:
		if a % 2 == 1: sum += b
		b = b << 1
		a = a >> 1
	return sum

print russian_peasant(238, 13)
print russian_peasant(13, 13)
print russian_peasant(1002193, 1123133)