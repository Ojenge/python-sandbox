def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    #initialize the two dictionaries to be returned
    intersect = {}
    difference = {}
    result = ()
    
    for n in d1.keys():
    	if (n in d1) & (n in d2):
    		x = f(d1[n],d2[n])
    		intersect[n] = x
    	elif (n in d1) & (n not in d2):
    		difference[n] = d1[n]
    		
    #second loop to pick the keys for d2 not in d1
    for k in d2.keys():
    	if (k in d2) & (k not in d1):
    		difference[k] = d2[k]
    		
    result = (intersect, difference)
    		
    		
    return result
    
def f(a,b):
	return a + b
	

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))