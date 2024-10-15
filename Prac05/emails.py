"""
CP1404/CP5632 Practical
receive consumers name and email.
"""


def main():
    """This function helps you grab and print your dictionary."""
    name_and_email = {}
    email_address = input("Email:")
    while email_address != "":
        capital_name = gather_name(email_address)
        choice = input(f"Is your name {capital_name}? (Y / n)")
        if choice.upper() == 'Y':
            name = capital_name
        else:
            input_name = input("Your name:")
            name = fetch_name(input_name)

        name_and_email[email_address] = name
        email_address = input("Email:")

    for email_address in name_and_email:
        print(f"{name_and_email[email_address]} ({email_address})")


def gather_name(email_address):
    """This function is to fetch and split your name at the front of your email."""
    """Suggestion: when your email input with your real name, please add a period in between."""
    mail_name = email_address.split('@')[0]
    mail_names = mail_name.split('.')
    capital_name = ' '.join(mail_names).title()
    return capital_name


def fetch_name(input_name):
    """This function is attempting to capitalize user input."""
    names = input_name.split(' ')
    name = ' '.join(names).title()
    return name


if __name__ == '__main__':
    main()
