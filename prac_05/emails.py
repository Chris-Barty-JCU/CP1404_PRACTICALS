
# Create email dictionary
email_dict = {}

# Get the email address
email_address = input("Email: ")

# Convert the email address to title-case
email_address = email_address.title()

# Get the email address by getting the first item before the at symbol as a string
email_alias = email_address.split("@")[0]

# If there is a full stop in the alias - Get the values on each side and put in to a list
email_name_list = email_alias.split(".")

# Declare the separtor variable then join the names on the email list together using that separator
separator = " "
email_name = separator.join(email_name_list)

print("Is your name {}? (Y/n)".format(email_name))

