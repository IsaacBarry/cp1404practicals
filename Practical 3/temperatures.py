"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Temp convert function"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius():
    """Convert fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit:"))
    # celsius = 5 / 9 * (fahrenheit - 32)
    return 5/9 * (fahrenheit - 32)


def celsius_to_fahrenheit():
    """Convert celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    return celsius * 9.0/5 + 32


main()
