import math

import locale
locale.setlocale(locale.LC_ALL, '')

#Creates menu for user to reference
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan\n")

#Request the user to choose which calculation required
choice = input("Please enter 'Investment' or 'Bond' from the menu above to proceed:\n").lower()

#Requests user to input the details required for investment calculations
if choice == "investment":
    deposit_amount = float(input("Please enter the amount you wish to deposit:\n"))
    interest_rate = float(input("Please enter the percentage of the interest rate (without percentage sign):\n"))
    interest_rate = interest_rate / 100
    years = float(input("Please enter the number of years you wish to invest:\n"))
    interest = input("Please enter if you would like 'Simple' or 'Compound' interest:\n").lower()

#Investment calculations based on user input based on simple or compound interest
    if interest == "simple":
        total = deposit_amount * (1 + interest_rate * years)
        total = locale.currency(total, grouping=True)     #Formats to show currency
        print (f"You will receive {total} after a period of {years} years")
    elif interest == "compound":
        total = deposit_amount * math.pow(1 + interest_rate , years)
        total = locale.currency(total, grouping=True)     #Formats to show currency
        print (f"You will receive {total} after a period of {years} years")
    else :
        print("Please enter valid interest type, 'Simple' or 'Compound'")

#Requests user to input the details required for bond calculations
elif choice == "bond":
    house_value = float(input("Please enter the current value of your house:\n"))
    interest_rate = float(input("Please enter the interest rate (without the percentage sign):\n"))
    interest_rate = interest_rate / 100
    monthly_interest_rate = interest_rate / 12
    months = int(input("Please enter the number of months you will take to repay the bond:\n"))

#Bond calculations based off user input
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-months))
    repayment = locale.currency(repayment, grouping=True)     #Formats to show currency
    print(f"The monthly repayment will be {repayment} over {months} months")

#Error message if the the user performs an invalid entry
else:
    print("Invalid entry. Please enter 'Investment' or 'Bond'")
