import random

pc_number=random.randint(1,10)

print("Welcome to guess the number")
user_number=int(input("pick a number from 1 to 10: "))

while user_number < 1 or user_number>10:
    user_number = int(input("Error. Pick a number from 1 to 10: "))

if user_number == pc_number:
    print("That's correct!")


else:
    print("That's incorrect! the winning number was: {}".format(pc_number))