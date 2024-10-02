"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    """The function that helping with avoiding zero division error."""
    if denominator == 0:
        print("We can't do divide when denominator is zero!")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. when numerator or denominator is not a number, it will jump to the ValueError.
# 2. when denominator is a zero, it will jump to the ZeroDivisionError.