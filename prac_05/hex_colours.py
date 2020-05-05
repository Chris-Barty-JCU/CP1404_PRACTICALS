
STATE_NAMES = {"NSW": "New South Wales", "QLD": "Queensland", "NT": "Northern Territory"}

for key, value in STATE_NAMES.items():
    print("{:3} is {}".format(key, value))


HEX_COLOURS = {"CornflowerBlue": "#6495ed", "DarkKhaki": "#bdb76b", "DarkOrchid": "#9932cc", "DimGray": "#696969",
               "ForestGreen": "#228b22", "Goldenrod": "#daa520", "LawnGreen": "#7cfc00", "Moccasin": "#ffe4b5"}

colour_name = input("Enter a colour name to see the hexadecimal value: ")
while colour_name != "":
    if colour_name not in HEX_COLOURS.keys():
        colour_name = input("Invalid colour - Enter a colour name to see the hexadecimal value: ")
    else:
        hex_code = HEX_COLOURS.get(colour_name)
        print("{} = {}".format(colour_name, hex_code))
        colour_name = input("Enter a colour name to see the hexadecimal value: ")
print("Blank Entered - Program Exited")

