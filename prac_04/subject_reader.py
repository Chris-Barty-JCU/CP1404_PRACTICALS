"""
CP1404 - Week 4 Practical
Program to display data from a list import in different ways
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print("----------")
    print_detailed_summary(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)

        print(parts)  # See if that worked
        print("----------")
        list_data.append(parts)
    input_file.close()
    return list_data


def print_detailed_summary(data):
    """Print detailed summary based on list data given and format output spacing"""
    longest_name = 0
    # Determine longest name for width formatting
    for item in data:
        if len(item[1]) > longest_name:
            longest_name = len(item[1])
    # Print formatted data
    for item in data:
        print("{} is taught by {:{width}} and has {:>3} students".format(item[0], item[1], item[2], width=longest_name))


main()
