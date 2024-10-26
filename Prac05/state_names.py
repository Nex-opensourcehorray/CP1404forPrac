"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    """This function is to execute the matching."""
    print(CODE_TO_NAME)
    for code, name in CODE_TO_NAME.items():
        print(f"{code: <4} is {name}")

    state_abbreviation = get_valid_input()
    while state_abbreviation != "":
        print(f"{state_abbreviation} is {CODE_TO_NAME[state_abbreviation]}")
        state_abbreviation = get_valid_input()
    print("This is the end of the comparison.")


def get_valid_input():
    """Deliver the error checking for input."""
    state_abbreviation = ''
    valid_input = True
    while valid_input:
        try:

            state_abbreviation = input("Enter short state: ").upper()
            if state_abbreviation == "":
                break
            elif state_abbreviation not in CODE_TO_NAME:
                print("Invalid short state")
            else:
                valid_input = False
        except ValueError:
            print("Invalid short state")
    return state_abbreviation


if __name__ == '__main__':
    main()
