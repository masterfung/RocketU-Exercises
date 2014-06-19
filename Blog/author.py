from blog import BlogPost
__author__ = '@masterfung'

class Author(object):
	def __init__(self, name):
		self.name = name
		self.blog_posts = []

	def __repr__(self):
		return self.name

	def write_blog_post(self, title, published_date):
		b = BlogPost(title, published_date, self)
		self.blog_posts.append(b)
		return b
