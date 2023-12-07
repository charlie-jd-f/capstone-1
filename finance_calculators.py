# Python programme which allows use to access an investment calculator
# and a home loan calculator
#
# Pseudo code given in finance_calculators_pseudo.txt file in same folder

import math

# Print text to give instructions to the user

print("Hello!")
print()
print("Which calculation would you like to perform?")
print()
print("Investment:")
print ("To calculate the amount of interest you'll earn on your investment")
print()
print("Bond:")
print("To calculate the amount you'll have to pay on a home loan")
print()
print("To perform a calculation please type 'investment' or 'bond'.")

# Request calculation user wants to perform. Change user input to lowercase
# to avoid any errors involving upper and lower case

calculation = input("")
calculation = calculation.lower()

if calculation == "investment":

    # User inputs the variables required to perform the calculation
    # P = the amount the user is depositing
    # r = the interest rate (divide by 100 to convert to decimal)
    # t = the number of years the money is being invested

    print()
    P = float(input("How much money will you be depositing? "))
    r = float(input("Enter the % interest rate: "))/100
    t = int(input("How many years do you plan on investing? "))

    # Ask user if they would like to work out simple or compound interest
    print()
    interest = input("Would you like to find 'simple' interest or " \
                     "'compound' interest? ")
    interest = interest.lower()
    
    # Calculate the simple interest
    if interest == "simple":

        A = int(P*(1+r*t))

    # Calculate the compound interest
    elif interest == "compound":

        A = int(P*math.pow((1+r),t))

    # Error message if user has not typed 'simple' or 'compound'
    else:
        print()
        print("Input Error: Please try again using 'simple' or 'compound' " \
          "as your input.")

    print()
    print(f"You will return £{A} after investing £{P} for {t} years")
    print()
    print("Thank you for using the fincance calculator!")

elif calculation == "bond":

    # User inputs the variables required to perform the calculation
    # P = present value of the house
    # i = monthly interest rate
    #     (input value is annual so is divided by 100, then divided by 12)
    # n = the number of repayment months
    
    print()
    p = float(input("Enter the present value of the house: "))
    i = float(input("Enter the annual interest rate: "))/(100*12)
    n = int(input("How many months do you plan to repay" \
                             " the bond? "))

    # Calculcate the amount to repay each month   
    repayment = int((i*p)/(1-(1+i)**(-n)))

    print()
    print(f"You will have to repay £{repayment} each month")
    print()
    print("Thank you for using the finance calculator!")

# Error message if user has not typed 'investment' or 'bond'
else:
    print()
    print("Input Error: Please try again using 'investment' or 'bond' " \
          "as your input.")


