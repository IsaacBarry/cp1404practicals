# Ask User for password and print * for length of password

min_length = 3


def main():
    # Uses functions to get password and print *
    password = get_password(min_length)
    print_asterisks(password)


def get_password(minimum_length):
    # Gets password
    password = input("Please enter a password with a minimum length of {}:".format(minimum_length))
    # Checks length of password
    while len(password) < 3:
        password = input('Please enter a valid password with a length of {}:'.format(minimum_length))
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
