"""
CP1404/CP5632 Practical
Sliver Service Taxi class with running test.
"""
from Prac09.silver_service_taxi import SliverServiceTaxi


def run_test():
    silver_service_taxi = SliverServiceTaxi("Tesla Sport 3", 100, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())


if __name__ == '__main__':
    run_test()
