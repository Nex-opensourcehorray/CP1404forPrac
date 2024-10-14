color_to_hex = {'Aqua': '#00ffff', 'Boysenberry': '#873260', 'Cambridge Blue': '#a3c1ad',
                'Carnation Pink': '#ffa6c9', 'Chocolate': '#d2691e', 'Crystal': '#a7d8de',
                'Dark Pastel Green': '#03c03c', 'Deep Space Sparkle': '#4a646c', 'Dogwood Rose': '#d71868',
                'French Lilac': '#86608e'}


def main():
    """This function is to get valid colour name and get actual hex code from dictionary."""
    colour_name = input("Please choose a color:").title()
    while colour_name != "":
        if colour_name in color_to_hex:
            print(f"{colour_name} is {color_to_hex[colour_name]}")
        else:
            print("Your input is invalid!")
        colour_name = input("Please choose a color:").title()


main()
