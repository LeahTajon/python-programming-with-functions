"""
File: pantry_inventory.py
Author: Leah Tajon

Purpose: Prove that you can write a significant Python program
that includes well organized functions and solves a real world problem.
"""
import csv
from datetime import datetime
from tabulate import tabulate

# These are the indexes of each
# element in the list
ITEM_INDEX = 0
QUANTITY_INDEX = 1
EXPIRY_DATE_INDEX = 2

def main():
    """ Shows the main options for the pantry inventory."""
    try:
        # Display main options 
        print()
        print("--------------------------------")
        print("    WELCOME PANTRY INVENTORY")
        print("----------------------------------")
        print()
        print("Available Options:")
        print()
        print("1 - Add Items To Inventory")
        print("2 - View Items To Inventory")
        print("3 - Track Items By Expiration Date")
        print("4 - Exit")
        print()

        # Continue to execute until condition is satisfied.
        while True:
            option = input("Choose an option: ")
            if option == '1':
                add_items_inventory()
                break
            elif option == '2':
                view_items()
                break
            elif option == '3':
                track_items()
                break
            elif option == '4':
                exit()         
    except (ValueError) as error:
        print(type(error).__name__, error, sep=": ")

def add_items_inventory():
    """ Gets the item name, quantity, and expiration date from the user. 
        Then, adds the values to the list. 

    Parameter: none
    Return: none    
    """

    try:
        
        file_csv = "inventory.csv"
        food_list = []

        print("--------------------------------------")
        print("         ADD ITEMS TO INVENTORY")
        print("--------------------------------------")
        print()
        print("Available Options:")
        print()
        print("1 - Add multiple items")
        print("2 - Add single item")
        print()

        # Continue to execute until condition is satisfied
        while True:
            option = input("Choose an option: ")
            if option in ['1', '2']:
                break
        
        # Option # 1: Add multiple items
        if option == '1':
            print()
            
            # Diplay user input
            while True:
                num_items = input("Enter the number of items to be added: ")
                if num_items.isdigit():
                    break
            num_items = int(num_items)

            for i in range(1, num_items + 1):
                while True:
                    print()
                    item_name = input("Item name: ")
                    if item_name != "":
                        break
                while True:
                    item_amount = input("Quantity: ")
                    if item_amount.isdigit():
                        break
                valid = False
                while not valid:
                    item_exp_date = input("Expiration Date (mm/dd/yyyy): ")
                    try:
                        item_date = datetime.strptime(item_exp_date, "%m/%d/%Y")
                        valid = True
                    except ValueError:
                        valid = False
                
                # Capitalize the first letter of a string
                item_name = item_name.capitalize()

                # Convert the type to integer
                item_amount = int(item_amount)
                
                # Add the input values to the list
                food_list.append([item_name, item_amount, item_exp_date])

            # Call a function to add the items in the file.
            add_item_file(file_csv, food_list)

            # Call a function that displays a message and asks the user
            # to return to the main menu
            return_to_main("Items have been added. ")

        # Option # 2: Add single item
        elif option == '2':
            print()

            # Display user input
            while True:
                food_name = input("Item name: ")
                if food_name != "":
                    break
            while True:
                food_amount = input("Quantity: ")
                if food_amount.isdigit():
                    break
            valid = False
            while not valid:
                food_expiry = input("Expiration Date (mm/dd/yyyy): ")
                try:
                    food_date = datetime.strptime(food_expiry, "%m/%d/%Y")
                    valid = True
                except ValueError:
                    valid = False
            
            # Capitalize the first letter of a string
            food_name = food_name.capitalize()

            # Add the input values to the list
            food_list.append([food_name, int(food_amount), food_expiry])
            
            # Call a function to add the items in the file.
            add_item_file(file_csv, food_list)

            # Call a function that displays a message and asks the user
            # to return to the main menu
            return_to_main("Item has been added. ")
          
    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ")

def add_item_file(file_name, file_list):
    """ Adds the items of the list in the csv file. 
    
    Parameter
        file_name: a csv file that will store the items from the list.
        file_list: a list that contains the data of inventory. 
            The values are in this format: [item name, quantity, expiration date]
    
    Return: nothing
    """

    try:
        # Write the values from the list to the csv file
        with open(file_name, "a", newline="") as inventory:
            file = csv.writer(inventory)

            for item in file_list:
                food = item[ITEM_INDEX]
                quantity = item[QUANTITY_INDEX]
                expire = item[EXPIRY_DATE_INDEX]

                file.writerow([food, int(quantity), expire])

    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ")

