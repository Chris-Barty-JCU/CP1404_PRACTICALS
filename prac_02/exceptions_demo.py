"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_denominator = False
while not valid_denominator:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Invalid Denominator - Cannot Divide By 0 - Enter numbers again")
        else:
            valid_denominator = True
            fraction = numerator / denominator
            print(fraction)
            print("Finished.")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

# This last part of the code is not needed now that there is a check for a 0 denominator value
"""   
    except ZeroDivisionError:
       print("Cannot divide by zero!")
"""

# When will a ValueError occur?
# Answer: When a non-integer value is entered for the numerator, or the numerator had an integer entered but the
# denominator had a non-integer value entered

# When will a ZeroDivisionError occur?
# Answer: When the numerator is an integer and the denominator is 0

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: Yes - See changes above. Used boolean validation.
