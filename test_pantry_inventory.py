import csv
import pytest
import os
from pantry_inventory import get_inventory_items, add_item_file

FOOD_ITEM_INDEX = 0
QUANTITY_ITEM_INDEX = 1
EXPIRE_DATE_INDEX = 2

def test_add_item_file():
    """ Verify that the add_item_file function works correctly."""

    # Sample lists and file
    file_name = "inventory2.csv"
    list_1 = [
        ['Eggs',6,'10/02/2022'],
        ['Olive oil',2,'09/30/2022'],
        ['Cocoa powder',10,'12/25/2022'],
        ['Pasta',2,'10/31/2022'],
        ['Potato chips',10,'11/01/2022']
        ]
    list_2 = []

    # Call the add_item_file function to
    # add the values from list_1 to inventory2.csv file
    add_item_file(file_name,list_1)

    # Read the contents of the inventory2.csv file
    # and add them to list_2
    with open(file_name, "rt") as file_list:
        read_file = csv.reader(file_list)

        for item in read_file:
            food = item[FOOD_ITEM_INDEX]
            quantity = item[QUANTITY_ITEM_INDEX]
            expire = item[EXPIRE_DATE_INDEX]

            list_2.append([food, int(quantity), expire])

    # Delete the inventory2.csv file  
    os.remove(file_name)

    # Verify that add_item_file correctly added the values to inventory2.csv
    assert list_1 == list_2
    
def test_get_inventory_items():
    """ Verify that the add_item_file function works correctly."""

    # Sample lists and file
    file_name = "inventory2.csv"
    list = [
        ['Cereal',3,'01/02/2022'],
        ['Flour',3,'01/05/2023'],
        ['Milk',1,'02/05/2022'],
        ['Bread',2,'02/06/2022'],
        ['Sugar',1,'01/02/2023'],
     ]
    
    header = "Item,Quantity,ExpiryDate"
    
    # Write the header and values of compound list to inventory2.csv
    with open(file_name, "wt", newline="") as file_list:
        write_file = csv.writer(file_list)
        write_file.writerow([header])
        
        for item in list:
            food = item[FOOD_ITEM_INDEX]
            quantity = item[QUANTITY_ITEM_INDEX]
            expire = item[EXPIRE_DATE_INDEX]

            write_file.writerow([food, int(quantity), expire])
    
    # Call the get_inventory_items to get the values 
    # in the inventory2.csv
    get_inv_list = get_inventory_items(file_name)

    # Delete the inventory2.csv
    os.remove(file_name)

    # Verify that get_inventory_items got the file correctly
    assert list == get_inv_list
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])