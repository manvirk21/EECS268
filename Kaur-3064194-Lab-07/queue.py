from time import process_time_ns  # importing nanosecond processing
from setup import Queue  # importing the queue class

q_file = open('queue.txt', 'w')  # creating a file


def nanosec_to_sec(ns):  # converting nanoseconds to seconds
    BILLION = 1000000000
    return ns / BILLION


print("Beginning the timing code...")
num_iterations = 1000  # one thousand
while num_iterations <= 100000:
    queue = Queue()  # creating a queue object
    start_time = process_time_ns()  # starting to note the time
    for i in range(num_iterations):  # iterations to add each number
        queue.enqueue(i)
    end_time = process_time_ns()  # ending noting the time

    start_time = process_time_ns()
    queue.enqueue(1)
    end_time = process_time_ns()

    print("Total time in ns: ", end_time - start_time)
    print("Total time in sec: ", nanosec_to_sec(end_time - start_time))
    q_file.write(str(num_iterations)+'\t'+str(nanosec_to_sec(end_time-start_time))+'\n')  # writing into the file
    num_iterations += 1000
q_file.close()
