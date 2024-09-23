random_numbers = [180, 130, 66, 77, 87, 76, 56, 98, 66, 76, 76, 170, 289, 230, 0, 1865]

# in built
print(set(random_numbers))

# without in built
unique_numbers = []

for number in random_numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)