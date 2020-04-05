"""
CP1404 Password Checker - Week 3 Practical
"""

MIN_LENGTH = 8


def main():
    """Program to get a users password and print it as asterisks"""
    print("Please enter a valid password ({} Characters or longer)".format(MIN_LENGTH))
    password = str(input("> "))
    while not password_validation(password):
        print("Invalid Password - Does Not Meet Requirements")
        password = input("> ")
    password_display = "*" * len(password)
    print("Password Set ({} Characters): {}".format(len(password), password_display))


def password_validation(password):
    """Determine if the provided password is valid"""
    if len(password) < MIN_LENGTH:
        return False
    else:
        return True


main()
