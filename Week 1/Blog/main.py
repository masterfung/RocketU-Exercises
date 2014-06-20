__author__ = '@masterfung'


def blog_manager(user, blog_posts, authors):
	action = raw_input('Would you like to (a)dd a post, (s)ee existing posts, add c(h)ange existing posts? ').lower()
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
		content = raw_input('Please add content here: ')

		b = author.write_blog_post(title, published_date, content) #user is the author
		blog_posts.append(b)
		print 'Congrats! Your post has been posted about {}. Here is your content: {}'.format(b.title, content)
		blog_manager(user, blog_posts, authors)
	elif action == 's':
		for post in blog_posts:
			print 'This is the title: {}.'.format(post)
			print 'Content: {}\n'.format(post.content)
		blog_manager(user, blog_posts, authors)
	elif action == 'q':
		print 'Have a good day!'
	elif action == 'h':
		for index,post in enumerate(blog_posts):
			print 'This is the title: {}. Reference: {}.'.format(post, index+1)

		user_num = int(raw_input('What is the index number? '))-1

		follow_up = raw_input('What would you like to change: (d)ate, (a)uthor, (t)itle, or (c)ontent ').lower()
		if follow_up == 'd':
			new_date = raw_input('What is the new year? ')
			blog_posts[user_num].published_date = new_date
		elif follow_up == 'a':
			author_name = raw_input('What is your name? ')
			author = Author(author_name)
			authors.append(author)
			blog_posts[user_num].change_author(author)
		elif follow_up == 't':
			new_title = raw_input('New title name: ')
			blog_posts[user_num].title = new_title
		elif follow_up == 'c':
			new_content = raw_input('New content: ')
			blog_posts[user_num].content = new_content
	else:
		print 'Please select correctly from above.'
	blog_manager(user, blog_posts, authors)

print 'Hey! Welcome to the blog manager {}.'.format(sys.argv[1]) #sys.argv[0] is the file name

user = Author(sys.argv[1])
blog_posts = []
authors = [user]
blog_manager(user, blog_posts, authors)