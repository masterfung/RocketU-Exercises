import os

__author__ = '@masterfung'


# def create_directories(dirname):
# 	for name in dirname:
# 		os.mkdir(name)
#
# def create_nested_directories(dirname):
# 	for name in dirname:
# 		os.mkdir(name)
# 		os.chdir(name)
#
#
#
# dirnames = ['happy', 'brave', 'energy']
# create_directories(dirnames)
#
# good_names = ['squida', 'happi', 'bravis']
# create_nested_directories(good_names)

# file = open('hello_world.txt', 'r')
# for line in file:
#     print line
#
# file = open('hello_world.txt', 'r')
# for line in file:
#     print line.upper()


def find_words(line):
	results = line.readlines()
	result = map(lambda x: x.strip(), results)
	return result

file = open('hello_world.txt', 'r')
result = find_words(file)
print result

#-Instructor's Solution-#
def find_words(file_name):
	words = []
	file = open(file_name, 'r')
	for line in file:
		words = words + line.split()
	return words

print find_words('hello_world.txt')