"""
Author: Manvir Kaur
KUID: 3064194
Date: 04/01/2022
Lab: lab06
Last modified: 04/15/2022
Purpose: Blob
"""


class Blob:  # creation of a Blob class
    def __init__(self, the_map, size_row, size_col, start_col, start_row):  # initialization of the Blob class
        self.the_map = the_map
        self.size_row = size_row
        self.size_col = size_col
        self.start_col = start_col
        self.start_row = start_row
        self.count = 0

    def walk_maze(self, row, col):  # function that will allow the blob to move around the map
        if self.the_map[row][col] != "@":  # checks the map at row and col then changes to B if it's a P or S
            if self.the_map[row][col] == "P":  # increases the count of people eaten by one
                self.count += 1
            self.the_map[row][col] = "B"
        if self.is_valid_move(row - 1, col):  # check up
            self.walk_maze(row - 1, col)
        if self.is_valid_move(row, col + 1):  # check right
            self.walk_maze(row, col + 1)
        if self.is_valid_move(row + 1, col):  # check down
            self.walk_maze(row + 1, col)
        if self.is_valid_move(row, col - 1):  # check left
            self.walk_maze(row, col - 1)
        else:
            if self.the_map[row][col] == "@":
                self.the_map[row][col] = "x"  # change @ to x to avoid an infinite loop
                for i in range(0, self.size_row):
                    for j in range(0, self.size_col):
                        if self.the_map[i][j] == "@":  # look through the whole maze and teleport to unvisited @
                            self.walk_maze(i, j)

    def is_valid_move(self, row, col):  # determines if a move is valid
        if not (0 <= row < self.size_row and 0 <= col < self.size_col):
            return False
        if self.the_map[row][col] == "S":
            return True
        if self.the_map[row][col] == "@":
            return True
        if self.the_map[row][col] == "P":
            return True
        else:
            return False

    def output(self):  # format correctly to output to the console
        for i in range(0, self.size_row):
            for j in range(0, self.size_col):
                if self.the_map[i][j] == "x":
                    self.the_map[i][j] = "@"  # changes the x back to @
                print(self.the_map[i][j], end="")  # prints the entire map
            print()
        print("Total number of people eaten: ", self.count)  # prints the count of people eaten


def main():  # takes the input file and manipulates it to be usable
    file_input = input("Enter a blob file: ")
    filename = open(file_input, "r")
    list1 = []
    for i in filename:
        list1.append(i.strip())  # strips and appends the items in the file into a list
    size_row, size_col = list1[0].split()  # gets the first line which tells the size of the map
    start_row, start_col = list1[1].split()  # gets the second line which tells the starting position of the blob
    true_map = [list(line) for line in list1[2:]]  # makes each line a list of lists and rids the first two info lines
    size_row, size_col, start_col, start_row = int(size_row), int(size_col), int(start_col), int(start_row)
    blob = Blob(true_map, size_row, size_col, start_col, start_row)  # creating a blob object
    blob.walk_maze(start_row, start_col)  # walking the maze with the given information from the file
    blob.output()  # getting the output from the process


main()
