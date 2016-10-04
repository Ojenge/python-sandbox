def biggest(aDict):
	'''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    #first check if the dictionary is empty
	if len(aDict.keys()) != 0:
		values = aDict.values()
		max_val = max(values)
		result = list(animals.keys())[list(animals.values()).index(max_val)]
		
		return result
		
	else:
		return None
		
	


animals = {'c': ['coati'], 'b': ['baboon'], 'a': ['aardvark'], 'd': ['donkey', 'dog', 'dingo']}

print(biggest(animals))