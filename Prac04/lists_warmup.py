"""
CP1404/CP5632 - Practical
The List review with question answering and List coding.
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
"""We could except the underline will print 3."""
print(numbers[0])
"""We could except the underline will print 2."""
print(numbers[-1])
"""We could except the underline will print 1."""
print(numbers[3])
"""We could except the underline will print all the number exclude 2."""
print(numbers[:-1])
"""We could except the underline will print 1."""
print(numbers[3:4])
"""We could except the underline will print True."""
print(5 in numbers)
"""We could except the underline will print False."""
print(7 in numbers)
"""We could except the underline will print False."""
print("3" in numbers)
"""We could except the underline will add the 6,5,3 into the numbers List."""
print(numbers + [6, 5, 3])

# Extra Requirements:
"""1. Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = 'ten'
print(numbers)
"""2. Change the last element of numbers to 1"""
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(numbers)
"""3. Print all the elements from numbers except the first two (slice)"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[2:])
"""4. Print whether 9 is an element of number"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(9 in numbers)