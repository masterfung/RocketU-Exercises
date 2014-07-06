__author__ = '@masterfung'


import os
import csv
import random
import string

# currentdirpath = os.getcwd()
# filename = 'hobbies.csv'
# file_path = os.path.join(os.getcwd(), filename)

def get_file_path(filename):
	currentdirpath = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename)
	return file_path

def read_csv(filepath):
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			print row[2]

path = get_file_path('hobbies.csv')
read_csv(path)
