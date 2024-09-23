"""
CP1404/CP5632 - Practical
A menu to choose the option with error detection.
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit\n>>>"

name = input("Your name: ")
choice = input(MENU).upper()

while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid input!")

    choice = input(MENU).upper()

print("Finished.")