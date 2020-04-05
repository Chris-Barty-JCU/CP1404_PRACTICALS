"""
CP1404 - Week 3 Practical
Program to convert between degrees Celsius and Fahrenheit
"""


def main():
    conversion_menu = """        TEMPERATURE CONVERSION TOOL
        C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius
        Q - Quit"""
    print(conversion_menu)
    menu_option = input("Option: ").upper()

    while menu_option != "Q":
        if menu_option == "C":
            user_temp = get_temp()
            converted_temp = convert_celsius_fahrenheit(user_temp)
            print("{:.2f} Degrees Celsius = {:.2f} Degrees Fahrenheit".format(user_temp, converted_temp))
            menu_option = input("Option: ").upper()
        elif menu_option == "F":
            user_temp = get_temp()
            converted_temp = convert_fahrenheit_celsius(user_temp)
            print("{:.2f} Degrees Fahrenheit = {:.2f} Degrees Celsius".format(user_temp, converted_temp))
            menu_option = input("Option: ").upper()
        else:
            print("Invalid Option - Choose Again")
            menu_option = input("Option: ").upper()


def get_temp():
    user_temp = float(input("Temperature: "))
    return user_temp


def convert_celsius_fahrenheit(temperature):
    fahrenheit = temperature * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_celsius(temperature):
    celsius = 5 / 9 * (temperature - 32)
    return celsius


main()
