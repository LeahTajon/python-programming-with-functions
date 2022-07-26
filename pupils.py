import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    filename = "pupils.csv"
    # Call the read_compound_list function to read the pupils.csv
    # file into a list named students_list.
    student_list = read_compound_list(filename)

    # # Write a lambda function that will extract the birthdate from a student.
    # extract_birthdate = lambda student: student[BIRTHDATE_INDEX]

    # # Write a call to the Python built-in sorted function that will sort
    # # the student_list by birthdate from oldest to youngest
    # sorted_list = sorted(student_list, key=extract_birthdate)

    # # Print the students_list by calling the print_list function.
    # new_list = print_list(sorted_list)
    # print(new_list)

    sorted_list = sort_by_month_day(student_list)
    new_list = print_list(sorted_list)
    print(new_list)

def sort_by_month_day(filename):
    def extract_month_day(student):
        birth_string = student[BIRTHDATE_INDEX]
        month_day = birth_string[5:]
        return month_day
    sorted_list = sorted(filename, key=extract_month_day)

    return sorted_list

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(student_list):
    for student in student_list:
        print(student)
    
    return student

main()



    
    
