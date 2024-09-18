print("Welcome to Pizza deliveries!")
size = input("What size of pizza do you want? S, M or L? ")
pepperoni = input("Do you want pepperoni topping? Y or N? ")
cheese = input("Do you want cheese? Y or N? ")
bill_amount = 0

if size == "S":
    bill_amount = 15
    if pepperoni == "Y":
        bill_amount += 2
    if cheese == "Y":
        bill_amount += 1
    print(f"Total bill amount is {bill_amount}")
elif size == "M":
    bill_amount = 20
    if pepperoni == "Y":
        bill_amount += 2
    if cheese == "Y":
        bill_amount += 1
    print(f"Total bill amount is {bill_amount}")
elif size == "L":
    bill_amount = 25
    if pepperoni == "Y":
        bill_amount += 2
    if cheese == "Y":
        bill_amount += 1
    print(f"Total bill amount is {bill_amount}")
else:
    print("Please choose the right options")
