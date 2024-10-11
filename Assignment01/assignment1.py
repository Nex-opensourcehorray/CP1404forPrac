"""
CP1404 Assignment 1 - Travel Tracker
Name: mingsen hua
Date started: 12/10/2024
GitHub URL:
"""
WELCOME = 'Travel Tracker 1.0 - by Nex'
FILENAME = 'places.csv'
MENU = ('MENU:\nD - Display all places\nR - Recommend a random place\nA - Add a new place\nM - Mark a place as '
        'visited\nQ - Quit\n>>>')
FAREWELL = 'Have a nice day! :)'


def main():
    """This function is to hold the menu option & your selection."""
    """Before get into the menu option, you should read in the document to the memory for first."""
    print(WELCOME)
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'D':
            """This statement will turn to display all the information from places.csv."""
            print("display.")
        elif choice == 'R':
            """This statement will random pick a place for recommend."""
            print("random.")
        elif choice == 'A':
            """This statement will add a place with specific detail for the List."""
            print("add.")
        elif choice == 'M':
            """This statement will change a place visited/unvisited label."""
            print("remark.")
        else:
            print("Invalid menu choice")

        choice = input(MENU).upper()
    print(f"places saved to {FILENAME}\n{FAREWELL}")
    """This statement will overwrite place.csv from the refresh List."""


if __name__ == '__main__':
    main()
