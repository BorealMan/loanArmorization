import math

e = 2.71828182845904

def calcLoan(p, i, t):
    return p * math.pow(e, i * t)

def printRepaymentDetails(p, i, t):
    totalLoan = round(calcLoan(principal, interestRate, years), 2)
    print(f'\nBarrowing ${principal} for {years} years at {interestRate*100}%')
    print(f'\tTotal Repayment: ${totalLoan}')
    print(f'\tTotal Interest Repayed: ${round(totalLoan - principal, 2)}')
    print(f'\tInterest % of repayment: {round((totalLoan - principal)/principal*100, 2)}%')
    print(f'\t\tYearly Payment: ${round(totalLoan/years, 2)}')
    print(f'\t\tMonthly Payment: ${round(totalLoan/years/12, 2)}')
    print(f'\t\tWeekly Payment: ${round(totalLoan/years/12/4, 2)}')
    print()


if __name__ == '__main__':
    principal = 24000
    interestRate = .048
    years = 7

    printRepaymentDetails(principal, interestRate, years)

