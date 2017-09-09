balance = 320000
annualInterestRate = 0.2
fixedMonthlyPayment = 0
b = balance
upperBound = balance

lowerBound = balance / 12
for c in range(12):
    upperBound = upperBound + ( (annualInterestRate / 12) * upperBound )

while round(b,2) != 0.01:
    b = balance
    fixedMonthlyPayment = ((upperBound - lowerBound) / 2) + lowerBound
    for c in range(12):
        ub = b - fixedMonthlyPayment
        b = ub + ( (annualInterestRate / 12) * ub )

    if b < 0.01:
        upperBound = fixedMonthlyPayment
    elif b > 0.01:
        lowerBound = fixedMonthlyPayment

print("Lowest payment: " + str(round(fixedMonthlyPayment, 2)))
