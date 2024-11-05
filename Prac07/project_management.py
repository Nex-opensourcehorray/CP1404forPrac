"""CP1404/CP5632 Practical - Project management example.
Record start doing time: 9:00 a.m.
Completed time: 3:00 p.m.
Estimate using time: 3h 30m
Real using time: 5h
"""
from Prac07.project import Project

FILENAME = 'projects.txt'
WELCOME = 'Welcome to Pythonic Project Management'
MENU = ('- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n'
        '- (A)dd new project\n- (U)pdate project\n- (Q)uit>>>')
INVALID_CHOICE = 'Invalid menu choice'
QUIT = 'Q'
LOAD = 'L'
SAVE = 'S'
DISPLAY = 'D'
FILTER = 'F'
ADD = 'A'
UPDATE = 'U'


def main():
    """This function is to hold the menu option & your selection."""
    """Before get into the menu option, you should read in the document to the memory for first."""
    print(WELCOME)
    public_projects = read_file(FILENAME)
    choice = input(MENU).upper()
    while choice != QUIT:
        if choice == LOAD:
            """This statement will load all the information from .txt."""
            load_public_project()
        elif choice == SAVE:
            """This statement will save the modification to .txt."""
            save_file(public_projects)
        elif choice == DISPLAY:
            """This statement will show the important and unimportant project."""
        elif choice == FILTER:
            """This statement will search the project."""
        elif choice == ADD:
            """This statement will add another project."""
        elif choice == UPDATE:
            """This statement will update some information in a specific project."""
        else:
            print(INVALID_CHOICE)

        choice = input(MENU).upper()

    print(f"Would you like to save to {FILENAME}?")
    print("Thank you for using custom-built project management software.")
    """This statement give an option whether you will overwrite .csv from the refresh List."""


def read_file(FILENAME):
    public_projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readlines()
        for line in in_file:
            projects = line.strip().split('\t')
            public_projects.append(Project(projects[0], projects[1], int(projects[2]), float(projects[3]),
                                           int(projects[4])))
    print(f"Loaded {len(public_projects)} projects from {FILENAME}")
    return public_projects


def load_public_project():
    file_name = input("Please input your filename:")
    try:
        read_file(file_name)
    except FileNotFoundError:
        print(f"{file_name} is not existed! System will use the default file {FILENAME}")
        read_file(FILENAME)


def save_file(public_projects):
    file_name = input("Please select your filename to save:")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    print(f"Save to {file_name} success!")
    save_to_file(public_projects, file_name)


def save_to_file(public_projects, file_name):
    with open(file_name, "w") as on_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=on_file)
        for line in public_projects:
            print(f"{line.name}\t{line.start_date}\t{line.priority}\t{line.cost_estimate}\t"
                  f"{line.completion_percentage}", file=on_file)
