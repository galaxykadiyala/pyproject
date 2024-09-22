import random

friends = ["John", "Papa John", "Mama John", "Baby John"]

# logic 1
randomize = random.choice(friends)
print(randomize)

# logic 2
randomize1 = random.randint(0, 3)
print(friends[randomize1])