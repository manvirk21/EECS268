from executive import Executive

# The main function will handle the user interactions and call Executive to run.
def main():
    try:
        file_name = input("Enter the name of the input file: ")
        filename = open(file_name, "r")
        my_exec = Executive(filename)
        my_exec.run()
    except:
        print("Invalid input. Try again! \n")


if __name__ == "__main__":
    main()
