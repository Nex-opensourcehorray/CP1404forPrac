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
    place_infos = read_csv_info()
    print(WELCOME)
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'D':
            """This statement will turn to display all the information from places.csv."""
            print_information(place_infos)
        elif choice == 'R':
            """This statement will random pick a place for recommend."""
            random_place(place_infos)
        elif choice == 'A':
            """This statement will add a place with specific detail for the List."""
            add_information(place_infos)
        elif choice == 'M':
            """This statement will change a place visited/unvisited label."""
            print_information(place_infos)
            print("marked.")
        else:
            print(INVALID_CHOICE)

        choice = input(MENU).upper()

    save_travel_information_into_file(place_infos)
    print(f"places saved to {FILENAME}\n{FAREWELL}")
    """This statement will overwrite place.csv from the refresh List."""


def read_csv_info():
    """This function is use to get in the csv dataset."""
    with open(FILENAME, 'r', encoding='utf-8') as place_infos_file:
        reader = csv.reader(place_infos_file)
        place_infos = [[text[0], text[1], text[2], text[3]] for text in reader]
    return place_infos


def print_information(place_infos):
    """This function is to print the blank for modification."""
    index = 1
    asterisk_count = 0
    city_length = max(len(place_info[0]) for place_info in place_infos)
    country_length = max(len(place_info[1]) for place_info in place_infos)
    visit_length = max(len(str(place_info[2])) for place_info in place_infos)

    for place_info in place_infos:
        if place_info[3] == 'n':
            print(f"{ASTERISK_LABEL}{index}. {place_info[0]: <{city_length}} in "
                  f"{place_info[1]: <{country_length}} {place_info[2]: >{visit_length}}")
            asterisk_count += 1
        else:
            print(f" {index}. {place_info[0]: <{city_length}} in "
                  f"{place_info[1]: <{country_length}} {place_info[2]: >{visit_length}}")

        index += 1
    print(f"{len(place_infos)} places tracked. You still want to visit {asterisk_count} places.")


def random_place(places_infos):
    """This function is to generate random number and print it."""
    random_number = random.randint(0, len(places_infos) - 1)
    random_city = places_infos[random_number][0]
    random_country = places_infos[random_number][1]
    print(f"Not sure where to visit next?\nHow about... {random_city} in {random_country}?")


def get_valid_word(prompt):
    """Ensure your input is not blank."""
    value = input(prompt).title()
    while value == "":
        print("Input can not be blank")
        value = input(prompt).title()
    return value


def get_valid_number(prompt):
    """Confirm your input number is not negative or equal than 0"""
    value_verify = False
    while not value_verify:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")


def add_information(place_infos):
    """Add the information into the List."""
    city_name = get_valid_word("Name: ")
    country_name = get_valid_word("Country: ")
    priority_number = get_valid_number("Priority: ")
    print(f"{city_name} in {country_name} (Priority {priority_number}) added to Travel Tracker.")
    place_infos.append([city_name, country_name, priority_number, 'n'])


def save_travel_information_into_file(place_infos):
    """This function is use to save the modified information to the csv dataset."""
    with open(FILENAME, 'w', encoding='utf-8') as save_information_file:
        for place_info in place_infos:
            print(f"{place_info[0]},{place_info[1]},{place_info[2]},{place_info[3]}", file=save_information_file)


if __name__ == '__main__':
    main()
