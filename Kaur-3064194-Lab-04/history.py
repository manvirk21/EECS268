from linkedlist import LinkedList


class Web:  # Creating a Web class that will be responsible for actually performing all the commands
    def __init__(self):
        self.arrow = ' <=='
        self.history = LinkedList()
        self.command = ""
        self.num = -1

    def navigate(self, url):  # Navigate will insert the url at the correct spot.
        self.num += 1
        while self.num < self.history.len():
            self.history.remove(self.history.len() - 1)
        try:
            self.history.insert(self.num, url)
        except:
            raise RuntimeError('Invalid Insertion')

    def back(self):  # Back will change the index the arrow is pointing to by -1 if possible
        if self.num > 0:
            self.num -= 1
        else:
            self.num = 0

    def forward(self):  # Forward will change the index the arrow is pointing to by + 1 if possible
        if self.num < self.history.len() - 1:
            self.num += 1
        else:
            self.num = self.history.len() - 1

    def view(self):  # View allows the whole list to be looked at in a nicely formatted manner
        print("Oldest \n=========== \n")
        for i in range(0, self.history.len()):
            print_hist = self.history.get_entry(i)
            if i == self.num:
                print(print_hist + self.arrow)
            else:
                print(print_hist)
        print("\n=========== \nNewest \n")
