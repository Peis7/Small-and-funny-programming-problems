#given a string, return the first recurring character 
#'abcdedsds'->return 'd'
#'sduyusduy'->returns 'u'
#'asdfgh'->return None
def firstRecurringChar(string):
	charCount = dict({})
	for char in string:
		if charCount.get(str(char),False):
			return char
		charCount.update({char:1})
	return None
	
print(firstRecurringChar("fddfdsdfhksdhfkj"))