test_tuple = ('I', 'am', 'a', 'test', 'tuple')

new_tuple = ()

size = len(test_tuple)

new_size = size + 1

#new_tuple = new_tuple + (test_tuple[2],)

#print(new_tuple)
	

for i in range(size):
	if i % 2 == 0:
		new_tuple = new_tuple + (test_tuple[i],)
		
	
	
	

print(new_tuple)

