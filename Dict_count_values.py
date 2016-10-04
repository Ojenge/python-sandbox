def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    keys = aDict.keys()
    #count holds the number of values
    count = 0
    
    for i in keys:
    	count = count + len(aDict[i])
    	
    
    return count
    

    
animals = {'c': ['coati'], 'b': ['baboon'], 'a': ['aardvark'], 'd': ['donkey', 'dog', 'dingo']}
print(how_many(animals))

