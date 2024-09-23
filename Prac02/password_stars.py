"""
CP1404/CP5632 - Practical 02
password asterisk printing with functions.
"""


def main():
    """The main function about how you get your password & printing."""
    require_pw_count = 8
    password = get_password(require_pw_count)
    print_asterisk(password)


def get_password(require_pw_count):
    """Ensure your password length is larger than requirement."""
    password = input("Please input your password: ")
    while len(password) < require_pw_count:
        print("This is invalid! please do it again!")
        password = input("Please input your password: ")
    return password


def print_asterisk(password):
    """Get password and print the asterisk with password length."""
    print("Your Password is: ")
    for i in range(len(password)):
        print("*", end='')


main()
