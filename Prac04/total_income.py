"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    """This variable stores the counting number of months"""
    month_for_counting = int(input("How many months? "))
    for month in range(1, month_for_counting + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes, month_for_counting)


def print_report(incomes, month_for_counting):
    """This function will print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_for_counting + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month} - Income: ${income: .2f} Total: ${total: .2f}")


main()