def view_items():
    """ Display viewing options and show the values in a table format.
    
    Parameter: None
    Return: nothing
    """
    try:
        
        file_csv = "inventory.csv"
        # Display a table that shows all the items in the file.
        print()
        print("-----------------------------------------")
        print("             VIEW INVENTORY")
        print("-----------------------------------------")
        print()
        
        # Call a function that gets a list of items from the inventory file. 
        inventory_items = get_inventory_items(file_csv)

        # Display the values in a table format
        col_names = ["Item", "Quantity", "Expiry Date"]
        print(tabulate(inventory_items, headers=col_names, tablefmt="grid"))
        print()

        # Diplay the options for viewing items.
        print("Available Options:")
        print()
        print("1 - Sort By Quantity")
        print("2 - Sort Alphabetically")
        print("3 - Back to Main Menu")
        print()
        while True:
            option = input("Choose an option: ")
            if option in ['1', '2', '3']:
                break

        if option == '1':
            sort_by_quantity()
        elif option == '2':
            sort_alphabetically()
        elif option == '3':
            main()
        
    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ")

def sort_by_quantity():
    """ Sort items by quantity from biggest to smallest. 
    
    Parameter: None
    Return: Nothing
    """

    try:
        file_csv = "inventory.csv"
        
        print("--------------------------------------------")
        print("             SORT BY QUANTITY")
        print("--------------------------------------------")
        
        # Call a function that gets a list of items from the inventory file. 
        inventory_list = get_inventory_items(file_csv)
        
        # Sort the items by quantity
        key_num = lambda inv_list: inv_list[QUANTITY_INDEX]
        sorted_list = sorted(inventory_list, key=key_num, reverse=True)

        # Display the sorted values in a table format
        col_names = ["Item", "Quantity", "Expiry Date"]
        print(tabulate(sorted_list, headers=col_names, tablefmt="grid"))

        # Call a function that displays a message and asks the user
        # to return to the main menu
        return_to_main("")

    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ")
   
def sort_alphabetically():
    """ Sort items alphabetically.
    
    Parameter: None
    Return: Nothing
    """
    try:

        file_csv = "inventory.csv"

        print("--------------------------------------------")
        print("             SORT ALPHABETICALLY")
        print("--------------------------------------------")

        # Call a function that gets a list of items from the inventory file.
        invetory_list = get_inventory_items(file_csv)

        # Sort items alphabetically
        key_num = lambda inv_list: inv_list[ITEM_INDEX]
        sorted_list = sorted(invetory_list, key=key_num)

        # Display the sorted values in a table format
        col_names = ["Item", "Quantity", "Expiry Date"]
        print(tabulate(sorted_list, headers=col_names, tablefmt="grid"))

        # Call a function that displays a message and asks the user
        # to return to the main menu
        return_to_main("")

    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ")

def get_inventory_items(file_name):
    """ Read the data from csv file into a list and return the list 
    that contain the values of inventory.
    
    Parameter
        file_name: the name of the csv file to read
    Return:
        inventory_list: a compound list of inventory items
    """
    try:
        # Create an empty list that will store 
        # the items from the csv file
        inventory_list = []

        # Open the csv file for reading and append
        # the values onto the end of the list.
        with open(file_name, "rt") as inventory:
            file = csv.reader(inventory)
            next(file)

            for item in file:
                item_name = item[ITEM_INDEX]
                item_amount = item[QUANTITY_INDEX]
                expire_date = item[EXPIRY_DATE_INDEX]

                inventory_list.append([item_name, int(item_amount), expire_date])
        
    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ") 

    # Return the list that contain the values of the inventory
    return inventory_list

