from history import Web


class Executive:  # Creating an Executive class to perform everything
    def __init__(self, file_name):
        self.browser = Web()
        self.file_name = file_name

    def run(self):  # The function responsible for managing the different commands given
        filename = open(self.file_name, "r")
        for i in filename:
            i = i.translate({ord(c): None for c in '\n'})
            self.browser.command = i
            self.browser.command = self.browser.command.split(" ")
            if self.browser.command[0] == "NAVIGATE":
                self.browser.navigate(self.browser.command[1])
            elif self.browser.command[0] == "HISTORY":
                self.browser.view()
            elif self.browser.command[0] == "BACK":
                self.browser.back()
            elif self.browser.command[0] == "FORWARD":
                self.browser.forward()
            else:
                raise RuntimeError("Invalid Input")


def main():  # Interacts with the user to get the file name
    file_name = input("Enter a file name: ")
    executive = Executive(file_name)
    executive.run()


main()


