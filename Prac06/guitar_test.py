"""CP1404/CP5632 Practical - Guitar class for testing example.
Record start doing time: 9:00 a.m.
Completed time: 11:00 a.m.
Estimate using time: 1h 30m
Real using time: 2h
"""
from Prac06.guitar import Guitar


def launch_test():
    """A random test about the guitar class."""
    gibson_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 12345.50)
    print(f"{gibson_ces.name} get age() - Expected {102}. Got {gibson_ces.get_age()}")
    print(f"{another_guitar.name} get age() - Expected {11}. Got {another_guitar.get_age()}")
    print()
    print(f"{gibson_ces.name} is_vintage() - Expected {True}. Got {gibson_ces.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    launch_test()
