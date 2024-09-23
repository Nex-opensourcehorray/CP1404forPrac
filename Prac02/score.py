"""
CP1404/CP5632 - Practical 02
Determine score status with functions
"""
import random


def main():
    input_scores = float(input("Please input the number:"))
    while input_scores < 0 or input_scores > 100:
        print("Invalid scores!")
        input_scores = float(input("Please input the number:"))
    output_grade = determine_score(input_scores)
    print(f"Your score is: {input_scores}")
    print(f"Your grade is: {output_grade}")

    generate_scores = determine_random_score()
    generate_evaluate = determine_score(generate_scores)
    print(f"Your generate score is: {generate_scores}")
    print(f"Your generate grade is: {generate_evaluate}")


def determine_score(scores):
    if scores >= 50:
        return "Passable"
    elif scores >= 90:
        return "Excellent"
    else:
        return "Bad"


def determine_random_score():
    scores = random.randint(0, 100)
    return scores


main()
