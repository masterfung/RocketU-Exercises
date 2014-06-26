import random
import csv

__author__ = '@masterfung'

#unfinished
# def quiz_generator():
# 	questions = []
# 	with open('quiz.csv', 'rb') as file:
# 		for row in csv.reader(file):
# 			user_choice = raw_input('Do you want to answer (G)eography, (H)istory, (S)cience, or (T)echnology? ')
# 			if user_choice == row[1]:
# 				print 'yeah'
# 			else:
# 				print 'wow'
#
# quiz_generator()



#need to review deeply
def get_list_of_powers(number, power=5):
	return [number, number**2, number**3, number**4, number**5]

def create_powers_csv(number_list):
	header = ['1st', '2nd', '3rd', '4th', '5th']
	with open('powers.csv', 'wb') as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow(header)

		for number in number_list:
			powers = get_list_of_powers(number)
			csv_writer.writerow(powers)

create_powers_csv([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])