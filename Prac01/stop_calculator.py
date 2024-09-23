"""
CP1404/CP5632 - Practical
A program to calculate the Total value for items with error checking.
"""

item_number = int(input("Number of items: "))
total_value = 0
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items: "))

for i in range(0, item_number):
    value = float(input("Price of item: "))
    total_value += value
    if total_value > 100:
        total_value *= 0.9
print(f"Total Price for {item_number} items is ${total_value: .2f}")
