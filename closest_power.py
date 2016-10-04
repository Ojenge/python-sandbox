def closest_power(base, num):
	#the exponent
	exp = 0
	#the desired result
	result = 0
	#loop to get the exponent
	while base > 0:
		
		if num - base**exp <= base**(exp+1) - num:
			result = exp 
			break
			
		else:
			#increment the exponent by if the condition is not met
			exp +=1
			
	#return the result	
	return result
	
print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
	