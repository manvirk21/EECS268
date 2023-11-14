from time import process_time_ns  # importing nanosecond processing
from linkedlist import LinkedList  # importing the linkedlist class

file3 = open('file3.txt', 'w')  # creating a file


def nanosec_to_sec(ns):  # converting nanoseconds to seconds
    BILLION = 1000000000
    return ns / BILLION


print("Beginning the timing code...")
num_iterations = 1000  # one thousand
while num_iterations <= 100000:
    linkedlist = LinkedList()  # creating a linkedlist object
    for i in range(num_iterations):  # iterations to add each number
        linkedlist.insert(i, i)
    start_time = process_time_ns()  # starting to note the time
    for i in range(num_iterations):
        print(linkedlist.get_entry(i))
    end_time = process_time_ns()  # ending noting the time

    print("Total time in ns: ", end_time - start_time)
    print("Total time in sec: ", nanosec_to_sec(end_time - start_time))
    file3.write(str(num_iterations)+'\t'+str(nanosec_to_sec(end_time-start_time))+'\n')  # writing into the file
    num_iterations += 1000
file3.close()
