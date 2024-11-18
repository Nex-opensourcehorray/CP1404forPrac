"""
CP1404/CP5632 Practical
Sliver Service Taxi class
"""
from Prac09.taxi import Taxi


class SliverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return f"${super().get_fare() + self.flagfall:.2f}"
