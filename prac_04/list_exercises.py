"""
CP1404 - Week 4 Practical
Program to prompt user for numbers and output various statistics
"""


def main():
    # Part 1 - Basic list operations
    num_list = get_numbers()
    display_statistics(num_list)

    # Part 2 - Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = get_username()
    check_access(username, usernames)


def get_numbers():
    """Get 5 numbers from the user and store as a list"""
    num_list = []
    for x in range(1, 6):
        input_number = float(input("Enter number {} of 5: ".format(x)))
        num_list.append(input_number)
    return num_list


def display_statistics(num_list):
    """Display various statistics based on the numbers in a list"""
    for item in num_list:
        print("Number: {}".format(item))
    print("The first number is {}".format(num_list[0]))
    print("The last number is {}".format(num_list[-1]))
    print("The smallest number is {}".format(min(num_list)))
    print("The largest number is {}".format(max(num_list)))
    print("The average of the numbers is {}".format(sum(num_list) / len(num_list)))


def get_username():
    """Get the username from a user"""
    username = input("Enter your username: ")
    return username


def check_access(username, user_list):
    """Check if a username is in a list of users and print access level"""
    if username in user_list:
        print("Access Granted")
    else:
        print("Access Denied")


main()
