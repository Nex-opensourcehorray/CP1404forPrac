"""
CP1404 Assignment 1 - Travel Tracker
Name: mingsen hua
Date started: 12/10/2024
GitHub URL:
"""
import csv
import random

WELCOME = 'Travel Tracker 1.0 - by Nex'
FILENAME = 'places.csv'
MENU = ('MENU:\nD - Display all places\nR - Recommend a random place\nA - Add a new place\nM - Mark a place as '
        'visited\nQ - Quit\n>>>')
FAREWELL = 'Have a nice day! :)'
INVALID_CHOICE = 'Invalid menu choice'
place_infos = []
ASTERISK_LABEL = '*'


def main():
    """This function is to hold the menu option & your selection."""
    """Before get into the menu option, you should read in the document to the memory for first."""
    print(WELCOME)
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'D':
            """This statement will turn to display all the information from places.csv."""
            text_number = read_csv_info(place_infos)
            print(f"{text_number} places tracked. You still want to visit {text_number} places.")
        elif choice == 'R':
            """This statement will random pick a place for recommend."""
            random_place(place_infos)
        elif choice == 'A':
            """This statement will add a place with specific detail for the List."""
            print("add.")
        elif choice == 'M':
            """This statement will change a place visited/unvisited label."""
            print("remark.")
        else:
            print(INVALID_CHOICE)

        choice = input(MENU).upper()

    print(f"places saved to {FILENAME}\n{FAREWELL}")
    """This statement will overwrite place.csv from the refresh List."""


def read_csv_info(place_infos):
    """This function is use to get in the csv dataset."""
    text_number = 0
    with open(FILENAME, newline='') as in_file:
        reader = csv.reader(in_file)
        for text in reader:
            text_number += 1
            place_infos.append(text)
            print(f"{ASTERISK_LABEL}{text_number}. {text[0]: <8} in {text[1]: <12} {text[2]: >2}")

    return text_number


def random_place(places_infos):
    random_number = random.randint(0, len(places_infos)-1)
    random_city = places_infos[random_number][0]
    random_country = places_infos[random_number][1]
    print(f"Not sure where to visit next?\nHow about... {random_city} in {random_country}?")


if __name__ == '__main__':
    main()
