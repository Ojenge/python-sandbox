balance = 320000
annualInterestRate = 0.2
oldBalance = balance

#get the monthly interest rate which is the annualInterestRate divided by 12
monthlyInterestRate = (annualInterestRate / 12)

while balance > 0:
	#upper bound for the payment
	high = (balance * (1 + monthlyInterestRate)^12) / 12.0
	
	#lower bound
	low = balance/12
	#get the new payment rate with every iteration
	monthlyPaymentRate = (high+low)/2
	
	#check if the new rate will ensure the balance is paid up within 12 months
	for i in range(12):
		
		#unpaid balance at the end before interest
		unpaidBalance = balance - monthlyPaymentRate
		
		#interest on unpaid balance
        interest = unpaidBalance * monthlyInterestRate
        
        balance = unpaidBalance + interest
        
	if balance <= 0.1:
    	print("LowestPayment: " + str(monthlyPaymentRate))
    	break
    	
    else:
    	balance = oldBalance
    	monthlyPaymentRate += 0.1
