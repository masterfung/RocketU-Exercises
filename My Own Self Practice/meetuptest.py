__author__ = 'htm'


import urllib2
import json

# Create your models here.

def meetup_api_find_group():
	meetup_api_key = '1c636c32173023181ddd632e1a6156'

	url = 'http://api.meetup.com/topics/?' + meetup_api_key + '&page=1'
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)

	for item in data['objects']:
		print "Test: " + str(item)

meetup_api_find_group()


def test():
	pass