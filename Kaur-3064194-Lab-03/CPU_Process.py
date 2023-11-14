from setup import Stack
from setup import Queue


class CPU:  # creates a CPU scheduler class
    def __init__(self):
        self.queue = Queue()

    def start(self, name):  # A process is added to the queue
        self.queue.enqueue(Process(name))

    def call(self, function_name):
        # The process at the front of the queue gets CPU time and the function is put on the call stack for that
        # process. Then the process goes to the back of the line.
        try:
            self.queue.peek_front().entry.add(function_name)
            print(self.queue.peek_front().entry.process_name, "calls", function_name)
            temp = self.queue.dequeue()
            self.queue.enqueue(temp)
        except AttributeError as a:
            pass

    def returning(self):
        # The process at the front of the queue has the function at the top of the call stack return. It gets put at
        # the back of the queue unless its main returns in which case it is removed.
        temp_process = self.queue.dequeue()
        temp_function = temp_process.return_stack()
        if temp_process.empty():
            print(temp_process.process_name, "returns from main")
            print(temp_process.process_name, "process has ended")
        else:
            self.queue.enqueue(temp_process)


class Process:  # creates a Process class
    def __init__(self, name):
        self.process_name = name
        self.call_stack = Stack()
        self.call_stack.push("main")

    def add(self, function_name):
        # Adds a function to the top of the call stack
        self.call_stack.push(function_name)

    def return_stack(self):
        # Removes the top function in the stack
        return self.call_stack.pop()

    def empty(self):
        # Checks if queue is empty
        return self.call_stack.is_empty()
