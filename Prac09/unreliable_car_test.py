"""
CP1404/CP5632 Practical
Unreliable Car class running test.
"""
from Prac09.unreliable_car import UnreliableCar


def run_test():
    My_unreliable_car = UnreliableCar("BMW M5", 125, 75)
    print(My_unreliable_car.drive(65))


if __name__ == '__main__':
    run_test()
