"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!

scores = int(input("Enter scores: "))

if scores < 0 or scores > 100:
    message = "Invalid scores"
elif 50 <= scores < 90:
    message = "Passable"
elif 90 <= scores <= 100:
    message = "Excellent"
else:
    message = "Bad"

print(message)

# Comment: I don't confirm that whether 50 <= score < 90 is readable or not,
# so, I offer another solution as well.

scores = int(input("Enter scores: "))

if scores < 0 or scores > 100:
    print("Invalid score")
elif scores >= 50 and scores < 90:
    print("Passable")
elif scores >= 90 and scores <= 100:
    print("Excellent")
else:
    print("Bad")