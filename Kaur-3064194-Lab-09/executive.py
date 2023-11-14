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
    print("\n1. Search by id number \n2. Add new Pokemon \n3. Print all Pokemon \n4. Copy \n5. Remove \n6. Quit")


def main():
    choice = "0"
    count = 0
    while choice != "6":
        print_menu()
        choice = input("Simply enter the choice number: ")  # getting choice from user
        if choice == "1":  # searching for a Pokemon using the ID num and printing it
            id = int(input("Please enter the Pokemon's ID num: "))
            try:
                print("Searching...\n")
                returned = bst.search(id)
                print("The US name is", returned.US_name, "and the Japanese name is", returned.jpn_name)
            except RuntimeError as e:
                print(e)
        elif choice == "2":  # adding a new pokemon into the bst
            entry = []
            USname = input("Enter the US name: ")
            num = int(input("Enter the ID number: "))
            JPN_name = input("Enter the Japanese name: ")
            entry.append(USname)
            entry.append(num)
            entry.append(JPN_name)
            pokemon2 = Pokemon(entry[0], entry[1], entry[2])
            try:
                print("Adding new Pokemon...")
                bst.add(pokemon2)
                print("Pokemon added successfully!")
            except RuntimeError as e:
                print(e)
        elif choice == "3":  # printing all pokemon in the desired traversal order
            order = input("What traversal order do you want? (in/pre/post): ")
            if order == "in":
                bst.visit_in_order(print_poke)
            elif order == "pre":
                bst.visit_pre(print_poke)
            elif order == "post":
                bst.visit_post(print_poke)
        elif choice == "4":  # making a copy of the existing bst if possible
            count += 1
            if count <= 1:
                new = bst.clone_tree()
                print("Tree successfully copied!")
            else:
                print("\nSORRY, YOU CAN ONLY COPY ONCE!")
            while choice != "6":  # Starting the process again to incorporate both new and original bst
                print_menu()
                tree = input("What tree would you like to use? (original/new): ")  # allowing user to choose desired tree
                choice = input("Simply enter the choice number: ")  # getting choice from user
                if tree == "original":  # Options for the original tree
                    if choice == "1":  # searching for a Pokemon using the ID num and printing it
                        id = int(input("Please enter the Pokemon's ID num: "))
                        try:
                            print("Searching...\n")
                            returned = bst.search(id)
                            print("The US name is", returned.US_name, "and the Japanese name is", returned.jpn_name)
                        except RuntimeError as e:
                            print(e)
                    elif choice == "2":  # adding a new pokemon into the bst
                        entry = []
                        USname = input("Enter the US name: ")
                        num = int(input("Enter the ID number: "))
                        JPN_name = input("Enter the Japanese name: ")
                        entry.append(USname)
                        entry.append(num)
                        entry.append(JPN_name)
                        pokemon2 = Pokemon(entry[0], entry[1], entry[2])
                        try:
                            print("Adding new Pokemon...")
                            bst.add(pokemon2)
                            print("Pokemon added successfully!")
                        except RuntimeError as e:
                            print(e)
                    elif choice == "3":  # printing all pokemon in the desired traversal order
                        order = input("What traversal order do you want? (in/pre/post): ")
                        if order == "in":
                            bst.visit_in_order(print_poke)
                        elif order == "pre":
                            bst.visit_pre(print_poke)
                        elif order == "post":
                            bst.visit_post(print_poke)
                    elif choice == "4":  # making a copy of the existing bst if possible
                        count += 1
                        if count <= 1:
                            new = bst.clone_tree()
                            print("Tree successfully copied!")
                        else:
                            print("\nSORRY, YOU CAN ONLY COPY ONCE!")
                    elif choice == "5":  # removing an entry given the id number
                        entry = int(input("What would you like to remove? "))
                        try:
                            print("Removing...")
                            bst.delete(entry)
                        except RuntimeError as e:
                            print(e)
                if tree == "new":  # Choices for the copy/new bst
                    if choice == "1":  # searching for a Pokemon using the ID num and printing it
                        id = int(input("Please enter the Pokemon's ID num: "))
                        try:
                            print("Searching...\n")
                            returned = new.search(id)
                            print("The US name is", returned.US_name, "and the Japanese name is", returned.jpn_name)
                        except RuntimeError as e:
                            print(e)
                    elif choice == "2":  # adding a new pokemon into the bst
                        entry = []
                        USname = input("Enter the US name: ")
                        num = int(input("Enter the ID number: "))
                        JPN_name = input("Enter the Japanese name: ")
                        entry.append(USname)
                        entry.append(num)
                        entry.append(JPN_name)
                        pokemon2 = Pokemon(entry[0], entry[1], entry[2])
                        try:
                            print("Adding new Pokemon...")
                            new.add(pokemon2)
                            print("Pokemon added successfully!")
                        except RuntimeError as e:
                            print(e)
                    elif choice == "3":  # printing all pokemon in the desired traversal order
                        order = input("What traversal order do you want? (in/pre/post): ")
                        if order == "in":
                            new.visit_in_order(print_poke)
                        elif order == "pre":
                            new.visit_pre(print_poke)
                        elif order == "post":
                            new.visit_post(print_poke)
                    elif choice == "4":  # making a copy of the existing bst if possible
                        count += 1
                        if count <= 1:
                            other = new.clone_tree()
                            print("Tree successfully copied!")
                        else:
                            print("\nSORRY, YOU CAN ONLY COPY ONCE!")
                    elif choice == "5":  # removing an entry given the id number
                        entry = int(input("What would you like to remove? "))
                        try:
                            print("Removing...")
                            new.delete(entry)
                        except RuntimeError as e:
                            print(e)
                else:
                    print("Invalid Choice!!")
        elif choice == "5":  # removing an entry given the id number
            entry = int(input("What would you like to remove? "))
            try:
                print("Removing...")
                bst.delete(entry)
            except RuntimeError as e:
                print(e)
    print("Quiting...")


main()
