import re
import csv

__author__ = '@masterfung'


class CSVtoHtml(object):
	def styles(self):

		styling = {
			"h1": "red",
			"p": "#363cff",
		}
		for k, v in styling.items():
			css = "{} {}".format(k, '{') + "\n\t\t\t{}: {}{}".format('color', v, '}')
			return css

	def closing_div(self):
		return '</div>\n'

	def closing_html(self):
		return '</html>'

	def head(self):
		styles = self.styles()
		return '\t<head>\n\t\t<style>\n\t\t{}\n\t\t</style>\n\t</head>\n'.format(styles)

	def html_generator(self):
		list = []
		string = []
		with open('html.csv', 'rb') as html_file:
			for data in csv.reader(html_file):
				list.append(data)
			print list
			previous = list[1][1]
			styling = self.head()
			closing_div = self.closing_div()
			closing_html = self.closing_html()
			s = '<h2>Hello World[http://savthecoder.com/blog/images/fry_notsure.png]!</h2>'
			output = re.sub(r'<h2.*>(.*)</h2>',
							"<a href='http://savthecoder.com/blog/images/fry_notsure.png'><h2>Hello World </h2></a>", s)
			print s, output
			if previous == 'div':
				str = '{}<{}>\n'.format('\t', previous)
				string.append(str)
			if list[2][1] == 'h2':
				str = '{}<{}>{}</{}>\n'.format('\t\t', list[2][1],
											   list[2][3], list[2][1])
				string.append(str)
			if list[3][1] == 'p':
				str = '{}<{}>{}</{}>\n'.format('\t\t', list[3][1],
											   list[3][3], list[3][1])
				string.append(str)
			if list[4][1] == 'div':
				str = '{}<{}>\n'.format('\t\t', list[4][1])
				string.append(str)
			if list[5][1] == 'h3':
				str = '{}<{}>{}</{}>\n'.format('\t\t\t', list[5][1],
											   list[5][3], list[5][1])
				string.append(str)
			if list[6][1] == 'span':
				str = '{}<{}>{}</{}>\n'.format('\t\t\t', list[6][1],
											   list[6][3], list[6][1])
				string.append(str)
				string.append('\t' + '\t' + closing_div)
			if list[7][1] == 'div':
				str = '{}<{}>\n'.format('\t\t', list[7][1])
				string.append(str)
			if list[8][1] == 'p':
				str = '{}<{}>{}</{}>\n'.format('\t\t\t', list[8][1],
											   list[8][3], list[8][1])
				string.append(str)
				string.append('\t' + '\t' + closing_div)
			if list[9][1] == 'div':
				str = '{}<{}>{}</{}>\n'.format('\t\t', list[9][1],
											   list[9][3], list[9][1])
				string.append(str)
				string.append('\t' + closing_div)
				string.append(closing_html)
		with open('csv_html.html', 'w') as write_file:
			write_file.write('<html> \n')
			write_file.writelines(styling)
			write_file.write('\t<h1>Welcome to Johnny\'s Page!</h1> \n')
			write_file.writelines(string)


CSVtoHtml().html_generator()
