"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year},"
                f" Pointer arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer_arithmetic(self):
        return self.pointer_arithmetic == "Pointer_Arithmetic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, "Pointer_Arithmetic")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, "Pointer_Arithmetic")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, "Pointer_Arithmetic")

    languages = [ruby, python, visual_basic]
    print(python)

    print("The pointer arithmetic typed languages are:")
    for language in languages:
        if language.is_pointer_arithmetic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
