"""CP1404/CP5632 Practical - Guitar class example.
Record start doing time: 9:00 a.m.
Completed time: 11:00 a.m.
Estimate using time: 1h 30m
Real using time: 2h
"""
SPECIFIC_YEAR = 2024
SPECIFIC_RANGE = 50


class Guitar:
    """This is a class for storing the guitar naming attributes and methods."""

    def __init__(self, name="", year=0, cost=0.00):
        """Initialize the attribute."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}({self.year}): {self.cost: .2f}"

    def get_age(self):
        """The method that determine the guitar age."""
        return SPECIFIC_YEAR - self.year

    def is_vintage(self):
        """The method that determine the guitar is vintage or not."""
        return self.get_age() >= SPECIFIC_RANGE

    def __lt__(self, other):
        """The method that start the guitar comparison and re-organize."""
        return self.year < other.year
