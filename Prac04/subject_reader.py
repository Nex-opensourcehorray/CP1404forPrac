"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """The main function that running two functions."""
    load_data()
    get_lecture_detailed()


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    Celebrity = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        Celebrity.append(parts)
        print(Celebrity)
    input_file.close()


def get_lecture_detailed():
    """Read data from file formatted and print the subject,lecturer,number of students in detailed."""
    input_file = open(FILENAME)
    for line in input_file:
        # To change every line with strip and split.
        line = line.strip()
        Parts = line.split(',')
        print(f"{Parts[0]} is taught by {Parts[1]} and has {Parts[2]} students.")
    print("----------")
    input_file.close()


main()
