"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Martha Cawood
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

while True:
    try:
        monthlySavings = int(input("Enter how much you want to save each month: "))
        break 
    except ValueError:
        print("You have not entered a number")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearlyTotal = monthlySavings * 12
print(f"You will have saved £{yearlyTotal} in one year")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

totalInterest = yearlyTotal * 1.008
roundedNumber = round(totalInterest, 2)
print(f"Your total savings after interest will be £{roundedNumber} in one year")
