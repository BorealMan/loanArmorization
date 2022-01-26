import math

# Continuous Interest Formula
def calcContinuousLoan(p, i, t):
    e = 2.71828182845904
    return p * math.pow(e, i * t)

# NonContinuous Interest
def calcNonContinuousLoan(p, i, t, n):
    return p * math.pow(1 + i, t/n)

#  Two forumulas to calculated the monthly repayment for a mortgage
def calculateMonthlyMortgageRepayment(p, i, t):
    r = i /12
    n = t * 12
    return p*r*math.pow(1+r,n) / (math.pow(1+r,n)-1)

def calculateMonthlyMortgageRepaymentEZ(p , i, t):
    r = i /12
    n = t * 12
    return p * r / (1 - math.pow((1 + r), -1*n))

# Calculates the total Mortgage Repayment
def calculateTotalMortgageRepayment(monthlyPayment, years):
    totalPayments = years * 12
    return monthlyPayment * totalPayments

# Calculates How much is left after a number of years assuming constant inflation
def calcCumlativeInflation(p, inflationRateAverage, t):
    for x in range(0, t):
        p = p * (1-inflationRateAverage)
    return round(p, 2)

# Calculate the multiplier to figure out how much it takes to equal the starting value after the duration 
def calculateInflationMultiplier(inflationRate, t):
    return math.pow(1 + inflationRate, t)

def calculateInflationAdjustedMortgage(monthlyPayment, inflationRate, years):
    n = years * 12
    mInflation = inflationRate/12
    compoundInflation = 0
    total = 0
    for x in range(0, n):
        compoundInflation += mInflation
        total += monthlyPayment * (1 - compoundInflation)
    return total

# Prints Loan Details Assuming continuous interest
def printContinuousRepaymentDetails(p, i, t, inflationRate=.05):
    totalLoan = round(calcContinuousLoan(principal, interestRate, years), 2)
    print(f'\nBarrowing ${principal} for {years} years at {interestRate*100}%')
    print(f'\tTotal Repayment: ${totalLoan}')
    print(f'\tTotal Interest Repayed: ${round(totalLoan - principal, 2)}')
    print(f'\tInterest % of repayment: {round((totalLoan - principal)/principal*100, 2)}%')
    print(f'\t\tYearly Payment: ${round(totalLoan/years, 2)}')
    print(f'\t\tMonthly Payment: ${round(totalLoan/years/12, 2)}')
    print(f'\t\tWeekly Payment: ${round(totalLoan/years/12/4, 2)}')
    print()
    print(f'Estimated Inflation over {years} years: {inflationRate}%')
    print(f'\tValue of Principal Loan Repayment Inflation Adjusted: ${calcCumlativeInflation(p, inflationRate, years)}')
    print(f'\tValue of Toal Loan Repayment Inflation Adjusted: ${calcCumlativeInflation(totalLoan, inflationRate, years)}')
    print(f'\t\tLender Profit: ${round(calcCumlativeInflation(totalLoan, inflationRate, years) - p, 2)}')
    print()
    print(f'Value of principal assuming it tracks inflation: ${round(calculateInflationMultiplier(interestRate, t) * p, 2)}')

# Prints Loan Details For a Mortgage
def printMortgageRepaymentDetails(p, i, t, inflationRate):
    monthlyRepayment = calculateMonthlyMortgageRepaymentEZ(p, i, t)
    totalLoan = round(calculateTotalMortgageRepayment(monthlyRepayment, t), 2)
    inflationAdjustedRepayment = calculateInflationAdjustedMortgage(monthlyRepayment, inflationRate, t)
    inflationAdjustedPrincipal = calculateInflationMultiplier(inflationRate, t) * p
    print(f'\nBarrowing ${moneyFormat(principal)} for {years} years at {i*100}%')
    print(f'\tTotal Repayment: ${moneyFormat(totalLoan)}')
    print(f'\tTotal Interest Repayed: ${moneyFormat(totalLoan - principal)}')
    print(f'\tInterest % of repayment: {round((totalLoan - principal)/principal*100, 2)}%')
    print(f'\t\tYearly Payment: ${moneyFormat(totalLoan/years)}')
    print(f'\t\tMonthly Payment: ${moneyFormat(totalLoan/years/12)}')
    print(f'\t\tWeekly Payment: ${moneyFormat(totalLoan/years/12/4)}')
    print()
    print(f'Estimated Inflation over {years} years: {inflationRate}%')
    print(f'\tValue of Toal Loan Repayment Inflation Adjusted: ${moneyFormat(inflationAdjustedRepayment)}')
    print(f'\t\tLender Profit: ${moneyFormat(inflationAdjustedRepayment - p)}')
    print(f'\t\tLender Profit Inflation Adjusted: ${calcCumlativeInflation(inflationAdjustedRepayment - p, inflationRate, t)}')
    print()
    print(f'Value of principal assuming it tracks inflation: ${moneyFormat(inflationAdjustedPrincipal)}')
    print(f'\tInflation Adjusted Repayment: ${moneyFormat(inflationAdjustedRepayment)}')
    print(f'\t\tBarrower Maximum Margin: ${moneyFormat(inflationAdjustedPrincipal - inflationAdjustedRepayment)}')
    print(f'\t\tBarrower Max Margin Inflation Adjusted: ${calcCumlativeInflation(inflationAdjustedPrincipal - inflationAdjustedRepayment, inflationRate, t)}')
    print()

def commaFormat(number):
    return ("{:,}".format(number))
    
def moneyFormat(n):
    return commaFormat(round(n, 2))

if __name__ == '__main__':
    principal = 100000
    interestRate = .025
    years = 15
    inflationRate = .06

    printMortgageRepaymentDetails(principal, interestRate, years, inflationRate)
