def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    #create variable to hold the flattened list
    result = []
    #loop through the individual elements in the List
    for i in aList:
    	#is the current i an object of type list?
    	if not isinstance(i, list):
    		#if not append it to result
    		result.append(i)
    	#instead of appending us extend
    	else:
    		result.extend(flatten(i))
    		
    	
    return result
    		 
    
    
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
result = []

print(flatten(aList))

