import random

randomlist = []

i = int(input("How many numbers do you want?"))
min = int(input("Enter the minimum number for your list:"))
max = int(input("Enter the maximum number for your list:"))
randomlist = random.sample(range(min,max), i)
print(randomlist)