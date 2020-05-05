
def main():

    # Create email dictionary
    email_dict = {}

    # Get the email address
    user_email = prompt_string("Email: ")

    while user_email != "":
        # Get the user's name from the email address
        user_name = get_name_from_email(user_email)

        # Confirm the user's name based on our assumptions - Otherwise get them to enter the correct name
        confirmed_name = check_name(user_name)

        # Add value to dictionary
        add_to_dict(email_dict, user_email, confirmed_name)

        # Get a new email address
        user_email = prompt_string("Email: ")

    # User has stopped entering email addresses - Now print the dictionary items
    print_email_dict(email_dict, "vk")


def print_email_dict(dictionary, key_value_order):
    """Print dictionary items as key/values or values/keys depending on the order specified."""
    print("")
    key_value_order = key_value_order.lower()
    if key_value_order == "vk":
        for item in dictionary:
            print("{} ({})".format(dictionary[item], item))
    elif key_value_order == "kv":
        for item in dictionary:
            print("{} ({})".format(item, dictionary[item]))
    else:
        print("Debug - Key/Value order of '{}' entered as function parameter is incorrect".format(key_value_order))


def check_name(name):
    """Ask the user if their name is correct and give the option enter the correct name if it is not."""
    user_response = input("Is your name {}? (Y/n)".format(name))
    if user_response in ["n", "no"]:
        name = input("Enter Correct Name: ")
    return name


def add_to_dict(dictionary, key, value):
    """Add a key/value pair to a dictionary."""
    dictionary[key] = value


def prompt_string(prompt):
    """Promt the user for a string input"""
    string = input(prompt)
    return string


def get_name_from_email(email_address):
    """Use string manipulation to get the assumed name of a user based on their email address."""
    # Get the email address by getting the first item before the at symbol as a string
    email_alias = email_address.split("@")[0]
    # If there is a full stop in the alias - Get the values on each side and put in to a list
    email_name_list = email_alias.split(".")
    # Declare the separtor variable then join the names on the email list together using that separator
    separator = " "
    email_name = separator.join(email_name_list)
    # Convert the name to title-case
    email_name = email_name.title()
    return email_name


main()

