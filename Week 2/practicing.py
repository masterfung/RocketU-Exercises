__author__ = '@masterfung'

# Just practicing #

#--map--#

celsius = [531, 12, 89, 52, 190, 109, -19, 25, 910]
fahrenheit = map(lambda x: (float(9)/5)*x + 32, celsius)
print fahrenheit

some_num = [12, 0, 0, -4, 5, 6, 7, 90, 7, 19]
filtered_num_with_seven = filter(lambda x: x % 7 == 0, some_num)
print filtered_num_with_seven

reduce_sum_ex = reduce(lambda x,y: x+y, celsius)
print reduce_sum_ex

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7]
c = [8, 9, 1, 2, 3]
l = map(lambda x:len(x), [a, b, c])
print l