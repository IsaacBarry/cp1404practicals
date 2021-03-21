"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    if 0 > score or score > 100:
        print("Invalid Score")
    elif score < 50:
        print("Bad")
    elif score < 90:
        print("Pass")
    elif score <= 100:
        print("Excellent")


main()