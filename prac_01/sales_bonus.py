"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Loop Task - Add a loop to the sales bonus exercise you did below, so that the program repeatedly asks for the user's
# sales and prints the bonus until they enter a negative number.

PROMPT = "\nSales Bonus Calculator"
print(PROMPT)

valid_input = False
while not valid_input:
    try:
        sales = float(input("\nEnter Sales: $"))
        valid_input = True
    except ValueError:
        print("\nInvalid Entry")

while sales > 0:
    if sales < float(1000):
        bonus = sales * float(0.1)
        print("10% Bonus: $ {:.2f}".format(bonus))
    elif sales >= float(1000):
        bonus = sales * float(0.15)
        print("15% Bonus: $ {:.2f}".format(bonus))
    valid_input = False
    while not valid_input:
        try:
            sales = float(input("\nEnter Sales: $"))
            valid_input = True
        except ValueError:
            print("\nInvalid Entry")
print("Negative Number Entered")
