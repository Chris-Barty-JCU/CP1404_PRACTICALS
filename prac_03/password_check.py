"""
CP1404 Password Checker - Week 3 Practical
Program to get a users password and print it as asterisks
"""

MIN_LENGTH = 10


def main():
    user_password = get_password()
    while not validate_password(user_password):
        print("Invalid Password - Does Not Meet Requirements")
        user_password = get_password()
    print_password(user_password)


def get_password():
    """Ask user for a password and receive input as a string"""
    print("Please enter a valid password ({} Characters or longer)".format(MIN_LENGTH))
    password = str(input("> "))
    return password


def print_password(password):
    """Print password in a particular format"""
    censored_password = "*" * len(password)
    print("Password Set ({} Characters): {}".format(len(password), censored_password))


def validate_password(password):
    """Validate password based on user input"""
    if len(password) >= MIN_LENGTH:
        return True
    else:
        return False


main()
