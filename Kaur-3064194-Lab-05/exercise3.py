"""
Author: Manvir Kaur
KUID: 3064194
Date: 03/25/2022
Lab: lab05
Last modified: 03/31/2022
Purpose: Calculating Fibonacci Numbers
"""


def ith(f):  # Conducts the function to see what the value of Fibonacci number will be for the given f.
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return ith(f - 1) + ith(f - 2)


def verify(num, prev1num, prev2num):  # Conducts the verify function to make sure the number is in Fibonacci numbers.
    if num == 0:
        return True
    elif num == 1:
        return True
    else:
        current_num = prev1num + prev2num
        if current_num == num:
            return True
        elif current_num > num:
            return False
        else:
            return verify(num, current_num, prev1num)


def main():  # Deals with the user input and correct output.
    info = input("Enter mode and value: ")
    info = info.split(" ")
    value = int(info[1])
    if value < 0:
        print("Invalid Input")
    elif info[0] == "-i":
        print(ith(value))
    elif info[0] == "-v":
        ver = verify(value, 1, 0)
        if ver:
            print(value, "is in the sequence.")
        else:
            print(value, "is not in the sequence.")


main()
