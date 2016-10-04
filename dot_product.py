def dotProduct(listA, listB):
    #the variable that will hold the result
	result = 0
    
    #loop through the lists in parallel
    #assuming that both lists are the same length
    #only need one loop to achieve the desired result
    
	for i in range(len(listA)):
		result = result + (listA[i]*listB[i])
    	
	return result
	
A = [1,2,3]
B = [4,5,6]
print(dot_product(A, B))
    
    
    	