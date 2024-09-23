"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $"))

while sales >= 0:
    if sales >= 1000:
        sales_bonus = sales * 0.15
    else:
        sales_bonus = sales * 0.10

    print(f"Your sales bonus is: {sales_bonus}")
    sales = float(input("Enter Sales: $"))

print("See you next time!")
