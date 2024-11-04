"""CP1404/CP5632 Practical - Guitar class for real example.
"""
from Prac07.guitar import Guitar


def main():
    """The actual real test about the guitar input."""
    guitars = []
    get_user_guitar(guitars)
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        names = line.strip().split(',')
        name = names[0]
        year = names[1]
        cost = names[2]
        guitar_name = Guitar(name, int(year), float(cost))
        guitars.append(guitar_name)
    in_file.close()
    display_my_guitar(guitars)
    write_back_csv(guitars)


def get_user_guitar(guitars):
    name = input("Name:")
    while name != "":
        """while name is not blank, if will continue grab the information from user."""
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "Added to the file")
        name = input("Name:")


def display_my_guitar(guitars):
    # The printing part of the guitars List and vintage confirmation:
    guitar_length = max(len(guitar.name) for guitar in guitars)
    cost_length = max(len(str(guitar.cost)) for guitar in guitars)
    if guitars:
        guitars.sort()
        print("My guitars:")
        for i, guitar in enumerate(guitars, 0):
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            else:
                vintage_string = ""
            print(
                f"Guitar {i + 1}: {guitar.name:{guitar_length}} ({guitar.year}), worth $ {guitar.cost:{cost_length}.2f}"
                f"{vintage_string}")

    else:
        print("Can you please go and get one, very cool!")


def write_back_csv(guitars):
    with open('guitars.csv', 'w', encoding='utf-8') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == '__main__':
    main()
