input("Please think of a number between 0 and 100! ")


high = 100
low = 0

guess = False

myguess = (high + low)/2


while not guess:
	
	myguess = int(myguess)
	
	print("Is your secret number " + str(myguess) + "?")
	
	result = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
	
	if result == "h":
		high = myguess
		
	elif result == "l":
		low = myguess
		
	elif result == "c":
		guess = True
		
		break
	else:
		print("Sorry, I did not understand your input.")
	
	myguess = (high + low)/2	
	
print("Game over. Your secret number was: " + str(myguess))
	
		