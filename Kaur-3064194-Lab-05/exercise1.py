"""
Author: Manvir Kaur
KUID: 3064194
Date: 03/25/2022
Lab: lab05
Last modified: 03/25/2022
Purpose: Recursive Power Function
"""


def power(base, p):  # Recursive function to do the math
    if p == 0:  # Base case of n^0
        return 1
    else:
        return base * power(base, p - 1)


exp = -1
while exp < 0:  # Makes sure exponent is a positive number
    num = int(input("Enter a base: "))
    exp = int(input("Enter a power: "))
    if exp <= -1:
        print("Sorry, your exponent must be zero or larger.")
print("Answer: ", power(num, exp))
