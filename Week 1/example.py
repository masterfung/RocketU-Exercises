# __author__ = 'Johnny Hung'
# #Week 1 Monday Class Example
#
# import sys
# print sys.argv[0]
# print sys.argv[1]
# print 'Hello {}'.format(sys.argv[1])
#
# def my_favorite(wow):
#     print 'I love cheese!' + wow
#
#
# my_favorite(' Awesome right?')
#
#
# def multiplication(a, b, c):
#     return a * b * c * c * b * a
#
# foo = multiplication(5,6,9)
# print foo
#
#
# fruits = ['tangerine', 'grape', 'pineapple', 'banana', 'apple']
#
# print fruits [2:]
# print fruits.append('pear')
# print fruits.append('mellon')
# print fruits.count('mellon')
# print fruits
#
# def ate(substance):
#     return 'I love eating: ' + substance + '.'
#
# #looping structure
# for fruit in fruits:
#     print ate(fruit)
#
#
# print 'Ben Kremer will love to eat some ' + fruits[6] + ' by tomorrow night.'
#
# my_lib = {'Harry Potter': 'JK Rowling', 'books': '7', 'ratings': 'awesome'}
#
# print my_lib['Harry Potter']
#
# print my_lib['ratings']
#
# my_lib['movies'] = 'yes'
#
# print my_lib.has_key('books')
#
# for k,v in my_lib.iteritems():
#     print k, v
#
# for k,v in my_lib.iteritems():
#     print '\n{}: {}'.format(k,v)
#
# sentence = '{} has {} books written and {} movies exists. Their cummulative rating are all {}'.format(my_lib['Harry Potter'], my_lib['books'], my_lib['movies'], my_lib['ratings'])
# print sentence
#
# def loop(food):
#     for k,v in food.iteritems():
#         if k == 'books':
#             print '\nShe has a total of {}'.format(v)
#
# loop(my_lib)
#

def loopy_loop(dictionary):
	for k,v in dictionary.iteritems():
		if k == 'name':
			print 'Hello, {}'.format(v)

loopy_loop({'name': "T-Rex O'Farrel"})
