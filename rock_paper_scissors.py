import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play Rock, Paper, Scissors!")
list1 = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
print(f"User chose:")
print(list1[user_input])
machine_input = random.randint(0, 2)
print(f"Machine chose:")
print(list1[machine_input])

# >=3 might not work as we have given a lost above and
# only 0,1,2,-1,-2,-3 are accepted
if user_input >= 3 or user_input < 0:
    print("Invalid input!!")
elif user_input == 0 and machine_input == 2:
    print("You win!")
elif machine_input > user_input:
    print("You lose!")
elif user_input == machine_input:
    print("Draw.")
elif machine_input == 0 and user_input == 2:
    print("You lose!")
elif user_input > machine_input:
    print("You win!")
else:
    print("Invalid input!!!")