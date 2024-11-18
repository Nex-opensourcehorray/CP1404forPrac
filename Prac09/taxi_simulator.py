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
    total_spend = 0.0
    your_taxi_list = None
    print("Let's drive!")
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            print("choose the taxi!")
        elif choice == "d":
            if your_taxi_list is None:
                print("You need to choose a taxi before you can drive!")
            else:
                print("drive the Taxi!")
        else:
            print("Invalid choice!")
        print(f"Bill to date:{total_spend:.2f}")
        choice = input(MENU).lower()

    print(f"Total trip cost: ${total_spend:.2f}")
    print("Taxis are now:")


if __name__ == '__main__':
    main()