def track_items():
    """ Display the track items options and show the items that are
    already expired or about to expire in a table format.
    
    Parameter: None
    Return: Nothing
    """
    try:
        file_csv = "inventory.csv"
        print("--------------------------------------------")
        print("             TRACK ITEMS")
        print("--------------------------------------------")
        print()
        print("Available Options:")
        print()
        print("1 - Track About To Expire Items")
        print("2 - Track Expired Items")
        print()

        
        # Continue to execute until condition is satisfied. 
        while True:
            option = input("Choose an option: ")
            if option in ['1', '2']:
                break
        
        # Option 1: Track About to Expire Items
        if option == '1':
            print()
            print("--------------------------------------------")
            print("             ITEMS ABOUT TO EXPIRE")
            print("--------------------------------------------")

            # Call function that track nearly expired items
            # in the inventory file and return a list
            inventory_list_1 = track_nearly_expired(file_csv)

            # Count the nearly expired items in the list
            count_list_1 = len(inventory_list_1)

            # Create a condition for nearly expired items. 
            # If the list is not empty, the items will be displayed.
            if count_list_1 != 0:
                col_names = ["Item", "Quantity", "Expiry Date", "No. of Days Left"]
                print(tabulate(inventory_list_1, headers=col_names, tablefmt="grid"))

                # Call a function to return to the main menu
                return_to_main("")
                print()
            
            # If the list has no values, a message will be displayed and call 
            # a function to return to the main menue.
            else:
                return_to_main("Items are up-to-date. ")
                print()
        
        # Option 2: Track already expired items.
        elif option == '2':
            print()
            print("--------------------------------------------")
            print("                EXPIRED ITEMS")
            print("--------------------------------------------")

            # Call function that track expired items
            # in the inventory file and return a list
            inventory_list_2 = track_expired_items(file_csv)

            # Count the nearly expired items in the list
            count_list_2 = len(inventory_list_2)

            # Create a condition for expired items. 
            # If the list is not empty, the items will be displayed.
            if count_list_2 != 0:
                col_names = ["Item", "Quantity", "Expiry Date", "No. of Days Left"]
                print(tabulate(inventory_list_2, headers=col_names, tablefmt="grid"))

                # Call a function to return to the main menu
                return_to_main("")
                print()
            
            # If the list has no values, a message will be displayed and call 
            # a function to return to the main menue.
            else:
                return_to_main("Items are up-to-date. ")
                print()

    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ") 


def track_nearly_expired(file_name):
    """ Read items in a file and returns a list of nearly expired items.
    
    Parameter
        file_name: name of the csv file to be read
    Return
        inventory_list: a compound list of inventory items
    """
    try:
        inventory_list = []

        # Opens a file to be read and appends the items that
        # are about to expire within 90 days to the list.
        with open(file_name, "r") as inventory:
            reader = csv.reader(inventory)
            next(reader)

            for item in reader:
                item_name = item[ITEM_INDEX]
                item_amount = item[QUANTITY_INDEX]
                expire_date = item[EXPIRY_DATE_INDEX]

                month = expire_date[0:2]
                day = expire_date[3:5]
                year = expire_date[6:]

                str_expire_date = f"{year}/{month}/{day}"
                current_date = datetime.today()

                exp_date = datetime.strptime(str_expire_date, "%Y/%m/%d")
                difference = (exp_date - current_date).days

                if difference <= 90 and difference >= 1:
                    inventory_list.append([item_name, int(item_amount), expire_date, difference])

    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ") 
    
    # Return the list that contains nearly expired items
    return inventory_list

def track_expired_items(file_name):
    """ Read items in a file and return items that are already expired.

    Parameter
        file_name: name of csv file to be read
    Return
        inventory_list: a compound list that contains expired items.
    """
    try:

        # 
        inventory_list = []

        # Open and read a file. Then, append the items that
        # are already expired to the list.
        with open (file_name, "r") as inventory:
            reader = csv.reader(inventory)
            next(reader)

            for item in reader:
                item_name = item[ITEM_INDEX]
                item_amount = item[QUANTITY_INDEX]
                expire_date = item[EXPIRY_DATE_INDEX]

                month = expire_date[0:2]
                day = expire_date[3:5]
                year = expire_date[6:]

                str_expire_date = f"{year}/{month}/{day}"
                current_date = datetime.today()

                exp_date = datetime.strptime(str_expire_date, "%Y/%m/%d")
                difference = (exp_date - current_date).days

                if difference <= 0:
                    inventory_list.append([item_name, item_amount, expire_date])

    except (PermissionError, FileNotFoundError, IndexError) as error:
        print(type(error).__name__, error, sep=": ")
    
    # Return the list that contains expired items.
    return inventory_list

def return_to_main(message):
    """ Display a message and give an option to return to the main menue.
    
    Parameter
        message: a string of message to be displayed
    Return: Nothing
    """

    # Continue to execute until condition is satisfied
    while True:
        print()
        back = input(f"{message}Press (M) to Return to Main Menu:  ").lower() if message != None else input("Press (M) to RETURN to the main menu: ").lower()
        if back == 'm':
            main()
            break

# Call main to start this program.
if __name__ == "__main__":
    main()