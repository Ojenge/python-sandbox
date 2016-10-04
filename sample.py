balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

low = balance / 12

high = (balance * (1 + annualInterestRate / 12) ** 12) / 12

originalBalance = balance

epsilon = 0.01 # Error margin e.g. $0.01

# Keep testing new payment values until the balance is +/- lowestBalance
while abs(balance) > epsilon:
    # Reset the value of balance to its original value
    balance = originalBalance
    # Calculate a new monthly payment value from the bounds
    payment = (high - low) / 2 + low

    # Test if this payment value is sufficient to pay off the entire balance in 12 months
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    # Reset bounds based on the final value of balance
    if balance > 0:
        # If the balance is too big, need higher payment so we increase the lower bound
        low = payment
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        high = payment

# When the while loop terminates, we know we have our answer!
print ("Lowest Payment: " +str(round(payment, 2)))