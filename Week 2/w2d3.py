import os
import re

__author__ = '@masterfung'


# def create_directories(dirname):
# for name in dirname:
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

#-End-#

lines = [
	'First line\n',
	'Second line\n',
	'Third line\n'
]

file = open('script.txt', 'w')
for line in lines:
	file.write(line)
file.close()



def reversing():
	goods = [
	'This is an example text file.\n',
	'It should have its order reversed.\n',
]

	final = []
	final = goods[0].split()
	good = final[::-1]
	good = ' '.join(good)

	print good
	with open('final.txt', 'w') as file:
		file.writelines(good)

reversing()

#-Regex-#

bibliography = "James, Henry. The Ambassadors. Rockville: Serenity, 2009-2010. Print."
rep = re.findall(r'\d{4}', bibliography)
print rep

correct_email = "r.mutter@gmail.com"
wrong_email = "r.mutter@yahoo,com"
another_wrong_email = "r.mutteratgmail.com"
signup_info = "Jenny: jenny@gmail.com, 867-5309"

def finding_email(input):
	email = re.findall(r'\w+@\w+\.com', input)
	print email

#_Rudy's_#
def find_email_address(info):
	return re.findall(r'([A-Za-z0-9\.\+_-]+@\w+\.\w+)', info)

print find_email_address(signup_info)

finding_email(wrong_email)




