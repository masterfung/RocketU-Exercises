from blog import BlogPost

__author__ = '@masterfung'

class Author(object):
	def __init__(self, name):
		self.name = name
		self.blog_posts = []

	def __repr__(self):
		return self.name

	def write_blog_post(self, title, published_date, content):
		b = BlogPost(title, published_date, content, self)
		self.blog_posts.append(b)
		return b

# cslewis = Author('CS Lewis')
# jack_london = Author('Jack London')
# bobsleigh = Author('Bob Sleigh')
#
# post1 = cslewis.write_blog_post('How to Train Your Dragon 2', 2014)
# post2 = cslewis.write_blog_post('How to Train Your Dragon', 2012)
# post3 = bobsleigh.write_blog_post('The Olympic Sport', 1870)
#
# print jack_london.blog_posts, cslewis.blog_posts