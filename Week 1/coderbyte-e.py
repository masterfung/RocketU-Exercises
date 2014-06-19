def LongestWord(sen):
	# code goes here
	text = "Code must be properly"
	more = " indented in Python!"
	new =  text + more
	longs = new.split(' ')
	for i in longs:
		print i

# keep this function call here‰
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())