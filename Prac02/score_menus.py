"""
CP1404/CP5632 - Practical
A menu to choose the option with error detection in function.
"""

"""import random"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n>>>"


def main():
    """ The main function that holding the score menu."""
    get_scores = get_valid_score()
    choice = input(MENU).upper()

    while choice != 'Q':
        if choice == 'G':
            print(f"Your score is: {get_scores}")
        elif choice == 'P':
            get_evaluate = determine_score(get_scores)
            print(f"Your result is: {get_evaluate}")
        elif choice == 'S':
            print_stars(get_scores)
            print('\n')
        else:
            print("Invalid input!")

        choice = input(MENU).upper()
    print("Farewell.")


def get_valid_score():
    """The function can ensure the score will be range between 0 & 100."""
    scores = int(input("Please input the scores:"))
    if scores < 0 or scores > 100:
        print("Invalid input! do it again!")
        scores = int(input("Please input the scores:"))
    return scores


def determine_score(get_scores):
    """The function can determine you grade."""
    if get_scores >= 90:
        message = "Excellent"
    elif get_scores >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


"""def determine_random_score():
    scores = random.randint(0, 100)
    return scores
"""


def print_stars(get_scores):
    """The function that helping you to print the asterisk."""
    for i in range(0, get_scores):
        print("*" * i, end='')


main()
