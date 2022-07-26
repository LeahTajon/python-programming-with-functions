"""
File: provinces.py
Author: Leah Tajon

Purpose:
Check your understanding of text files and lists by writing a program
that reads the contents of a text file into a list and then changes some
of the values in the list.
"""
def main():

    provinces_list = read_list("provinces.txt")

    print(provinces_list)
    print()
    
    # Remove the first element from the list
    provinces_list.pop(0)
    print(provinces_list)
    print()

    # Remove the last element from the list
    provinces_list.pop()
    print(provinces_list)
    print()
    
    # Replace all occurences of "AB" in the list with "Alberta"
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'
    print(provinces_list)
    print()

    # Count the number of elements that are "Alberta" and print that number.
    count = provinces_list.count("Alberta")
    print(f'\nAlberta occurs {count} times in the modified list.')


def read_list(filename):
    text_list = []

    with open(filename, "rt") as text_file:
        for text in text_file:
            clean_line = text.strip()
            text_list.append(clean_line)
    
    return text_list

# Call main to start this program.
if __name__ == "__main__":
    main()
