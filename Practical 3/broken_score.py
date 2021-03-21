"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Gets users score"""
    score = float(input("Enter score: "))
    result = score_check(score)
    print(result)


def score_check(score):
    """Determines result"""
    if 0 > score or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    elif score <= 100:
        return "Excellent"


main()
