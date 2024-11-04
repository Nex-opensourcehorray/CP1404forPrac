"""CP1404/CP5632 Practical - Guitar class for real example.
"""
from Prac07.guitar import Guitar


def main():
    """The actual real test about the guitar input."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        names = line.strip().split(',')
        name = names[0]
        year = names[1]
        cost = names[2]
        guitar_name = Guitar(name, int(year), float(cost))
        guitars.append(guitar_name)
    in_file.close()
    display_my_guitar(guitars)


def display_my_guitar(guitars):
    # The printing part of the guitars List and vintage confirmation:
    guitar_length = max(len(guitar.name) for guitar in guitars)
    cost_length = max(len(str(guitar.cost)) for guitar in guitars)
    if guitars:
        guitars.sort()
        print("My guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            else:
                vintage_string = ""
            print(f"Guitar {i}: {guitar.name:{guitar_length}} ({guitar.year}), worth $ {guitar.cost:{cost_length}.2f}"
                  f"{vintage_string}")

    else:
        print("Can you please go and get one, very cool!")


if __name__ == '__main__':
    main()
