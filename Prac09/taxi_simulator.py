"""
CP1404/CP5632 Practical
Taxi Simulator main function.
"""
from Prac09.silver_service_taxi import SliverServiceTaxi
from Prac09.taxi import Taxi

TAXIS = [Taxi("Prius", 100), SliverServiceTaxi("Limo", 100, 2),
         SliverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive\n>>>"


def main():
    """The main part of program to control."""
    total_spend = 0.0
    your_taxi = None
    print("Let's drive!")
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            your_taxi = choose_your_taxi()
        elif choice == "d":
            if your_taxi is None:
                print("You need to choose a taxi before you can drive!")
            else:
                current_spend = drive_taxi(your_taxi)
                total_spend += current_spend
                print(f"Your {your_taxi.name} cost you ${current_spend:.2f}")
        else:
            print("Invalid choice!")
        print(f"Bill to date:{total_spend:.2f}")
        choice = input(MENU).lower()

    print(f"Total trip cost: ${total_spend:.2f}")
    print("Taxis are now:")
    display_all_taxi()


def choose_your_taxi():
    """Choose a taxi to service you."""
    print("Taxis available:")
    display_all_taxi()
    choose = int(input("Choose taxi:"))
    if 0 <= choose < len(TAXIS):
        return TAXIS[choose]
    else:
        print("Invalid Taxi Choose!")
        return None


def display_all_taxi():
    """Print all the taxi from the list."""
    for index_number, taxi in enumerate(TAXIS):
        print(f"{index_number} - {taxi}")


def drive_taxi(your_taxi):
    """Control your Taxi with your requirement distance."""
    distance = int(input("Drive how far?"))
    your_taxi.drive(distance)
    your_taxi.get_fare()
    return your_taxi.get_fare()


if __name__ == '__main__':
    main()
