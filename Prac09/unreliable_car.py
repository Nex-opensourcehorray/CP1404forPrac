"""
CP1404/CP5632 Practical
Unreliable Car class
"""
import random
from Prac09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """The Initial of the Parent value and child self value."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def drive(self, distance):
        """Inherit from Parent class to use drive method."""
        distance = super().drive(distance)
        number = random.randint(0, 100)
        if number < self.reliability:
            distance_driven = distance
        else:
            distance_driven = 0

        return distance_driven
