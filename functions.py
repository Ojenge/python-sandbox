def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
    
    
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
		
def fact_iter(n):
	prod = 1
	
	for i in range(1, n+1):
		prod *=i
		
	return prod
	
	result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result