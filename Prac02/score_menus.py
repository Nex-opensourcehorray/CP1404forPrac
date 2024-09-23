"""
CP1404/CP5632 - Practical
A menu to choose the option with error detection in function.
"""

import random

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n>>>"


def main():
    choice = input(MENU).upper()

    while choice != 'Q':
        if choice == 'G':
            get_score = determine_random_score()
            print(f"Your score is: {get_score}")
        elif choice == 'P':
            scores = determine_random_score()
            get_evaluate = determine_score(scores)
            print(f"Your result is: {get_evaluate}")
        elif choice == 'S':
            star_scores = determine_random_score()
            print_stars(star_scores)
            print('\n')
        else:
            print("Invalid input!")

        choice = input(MENU).upper()
    print("Farewell.")


def determine_score(scores):
    if scores < 0 or scores > 100:
        return "Invalid scores"
    elif 50 <= scores < 90:
        return "Passable"
    elif 90 <= scores <= 100:
        return "Excellent"
    else:
        return "Bad"


def determine_random_score():
    scores = random.randint(0, 100)
    return scores


def print_stars(star_scores):
    for i in range(0, star_scores):
        print("*" * i, end='')


main()
