# NAMES FILE TASK

# Name Input & Output Files

OUTPUT_FILE_NAMES = "name.txt"
INPUT_FILE_NAMES = "name.txt"

# Prompt for user's name

user_name = input("Please enter your name: ")

# Open name file in write mode, print the users' name to the file, then close the file

out_file = open(OUTPUT_FILE_NAMES, 'w')
print(user_name, file=out_file)
out_file.close()

# Open name file in read mode, read back the user's name to them, then close the file

in_file = open(INPUT_FILE_NAMES, 'r')
print("Your name is " + in_file.readline())
in_file.close()

# NUMBERS FILE TASK

# Numbers Input & Output Files

OUTPUT_FILE_NUMBERS = "numbers.txt"
INPUT_FILE_NUMBERS = "numbers.txt"

# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
# which should be... 59.

in_file = open(INPUT_FILE_NUMBERS, 'r')
file_numbers_list = in_file.readlines()
num_total = 0

for num in file_numbers_list[:2]:
    num_total = num_total + int(num)
print("Total of the first 2 numbers in the test file is: {}".format(num_total))
in_file.close()

# Open file in read mode, read the lines into a list, add the items in the list together, display total, close file
# Reading the numbers to a list, then adding together by iterating with a for loop caters for any amount of numbers

in_file = open(INPUT_FILE_NUMBERS, 'r')
file_numbers_list = in_file.readlines()
num_total = 0
for num in file_numbers_list:
    num_total = num_total + int(num)
print("Total of the numbers in the test file is: {}".format(num_total))
in_file.close()
