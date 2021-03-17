"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

if sales < 1000:
    # calculate bonus when under 1000
    bonus = sales * 0.1
    print("Your bonus is $", bonus)
else:
    # calculate bonus when 1000 or over
    bonus = sales * 0.15
    print("Your bonus is $", bonus)
