import urllib2
import json

__author__ = '@masterfung'


locu_api = '3087e0fc27bb301c8483117369ae988e0b558f66'


def locu_search(query):
	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
	locality = query.replace(' ', '%20')
	final_url = url + '&locality=' + locality + '&category=restaurant'
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)

	for item in data['objects']:
		print 'Item is: ' + str(item)

	for item in data['objects']:
		print item['name'] #prints the key

	for item in data['objects']:
		print item['name'], item['phone']

locu_search('san francisco')