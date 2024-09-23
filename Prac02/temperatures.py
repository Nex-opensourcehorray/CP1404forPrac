"""
CP1404/CP5632 - Practical 02
Temperature conversion with two functions.
"""
MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit\n>>> """


def main():
    """The main menu function with the temperature conversion."""
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        choice = input(MENU).upper()
    print("Thank you.")


def convert_celsius(celsius):
    """convert the temperature from celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit(fahrenheit):
    """convert the temperature from fahrenheit to celsius."""
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius


main()
