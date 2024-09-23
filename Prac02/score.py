"""
CP1404/CP5632 - Practical 02
Determine score status with functions
"""
import random


def main():

    scores = determine_random_score()
    generate_evaluate = determine_score(scores)
    print(f"Your score is: {scores}")
    print(f"Your generate evaluate is: {generate_evaluate}")
def get_valid_score(scores):

def determine_score(scores):
    if scores < 0 or scores > 100:
        return "Invalid scores"
    elif 50 <= scores < 90:
        return "Passable"
    elif 90 <= scores <= 100:
        return "Excellent"
    else:
        return "Bad"


def determine_random_score():
    scores = random.randint(0, 100)
    return scores


main()
