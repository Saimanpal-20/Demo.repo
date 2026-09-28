# Game of luck door 

import random

print("Welcome to door of luck")
print("You are in a room with one will hwlp you escape and may trap you ")

correct_door = random.randint(1,3)
user_choice = int(input("choose a door(1,2 or 3):"))

if user_choice == correct_door:
    print("Cogrates ! , you choose correct door")

elif user_choice == 1 or user_choice == 2 or user_choice == 3:
    print("Sorry ! Wrong dorr")

else:
    print("Invalid Door")

# for find comput choice 
print("Ccomputer choice", correct_door)