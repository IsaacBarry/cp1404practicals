
numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]
# 3
numbers[-1]
# 2
numbers[3]
# 1
numbers[:-1]
# 3 1 4 1 5 9
numbers[3:4]
# 1 5
5 in numbers
# true
7 in numbers
# false
"3" in numbers
# false
numbers + [6, 5, 3]
# 3 1 4 1 5 9 2 6 5 3

# Change first number to 'ten'
numbers[0] = 'ten'
# change last number to 1
numbers[-1] = 1
# get all numbers beside first 2
numbers[2:]
# check if 9 in numbers
9 in numbers
