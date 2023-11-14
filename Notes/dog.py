#dog.py

from animal import Animal

class Dog(Animal):
    def __init__ (self):

        #call Animal's init
        super().__init__(self) #or Animal.__init__(self)

        self. breed = "NOT SET"
        print("You made a Dog")

    def do_trick(self):
        print("Dog doing amazing trick!")

    def sleep(self):
        super().sleep()
        print("Ruf. roof. rooooof. rof")
        print("*kick* *kick*")
        print("Ruf. roof. rooooof. rof")
        print("SUDDENLY STARTLED")
