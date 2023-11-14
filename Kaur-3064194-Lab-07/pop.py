from time import process_time_ns  # importing nanosecond processing
from setup import Stack  # importing the stack class

pop_file = open('pop.txt', 'w')  # creating a file


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
    pop_file.write(str(num_iterations)+'\t'+str(nanosec_to_sec(end_time-start_time))+'\n')  # writing into the file
    num_iterations += 1000
pop_file.close()
