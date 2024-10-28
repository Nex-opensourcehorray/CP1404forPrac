"""CP1404/CP5632 Practical - Programming language class example.
Record start doing time: 10:45 p.m.
Completed time: 11:45 p.m.
Estimate using time: 45 minutes
Real using time: 1 hours
"""


class ProgrammingLanguage:
    """This is a class for storing the programming language attributes and methods."""
    def __init__(self, name, typing, reflection, year):
        """Initialize the attribute."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First Appeared in {self.year}"

    def is_dynamic_language(self):
        """Confirm the programming language is dynamic or not."""
        return self.typing == "Dynamic"
