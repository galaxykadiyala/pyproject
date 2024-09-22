print('''
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|
''')
print("Welcome to the Treasure Island!")
print("All you have to do is find the treasure.")
input1 = input('Type left of right to move further: ').lower()
if input1 == "left":
    input2 = input('You have come to a lake. '
                   'There is an island in the middle of the lake. '
                   'Type "wait" to wait for the boat. '
                   'Type "swim" to swim across. ').lower()
    if input2 == "wait":
        input3 = input('You have reached the island. '
                       'Which door would you want to enter? '
                       'Type "red" or "blue" or "yellow" ').lower()
        if input3 == "yellow":
            print("You've found the treasure. You win!")
        elif input3 == "red":
            print("Fire!!! Game over!")
        elif input3 == "blue":
            print("Water!! Game over")
        else:
            print("Damn! Game over!")
    else:
        print("Oh no! Game over!")
else:
    print("Oops! Game over!")