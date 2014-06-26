import re
import csv

__author__ = '@masterfung'

class CSVtoHtml(object):
	
	def html_generator(self):
		with open('csv_html.html', 'w') as write_file:
			write_file.write('<h1>Welcome to Johnny\'s Page!</h1> \n')
			write_file.write('<html> \n')
		list = []
		with open('html.csv', 'rb') as html_file:
			for data in csv.reader(html_file):
				list.append(data)
			print list

		for index in list[1:]:
			print '<{}>{}</{}>'.format(index[1],
									index[3], index[1])


CSVtoHtml().html_generator()
