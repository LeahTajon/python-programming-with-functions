import random

def main():
    # Creates a list
    numbers = [16.2, 75.1, 52.3]

    # Prints the number list
    print(f'{numbers}')

    # Calls the append_random_numbers function with
    # only one argument to add one number to numbers
    append_random_numbers(numbers)

    # Prints the numbers list
    print(f'{numbers}')

    # Calls the append_random_numbers function again with 
    # two arguments to add three numbers to numbers
    append_random_numbers(numbers, 3)

    # Prints the number list
    print(f'{numbers}')
    
def append_random_numbers(num_list, quantity = 1):
    """ Add and return random numbers to the list.
    
    Parameters:
        num_list -  is a list where the random numbers will be added to
        quantity - tells how many random numbers will be added in the list.
            It has a default value of 1.
    Return: nothing 
    """

    # This loop will iterates how many times this
    # function will add random numbers 
    for i in range(quantity):
        # Computes quantity pseudo random numbers
        # by calling the random.uniform function.
        num = random.uniform(1, 50)

        # Rounds the quantity pseudo random numbers
        # to one digit after the decimal.
        round_num = round(num, 1)

        # Appends the quantity pseudo random numbers
        # onto the end of the numb_list.
        num_list.append(round_num)

# At the bottom of your program, write an if statement
# that calls the main function.
if __name__ == "__main__":
    main()

