# ask user for name
name = input('Please enter your name:')
# Open file in users name and writes name to it
name_file = open(name, 'w')
print(name, file=name_file)
name_file.close()

# Open file in users name and reads
name_file = open(name, 'r')
users_name = name_file.readline()
# Prints what was in the first line of file
print('Your name is {}'.format(users_name))
name_file.close()

# Open numbers and read first 2 lines
numbers_file = (open('numbers.txt', 'r'))
number_1 = int(numbers_file.readline())
number_2 = int(numbers_file.readline())
print(number_1 + number_2)
numbers_file.close()

# file has n amount of lines and add them together
n_file = open('numbers.txt', 'r')
total = 0
for line in n_file:
    number = int(line)
    total += number
print(total)
n_file.close()
