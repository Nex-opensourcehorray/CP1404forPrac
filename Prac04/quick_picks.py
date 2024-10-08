"""
CP1404/CP5632 - Practical
"Quick Pick" Lottery Ticket Generator
"""
import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
LINE_OF_NUMBER = 6
quick_pick_number = int(input("How Many Quick Picks You Want? >"))
"""This function is to generate and fetch quick pick number."""
for i in range(quick_pick_number):
    generate_numbers = []
    for j in range(0, 6):
        generate_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while generate_number in generate_numbers:
            generate_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        generate_numbers.append(generate_number)
    generate_numbers.sort()

    for k in generate_numbers:
        """This function is to print generate number."""
        print(f"{k:>2}", end=" ")
    print()