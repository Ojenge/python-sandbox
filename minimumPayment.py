def monthly(balance, annualInterestRate, monthlyPaymentRate):
	
	oldBalance = balance
	#get the monthly interest rate which is the annualInterestRate divided by 12
	
	monthlyInterestRate = (annualInterestRate / 12)

	#monthlyPaymentRate = 10
	
	for i in range(12):
		#unpaid balance at the end before interest
		unpaidBalance = balance - monthlyPaymentRate
		
		#interest on unpaid balance
		interest = unpaidBalance * monthlyInterestRate
		
		balance = unpaidBalance + interest
		
	#return balance
		
	if balance <= 0:
		return print("LowestPayment: " + str(monthlyPaymentRate))		
			
	else:
		balance = oldBalance
		return monthly(balance, annualInterestRate, monthlyPaymentRate+ 10)

	
monthly(4773, 0.2, 10)
	
			