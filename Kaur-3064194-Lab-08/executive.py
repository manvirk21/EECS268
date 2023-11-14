from pokemon import Pokemon
from bst import BST

bst = BST()  # creates BST class object

file_name = input("Enter a file: ")  # gets a file from the user
filename = open(file_name, "r")  # reads user file
for line in filename:  # formatting the file correctly and adding it to the bst
    word = line.strip().split()
    word[1] = int(word[1])
    pokemon = Pokemon(word[0], word[1], word[2])
    bst.add(pokemon)


def print_poke(obj):  # prints pokemon objects
    print(obj.US_name, obj.jpn_name, obj.id_num)


def print_menu():  # prints the menu
    print("\n1. Search by id number \n2. Add new Pokemon \n3. Print all Pokemon \n4. Quit")


def main():
    choice = 0
    while choice != 4:
        print_menu()
        choice = int(input("Simply enter the choice number: "))  # getting choice from user
        if choice == 1:  # searching for a Pokemon using the ID num and printing it
            id = int(input("Please enter the Pokemon's ID num: "))
            try:
                returned = bst.search(id)
                print(returned.US_name, returned.jpn_name, returned.id_num)
            except RuntimeError as e:
                print(e)
        elif choice == 2:  # adding a new pokemon into the bst
            entry = []
            USname = input("Enter the US name: ")
            num = int(input("Enter the ID number: "))
            JPN_name = input("Enter the Japanese name: ")
            entry.append(USname)
            entry.append(num)
            entry.append(JPN_name)
            pokemon2 = Pokemon(entry[0], entry[1], entry[2])
            try:
                bst.add(pokemon2)
            except RuntimeError as e:
                print(e)
        elif choice == 3:  # printing all pokemon in the desired treversal order
            order = input("What traversal order do you want? (in/pre/post): ")
            if order == "in":
                bst.visit_in_order(print_poke)
            elif order == "pre":
                bst.visit_pre(print_poke)
            elif order == "post":
                bst.visit_post(print_poke)


main()
