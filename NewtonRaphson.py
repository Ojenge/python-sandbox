#how accurate I want the solution
epsilon = 0.00001

#number I am getting the square root of
y = 13

guess = y/2.0

#number of guesses I shall make
numGuesses = 0

while abs(guess * guess - y) >= epsilon:
	numGuesses +=1
	
	guess = guess - (((guess ** 2) - y)/(2 * guess))
	
print('Number of Guesses: ' + str(numGuesses))
print('Square Root of ' + str(y) + 'is about: ' + str(guess))

