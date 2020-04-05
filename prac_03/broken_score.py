"""
CP1404 - Week 3 Practical
Program to determine result based on numeric score
"""

import random


def main():
    user_score = get_score()
    print(calc_result(user_score))

    print("Random User Score:")
    random_score = random.randint(0, 101)
    print(random_score)
    print(calc_result(random_score))


def get_score():
    input_score = float(input("Enter Score: "))
    return input_score


def calc_result(score):
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


main()
