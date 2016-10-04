
def monthly(balance, annualInterestRate, monthlyPaymentRate):
	
	#get the monthly interest rate which is the annualInterestRate divided by 12
	
	monthlyInterestRate = (annualInterestRate / 12)
	
	
	for i in range(12):
		
		#minimum payment to be made
		minimumPayment = balance * monthlyPaymentRate
		
		#unpaid balance at the end before interest
		unpaidBalance = balance - minimumPayment
		
		#interest on unpaid balance
		interest = unpaidBalance * monthlyInterestRate
		
		balance = unpaidBalance + interest
		
		print("Month " + str(i + 1) +" Remaining balance:" + str(round(balance,2)))
		
	return print("Remaining balance: " + str(round(balance,2)))
	
monthly(42, 0.2, 0.04)