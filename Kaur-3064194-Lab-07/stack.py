"""
Author: Manvir Kaur
KUID: 3064194
Date: 04/08/2022
Lab: lab07
Last modified:02/15/2022
Purpose: Time Complexity
"""

from time import process_time_ns  # importing nanosecond processing
from setup import Stack  # importing the stack class

s_file = open('stack.txt', 'w')  # creating a file


def nanosec_to_sec(ns):  # converting nanoseconds to seconds
    BILLION = 1000000000
    return ns / BILLION


print("Beginning the timing code...")
num_iterations = 1000  # one thousand
while num_iterations <= 100000:
    stack = Stack()  # creating a stack object
    for i in range(num_iterations):  # iterations to add each number
        stack.push(i)
    start_time = process_time_ns()  # starting to note the time
    stack.pop()
    end_time = process_time_ns()  # ending noting the time

    print("Total time in ns: ", end_time - start_time)
    print("Total time in sec: ", nanosec_to_sec(end_time - start_time))
    s_file.write(str(num_iterations)+'\t'+str(nanosec_to_sec(end_time-start_time))+'\n')  # writing to the file
    num_iterations += 1000
s_file.close()
