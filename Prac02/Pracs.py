import random

low = int(input("Please input your downside number: "))
high = int(input("Please input your upside number: "))

while low >= high:
    print("Invalid input!")
    low = int(input("Please input your downside number: "))
    high = int(input("Please input your upside number: "))

generate_number = random.randint(low, high)
print(":)" * generate_number, end=' ')


"""
import random
def main():
    choice = input("get your choice: ")
    while choice != 'Q':
        if choice == 'P':
            print_line()
        elif choice == 'R':
            random_number()
        else:
            get_valid_name()
def get_valid_name():
    name = input("Please input your name: ")
    while name == '':
        print("Invalid input!")
        name = input("Please input your name: ")
def print_line():


def random_number():
    number = random.randint(0,100)
    return number


main()
"""

"""
1, determine_grade()
2, convert_USD_to_AUD()
3, print_report()
4, calculate_average()
5, is_even()
6, get_valid_age()
"""