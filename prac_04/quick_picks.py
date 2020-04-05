"""
CP1404 - Week 4 Practical
Program to generate 'quick picks'
"""

import random


def main():
    num_quickpicks = get_quickpick_num()
    generate_quickpicks(num_quickpicks)


def get_quickpick_num():
    """Get the number of quick picks that the user wants to generate"""
    num_quickpicks = int(input("Enter the number of quick picks you would like: "))
    return num_quickpicks


def generate_quickpicks(num_quickpicks):
    """Generate quickpicks and print the output"""

    # Loop for the amount of quickpicks that were selected
    for x in range(1, num_quickpicks + 1):
        # Initialise lists that will be used within the function
        quickpick_list = []
        formatted_list = []

        # Within each quickpick - create a list of 6 random numbers
        for y in range(1, 7):
            # Create a random number and add to quick pick if it has not been repeated
            random_num = random.randint(1, 45)
            while random_num in quickpick_list:
                random_num = random.randint(1, 45)
            quickpick_list.append(random_num)

        # Sort the quickpick list in ascending order
        quickpick_list.sort()
        # Create formatted list with right alignment and number width of 2
        for item in range(len(quickpick_list)):
            formatted_list.append(("{:>2}".format(quickpick_list[item])))

        # Print list without brackets, commas or quotation marks
        print(*formatted_list)


main()
