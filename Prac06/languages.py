"""CP1404/CP5632 Practical - Programming language importing example.
Record start doing time: 10:45 p.m.
Estimate using time: 45 minutes
Completed time: 11:45 p.m.
Real using time: 1 hours
"""
from Prac06.programming_language import ProgrammingLanguage


def main():
    """The actual printing that import from class and printing."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(f"{python}\n")

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic_language():
            print(programming_language.name)


if __name__ == '__main__':
    main()
