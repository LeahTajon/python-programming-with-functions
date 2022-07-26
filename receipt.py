"""
File: receipt.py
Author: Leah Tajon

Problem Statement:
A local grocery store subscribes to an online service that enables its
customers to order groceries online. After a customer completes an order,
the online service sends a CSV file that contains the customer's requests
to the grocery store. The store needs you to write a program that reads the
CSV file and prints to the terminal window a receipt that lists the purchased
items and shows the subtotal, the sales tax amount, and the total.
"""
import csv
from datetime import datetime

# Indexes of some of the columns 
# in the products.csv file.
PROD_NUM_INDEX = 0
PROD_NAME_INDEX = 1
PROD_PRICE_INDEX = 2

# Index of quantity column
# in the request.csv
PRODUCT_INDEX = 0
QUANTITY_INDEX = 1

def main():
    try:
        # Print the store name at the top of the receipt
        store = "Tajon Mini Mart"
        print()
        print("===============================================")
        print(f"            Welcome to {store}")
        print("===============================================")
        print()

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        datetime_data = datetime.now()

        # Read the contents of the products.csv into a 
        # compound dictionary named products_dict. Use
        # the product numbers as the keys in the dictionary.
        products_dict = read_dict("products.csv", PROD_NUM_INDEX)
        
        # Open a file named request.csv and store a reference
        # to the opened file in a variable named requests_file
        filename = 'request.csv'
        with open(filename, 'rt') as requests_file:

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(requests_file)
        
            # The first row of the CSV file contains column
            # headings so this statement skips the first row
            # of the CSV file.
            next(reader)

            items = 0
            total = 0
            subtotal = 0
            discount = 0

            # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # If the current row is not blank, add the
                # data from the current to the dictionary.
                if len(row_list) != 0:
                    product = row_list[PRODUCT_INDEX]
                    # Convert the str type of quantity to int
                    quantity = int(row_list[QUANTITY_INDEX]) 

                    prod_info = products_dict[product]
                    prod_name = prod_info[PROD_NAME_INDEX]
                    # Convert the str type of price to float
                    prod_price = float(prod_info[PROD_PRICE_INDEX])

                    # Print the list of ordered items. 
                    print(f'{prod_name}: {quantity} @ {prod_price}')

                    # Sum the number of ordered items
                    items += quantity

                    # ------------ STRETCH CHALLENGE -------------------
                    # Write code to discount the product prices by 10% if today
                    # is Tuesday or Wednesday

                    today = datetime_data.strftime("%A")
                    if today.lower() == "tuesday" or today.lower() == "wednesday":
                        
                        # Compute the amount of the items bought
                        amount = prod_price * quantity
                        # Sum the subtotal due        
                        subtotal += amount
                        # Compute the discount amount
                        discount = subtotal * 0.1
                        # Compute the subtotal with discount amount
                        total_discount = subtotal - discount
                        # Compute the sales tax
                        tax = total_discount * .06
                        # Compute the total amount due
                        total = total_discount + tax
                        
                    
                    else:
                        # Compute the amount of the items bought
                        amount = prod_price * quantity
                        # Sum the subtotal due        
                        subtotal += amount
                        # Compute the sales tax
                        tax = subtotal * .06
                        # Compute the total amount due
                        total = subtotal + tax

            # Print the number of numbered items, subtotal due,
            # sales tax amount, and total amount due
            print(f'\nNumber of Items: {items}')
            print(f'Subtotal: ${subtotal:.2f}')
            print(f'Discount Amount: -${discount: .2f}')
            print(f'Sales Tax: ${tax:.2f}')
            print(f'Total: ${total:.2f}')

        # Print a thank you message
        print("_______________________________________________")
        print(f'\nThank you for shopping at {store}')
        # Print the current day of the week and the current time.
        print(f'{datetime_data:%a %b %d %I:%M:%S %Y}')
        print("===============================================")
        
    except FileNotFoundError as not_found_err:
        print(f"\nError: missing file")
        print(f"{not_found_err}")
    
    except PermissionError as perm_err:
        print(f"\nError: cannot read from {filename}"
                " because you don't have permission.")
    except KeyError as key_err:
        print(f"\nError: unknown Product ID in the {filename} file \n{product}")
    
def read_dict(filename, key_column_index):
    """ Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains the
        contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file
    dictionary = {}

    try:
        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        with open(filename, "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the csv file.
            next(reader)

            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # If the current row is not blank, add the
                # data from the current to the dictionary.
                if len(row_list) != 0:

                    # From the current row, retrieve the data
                    # from the column that contains the key.
                    key = row_list[key_column_index]

                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list

    except FileNotFoundError as not_found_err:
        print(f"\nError: missing file")
        print(f"{not_found_err}")

    except PermissionError as perm_err:
        print(f"\nError: cannot read from {filename}"
                " because you don't have permission.")

    except KeyError as key_err:
        print(f"\nError: unknown Product ID in the {filename} file \n{key}")

    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()
