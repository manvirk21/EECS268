from CPU_Process import CPU
from CPU_Process import Process


class Executive:
    # Creates a class responsible for executing the CPU Process
    def __init__(self, name):
        self.name = name
        self.cpu = CPU()

    def run(self, filename):
        # Opens the file and executes the commands
        file = open(filename, "r")
        for line in file:
            word = line.strip().split()
            if word[0] == "START":
                try:
                    self.cpu.start(word[1])
                    print(word[1], "added to queue")
                except RuntimeError as e:
                    print(e)
            elif word[0] == "CALL":
                try:
                    self.cpu.call(word[1])
                except RuntimeError as e:
                    print("No process to call")
                    print(e)
            elif word[0] == "RETURN":
                try:
                    self.cpu.returning()
                except RuntimeError as e:
                    print(e)
            else:
                raise RuntimeError('Invalid command')


def main():
    # Takes in a file and creates an executive object to run the file
    filename = input("Enter a file: ")
    executive = Executive(filename)
    executive.run(filename)


main()
