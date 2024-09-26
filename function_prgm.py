def greet():
    print("hello")
    print("how are you?")
    print("kbye!")

greet()
def life_in_weeks(current_age):
    total_age = 90
    current_age = int(input("What is your current age?"))
    time_left = (total_age - current_age) * 52
    print(f"You have {time_left} weeks left.")

life_in_weeks(current_age=0)