import re


__author__ = '@masterfung'


test = '<p id="title">Blog Post #1</p>'

def scrappy():
	f = open('scraping.html', 'r')
	all_file = f.read()
	w = open('result.txt', 'w')
	m = re.search('id="title".*?>(.*?)<', all_file)
	n = re.search('class="small-text".*?>(.*?)<', all_file)
	o = re.search('h4.*?>(.*?)<', all_file)
	if m:
		headline = m.group(1)
	if n:
		first = n.group(1)
	if o:
		second = o.group(1)
	w.write(headline + '\n')
	w.write(first + '\n')
	w.write(second + '\n' )
	return headline, first, second



substance = scrappy()
print substance