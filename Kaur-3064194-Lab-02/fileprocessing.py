"""
Author: Manvir Kaur
KUID: 3064194
Date: 02/05/2022
Lab: lab02
Last modified:02/11/2022
Purpose: Processing Moby Dick
"""


def clean_word(word):
    # This function will remove the unwanted symbols that can be seen below and return a clean word.
    word = word.lower()
    word = word.strip()
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace(",", "")
    word = word.replace("|", "")
    word = word.replace(".", "")
    word = word.replace("--", "")
    word = word.replace('"', "")
    word = word.strip(" ' ' ")
    return word


def build_count(text):
    # This will create a dictionary of the words with how many times they appear in the text file.
    count_dict = {}
    text = text.split()
    for word in text:
        word = clean_word(word)
        if word in count_dict.keys():
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return count_dict


def unique_words(word_counts):
    # This will make a list of the words that appear only once in the file
    unique = []
    for word, count in word_counts.items():
        if count == 1:
            unique.append(word)
    return unique


def main():
    # The main function will combine and process everything
    try:
        word_data_file = open("word_data.txt", "w")  # A word_data file will be created
        unique_words_file = open("unique_words.txt", "w")  # A unique_words file will be created
        message = "Welcome to the word counter!"
        print(message.center(50, '='))
        file = input("Enter a file name: ")
        input_file = open(file, "r")  # opens the file the user gave
        print(f"The file {file} has been processed.")

        new_dict = build_count(input_file.read())
        for key, value in new_dict.items():
            word_data_file.write(key + ": " + str(value) + "\n")
        '''This will take the input file and list the count of all the words using the build_count function and format 
        the output nicely.'''

        new_list = unique_words(new_dict)
        for value in new_list:
            unique_words_file.write(value)
            unique_words_file.write("\n")
        '''This will take the input file and list the count of all the unique words using the unique_words function 
        # and format the output nicely. '''

        input_file.close()
        word_data_file.close()
        unique_words_file.close()
        print("Output stored in word_data.txt and unique_words.txt")
        print("Exiting...")
    except:
        print("Invalid Input!")


main()
