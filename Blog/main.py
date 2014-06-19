import sys
from author import Author

__author__ = '@masterfung'


def blog_manager(user, blog_posts, authors):
	action = raw_input('Would you like to (a)dd a post or (s)ee existing posts? ').lower()
	if action == 'a':
		is_author = raw_input('Are you the author of this post? (Y/N) ').lower()
		if is_author == 'y':
			author = user
		else:
			author_name = raw_input('What is your name? ')
			author = Author(author_name)
			authors.append(author)
		title = raw_input('What is the title? ')
		published_date = raw_input('When was this published? ')
		b = author.write_blog_post(title, published_date) #user is the author
		blog_posts.append(b)
		print 'Congrats! Your post has been posted about {}.'.format(b.title)
		blog_manager(user, blog_posts, authors)
	elif action == 's':
		print blog_posts
		blog_manager(user, blog_posts, authors)
	elif action == 'q':
		print 'Have a good day!'
	else:
		print 'Please select correctly from above.'

print 'Hey! Welcome to the blog manager {}.'.format(sys.argv[1]) #sys.argv[0] is the file name

user = Author(sys.argv[1])
blog_posts = []
authors = [user]
blog_manager(user, blog_posts, authors)