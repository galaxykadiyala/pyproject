random_numbers = [180, 130, 66, 77, 87, 76, 56, 98, 66, 76, 76, 170, 289, 230, 0, 1865]

# in-built function
print(max(random_numbers))

# without in-built
max_number = 0
for number in random_numbers:
    if number > max_number:
        max_number = number
print(max_number)