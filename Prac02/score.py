"""
CP1404/CP5632 - Practical 02
Determine score status with functions
"""
import random


def main():
    """ The main function to decide your input score and grade & random generate score and grade."""
    input_scores = float(input("Please input the number:"))

    while input_scores < 0 or input_scores > 100:
        print("Invalid scores!")
        input_scores = float(input("Please input the number:"))

    output_grade = determine_grade(input_scores)
    print(f"Your score is: {input_scores}")
    print(f"Your grade is: {output_grade}")

    generate_scores = generate_random_score()
    generate_evaluate = determine_grade(generate_scores)
    print(f"Your generate score is: {generate_scores}")
    print(f"Your generate grade is: {generate_evaluate}")


def determine_grade(scores):
    """The function that determine your grade."""
    if scores >= 50:
        return "Passable"
    elif scores >= 90:
        return "Excellent"
    else:
        return "Bad"


def generate_random_score():
    """The function that generate the random score."""
    scores = random.randint(0, 100)
    return scores


main()
