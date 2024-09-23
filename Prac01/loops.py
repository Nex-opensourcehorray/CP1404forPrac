"""
CP1404/CP5632 - Practical
The Revision about the for loop
"""

# example for loop:
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100:
for a in range(0, 110, 10):
    print(a, end=' ')
print()

# b. count down from 20 to 1:
for b in range(20, 0, -1):
    print(b, end=' ')
print()

# c. print n stars:
star_number = int(input("Number of Stars: "))
for o in range(1, star_number+1):
    print("*", end='')
print(end='\n')

# d. print n lines of increasing stars:
number_star = int(input("Number of Stars: "))
for o in range(1, number_star+1):
    for p in range(o):
        print("*", end='')
    print()
