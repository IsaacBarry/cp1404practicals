
# Get number of items from user

num_items = int(input(" Number of items: "))
# Set price and i to be used in loop
price = 0
i = 0

# Get price of each item
while i < num_items:
    price_item = int(input("Price of item: "))
    # Add new item price to old
    price += price_item
    i += 1

# Prints number of items and total price
print("Total price for {} items is ${}".format(num_items, price))


c = 15 / 3 + 2 * 4
print(c)
