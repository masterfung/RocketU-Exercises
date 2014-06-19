#from author import Author

__author__ = '@masterfung'

class BlogPost(object):
	def __init__(self, title, published_date, author=None):
		self.title = title
		self.content = ''
		self.published_date = published_date
		self.author = author

	def __repr__(self):
		return self.title

	def change_author(self, new_author):
		change_a = self.author
		change_a.blog_posts.remove(self)
		new_author.blog_posts.append(self)
		self.author = new_author

