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

ASTERISK_LABEL = '*'


def main():
    """This function is to hold the menu option & your selection."""
    """Before get into the menu option, you should read in the document to the memory for first."""
    travel_places = []
    place_infos = []
    asterisk_count = 0
    text_number = 1
    print(WELCOME)
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'D':
            """This statement will turn to display all the information from places.csv."""
            read_csv_info(place_infos)
            city_length = max(len(place_info[0]) for place_info in place_infos)
            country_length = max(len(place_info[1]) for place_info in place_infos)
            visit_length = max(len(place_info[2]) for place_info in place_infos)

            for place_info in place_infos:
                if place_info[3] == 'n':
                    value = (f"{ASTERISK_LABEL}{text_number}. {place_info[0]: <{city_length}} in "
                             f"{place_info[1]: <{country_length}} {place_info[2]: >{visit_length}}")
                    asterisk_count += 1
                    travel_places.append(value)
                else:
                    value = (f" {text_number}. {place_info[0]: <{city_length}} in "
                             f"{place_info[1]: <{country_length}} {place_info[2]: >{visit_length}}")
                    travel_places.append(value)
                text_number += 1
            for travel_place in travel_places:
                print(travel_place)
            print(f"{len(place_infos)} places tracked. You still want to visit {asterisk_count} places.")
        elif choice == 'R':
            """This statement will random pick a place for recommend."""
            random_place(place_infos)
        elif choice == 'A':
            """This statement will add a place with specific detail for the List."""
            print("add.")
        elif choice == 'M':
            """This statement will change a place visited/unvisited label."""
            for travel_place in travel_places:
                print(travel_place)
            print(f"{len(place_infos)} places tracked. You still want to visit {asterisk_count} places.")
        else:
            print(INVALID_CHOICE)

        choice = input(MENU).upper()

    print(f"places saved to {FILENAME}\n{FAREWELL}")
    """This statement will overwrite place.csv from the refresh List."""


def read_csv_info(place_infos):
    """This function is use to get in the csv dataset."""
    with open(FILENAME, newline='') as in_file:
        reader = csv.reader(in_file)
        for text in reader:
            place_infos.append(text)

    return place_infos


def random_place(places_infos):
    """This function is to generate random number and print it."""
    random_number = random.randint(0, len(places_infos) - 1)
    random_city = places_infos[random_number][0]
    random_country = places_infos[random_number][1]
    print(f"Not sure where to visit next?\nHow about... {random_city} in {random_country}?")


"""def add_information():"""

if __name__ == '__main__':
    main()
