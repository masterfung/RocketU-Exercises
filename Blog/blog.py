__author__ = '@masterfung'

class BlogPost(object):
	def __init__(self, title, published_date, author=None):
		self.title = title
		self.content = ''
		self.published_date = published_date
		self.author = author

	def __repr__(self):
		return self.title


