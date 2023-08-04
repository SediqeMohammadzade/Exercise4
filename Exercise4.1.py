import random

pc_number = random.randint(0,20)

for i in range(10):
    user_number = int(input("Enter your num:"))

    if user_number == pc_number:
        print(i)
        break
    if user_number < pc_number:
        print("add to your number")
    if user_number > pc_number:
        print("subtract from the number")