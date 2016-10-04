#start the monthly payment amount at $10
balance = 4772
annualInterestRate = 0.2
monthlyPaymentRate = 10
oldBalance = balance
#get the monthly interest rate which is the annualInterestRate divided by 12
monthlyInterestRate = (annualInterestRate / 12)
while balance > 0:
    #oldBalance = balance
    

    for i in range(12):
        #unpaid balance at the end before interest
        unpaidBalance = balance - monthlyPaymentRate
        #interest on unpaid balance
        interest = unpaidBalance * monthlyInterestRate
    
        balance = unpaidBalance + interest
        
    
    if balance <=0:
    	
    	print("LowestPayment: " + str(monthlyPaymentRate))
    	break
    	
    else:
    	balance = oldBalance
    	monthlyPaymentRate += 10
    	
        