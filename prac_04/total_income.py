"""
CP1404 - Week 4 Practical
Program to calculate a list of cumulative totals
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_count = int(input("How many months? "))

    for month in range(1, month_count + 1):
        income = float(input("Enter income for month {}: ".format(str(month))))
        incomes.append(income)

    print_income_report(incomes, month_count)


def print_income_report(incomes, month_count):
    """Print income report based on incomes and number of months"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_count + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
