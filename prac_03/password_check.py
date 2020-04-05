"""
CP1404 Password Checker - Week 3 Practical
Program to get a users password and print it as asterisks
"""

MIN_LENGTH = 8


def main():
    get_password()


def get_password():
    """Ask user for a password and receive input as a string"""
    print("Please enter a valid password ({} Characters or longer)".format(MIN_LENGTH))
    password = str(input("> "))
    while not validate_password(password):
        print("Invalid Password - Does Not Meet Requirements")
        password = input("> ")
    print_password(password)


def print_password(password):
    """Print password in a particular format"""
    censored_password = "*" * len(password)
    print("Password Set ({} Characters): {}".format(len(password), censored_password))


def validate_password(password):
    """Validate password based on user input"""
    if len(password) < MIN_LENGTH:
        return False
    else:
        return True


main()
