"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_month."""
    incomes = []
    number_of_month = int(input("How many number_of_month? "))

    for month in range(1, number_of_month + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print(f"Income Report is: ")
    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()