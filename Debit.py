
duration = 12
for month in range(duration):
    minpayment = monthlyPaymentRate * balance
    balance = balance - minpayment
    balance = ((annualInterestRate/12) * balance) + balance
    balance =round(balance,2)
#print("Month {0} Remaining balance: {1}".format(month+1, balance))
print("Remaining balance: ", balance)



