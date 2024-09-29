import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# TODO: Answer all the following questions and reach to the requirement.
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
"""It will generate a integer between 5 and 20."""
"""Since it is being narrowed into the range from 5 to 20, after running thousands of time, 
the minimum that I had seen is 5, and the largest number I had seen is 20."""

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
"""It will generate a integer between 3 and 10."""
"""Since it is being narrowed into the range from 3 to 10, after running thousands of time, 
the minimum that I had seen is 3, and the largest number I had seen is 9."""
"""No, it can't, because the stepping limit the data fetching."""


# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
"""It will generate a float16 number between 2.5 and 5.5."""
"""Since it is being narrowed into the range from 2.5 to 5.5, after running thousands of time, 
the minimum that I had seen is 2.5100849599555755, and 
the largest number I had seen is 5.400429463723878."""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randrange(1, 100))