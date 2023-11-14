"""
Author: Manvir Kaur
KUID: 3064194
Date: 03/25/2022
Lab: lab05
Last modified: 03/25/2022
Purpose: Calculating the spread of the flu
"""


def outbreak(num):  # Recursive function figuring out the sick count for the given day.
    if num == 1:
        return 6
    elif num == 2:
        return 20
    elif num == 3:
        return 75
    else:
        return outbreak(num - 1) + outbreak(num - 2) + outbreak(num - 3)


# Prints the output and takes in the user input:
print("OUTBREAK!")
n = int(input("What day do you want a sick count for?: "))
if n > 0:
    print("Total people with flu:", outbreak(n))
else:
    print("Invalid day")
