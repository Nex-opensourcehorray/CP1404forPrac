"""CP1404/CP5632 Practical - Guitar class for real example.
Record start doing time: 9:00 a.m.
Completed time: 11:00 a.m.
Estimate using time: 1h 30m
Real using time: 2h
"""
from Prac06.guitar import Guitar


def main():
    """The actual real test about the guitar input."""
    guitars = []
    print("My guitars!")
    name = input("Name:")
    while name != "":
        """while name is not blank, if will continue grab the information from user."""
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "Added to the file")
        name = input("Name:")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# The printing part of the guitars List and vintage confirmation:
    if guitars:
        guitars.sort()
        print("My guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage_string = " (vintage)"
                print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}"
                      .format(i, guitar, vintage_string))
    else:
        print("Can you please go and get one, very cool!")


if __name__ == '__main__':
    main()
