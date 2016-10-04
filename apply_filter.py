
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    #loop through L
    for i in L[:]:
    	y = g(f(i))
    	
    	if not y:
    		L.remove(i)
    	
    if not L:
    	return -1
    	
    else:
    	
    	return max(L)
    	  
    
def f(r):
    return r + 2
def g(r):
    return r > 5


L = [-1,-2,-3,-4,-5]

print(applyF_filterG(L,f,g))
print(L)

