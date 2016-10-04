balance = 320000
annualInterestRate = 0.2
oldBalance = balance

#get the monthly interest rate which is the annualInterestRate divided by 12
monthlyInterestRate = (annualInterestRate / 12)

#lower bound
low = (balance)/12.0

#upper bound for the payment
high = (balance * (1 + monthlyInterestRate)**12) / 12.0

epsilon = 0.01

while abs(balance) > epsilon:
	#reset the balance after every iteration
	balance = oldBalance
	#get the new payment rate with every iteration
	monthlyPaymentRate = ((high-low)/2.0) + low
	
	
	#check if the new rate will ensure the balance is paid up within 12 months
	for i in range(12):
		#reduce the balance for every month
		balance -= monthlyPaymentRate
		
		balance *= 1 + monthlyInterestRate
		
		
	if balance > 0:
		low = monthlyPaymentRate
	else:
		high = monthlyPaymentRate
		
print("Lowest Payment: " +str(round(monthlyPaymentRate,2)))	
	
