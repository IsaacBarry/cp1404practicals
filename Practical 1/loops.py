# Displays odd numbers between 1-20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10's from 0-100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Count down from 20-1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print n stars
number_stars = int(input("Number of stars:"))
for i in range(0, number_stars, 1):
    print(end='*')
print()

# Print n stars without loop
print('*' * number_stars)
