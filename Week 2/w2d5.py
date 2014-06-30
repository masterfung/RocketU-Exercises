__author__ = '@masterfung'
#use in coordination with the Django app created on 6.27.14

def get_post_into(post_id):
	post = Post.objects.get(pk=post_id)
	return {
		'post_title': post.title,
		'author_name': post.author.name,
	}

print get_post_into(1)



def blog_post_title(author_id):
	author = Author.objects.get(pk=author_id)
	post_titles = []
	for post in author.posts.all():
		post_titles.append(post.titles)

	return post_titles

print blog_post_title(1)



def get_author_get_blog():
	authors = {}
	for author in Author.objects.all():
		author[author.twitter] = author.posts.count()
	return authors

print get_post_into()



#many to many

def post_id():
	return Post.objects.filter(tags__pk=1)

print post_id()



def return_post(post_id):
	post = Post.objects.get(pk=post_id)
	return post.tags.all()

print return_post(2)




def all_tags(): #dont understand very much
	tags = Tag.objects.filter(pk__gt=1)
	return tags.all()

all_tags()




def return_dict(): #unfinished
	authors = {}
	for author in Author.objects.all()
return_dict()

