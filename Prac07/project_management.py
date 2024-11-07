"""CP1404/CP5632 Practical - Project management example.
Record start doing time: 9:00 a.m.
Completed time: 3:00 p.m.
Estimate using time: 3h 30m
Real using time: 5h
"""
from Prac07.project import Project
import datetime

INNER_FILE = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>> ")
INVALID_CHOICE = 'Invalid menu choice'
QUIT = 'Q'
LOAD = 'L'
SAVE = 'S'
DISPLAY = 'D'
FILTER = 'F'
ADD = 'A'
UPDATE = 'U'
MINIMUM_NUMBER = 0
MAXIMUM_PERCENTAGE = 100


def main():
    """This function is to hold the menu option & your selection."""
    """Before get into the menu option, you should read in the document to the memory for first."""
    print("Welcome to Pythonic Project Management")
    projects_detail = read_file_information(INNER_FILE)
    choice = input(MENU).upper()
    while choice != QUIT:
        if choice == LOAD:
            """This statement will load all the information from .txt."""
            load_projects()
        elif choice == SAVE:
            """This statement will save the modification to a new.txt."""
            save_data_to_another_file(projects_detail)
        elif choice == DISPLAY:
            """This statement will show the important and unimportant project."""
            show_projects(projects_detail)
        elif choice == FILTER:
            """This statement will search the project."""
            filter_projects(projects_detail)
        elif choice == ADD:
            """This statement will add another project."""
            add_project(projects_detail)
        elif choice == UPDATE:
            """This statement will update some information in a specific project."""
        else:
            print(INVALID_CHOICE)

        choice = input(MENU).upper()

    print(f"Would you like to save to {INNER_FILE}?")
    print("Thank you for using custom-built project management software.")
    """This statement give an option whether you will overwrite .txt from the refresh List."""


def read_file_information(file_name):
    """Read line and append to List from the selected or default file."""
    projects_detail = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            projects_detail.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects_detail)} projects from {file_name}")
    return projects_detail


def load_projects():
    """User input the file to determine which file to read."""
    file_name = input("Please enter the file name: ")
    try:
        read_file_information(file_name)
    except FileNotFoundError:
        print(f"System will using the default file: {INNER_FILE}")
        read_file_information(INNER_FILE)


def save_data_to_another_file(projects_detail):
    """Find selected file that will save the information from List."""
    file_name = input("Enter which document you want save:")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    print(f"Save into {file_name} success")
    save_data_to_file(projects_detail, file_name)


def save_data_to_file(projects_detail, file_name):
    """Save data from the selected file."""
    with open(file_name, "w") as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for line in projects_detail:
            print(f"{line.name}\t"
                  f"{line.start_date}\t"
                  f"{line.priority}\t"
                  f"{line.cost_estimate}\t"
                  f"{line.completion_percentage}", file=out_file)


def show_projects(projects_detail):
    """Display completed and uncompleted projects based on progress."""
    show_information = sorted(projects_detail)
    print("Incomplete projects:")
    incomplete_projects = [line for line in show_information if not line.is_completed()]
    for line in incomplete_projects:
        print(f"\t{line}")
    print("Completed projects:")
    completed_projects = [line for line in show_information if line.is_completed()]
    for line in completed_projects:
        print(f"\t{line}")


def filter_projects(projects_detail):
    """Output the project after the valid selected date."""
    show_information = sorted(projects_detail)
    date = 0
    valid_date = False
    while not valid_date:
        try:
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            valid_date = True
        except ValueError:
            print("Please enter a valid date!")

    for line in show_information:
        project_start_date = datetime.datetime.strptime(line.start_date, "%d/%m/%Y").date()
        if project_start_date >= date:
            print(line)


def add_project(projects_detail):
    """Add an extra new project."""
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    day = 0
    valid_daytime = False
    while not valid_daytime:
        try:
            day = input("Start date (dd/mm/yy): ")
            datetime.datetime.strptime(day, "%d/%m/%Y").date()
            valid_daytime = True
        except ValueError:
            print("please enter a  valid day")
    priority = int(get_valid_number("Priority: "))
    cost = get_valid_number("Cost estimate: ")
    percent_complete = int(get_valid_percentage("Percent complete: "))
    projects_detail.append(Project(name, day, priority, cost, percent_complete))
    show_projects(projects_detail)


def get_valid_string(prompt):
    value = input(prompt)
    while value == "":
        print(f"{prompt} can not be blank")
        value = input(prompt)
    return value


def get_valid_number(prompt):
    effect_number = False
    while not effect_number:
        try:
            value = float(input(prompt))
            if value < MINIMUM_NUMBER:
                print("number should > 0")
            else:
                return value
        except ValueError:
            print("Please enter a valid number")


def get_valid_percentage(prompt):
    value = get_valid_number(prompt)
    while value > MAXIMUM_PERCENTAGE:
        print("Percentage can not > 100")
        value = get_valid_number(prompt)
    return value


if __name__ == '__main__':
    main()
