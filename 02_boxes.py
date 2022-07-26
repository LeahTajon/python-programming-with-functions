"""
File: 02_boxes.py
Author: Leah Tajon

Purpose:
Check your understanding of calling built-in Python functions and
functions that are in a standard Python module.

Assignment:
A manufacturing company needs a program that will help its employees pack manufactured
items into boxes for shipping. Write a Python program that asks the user for two integers:

    1. the number of manufactured items
    2. the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This
must be a whole number. Note that the last box may be packed with fewer items than the other
boxes.
"""
# Import math module
import math

# Get the number of items and number of items per box from the user
num_of_items = int(input("\nEnter the number of items: "))
num_per_box = int(input("Enter the number of items per box: "))

# Compute the number of boxes by dividing number of items by the number of items per box
num_of_box = num_of_items / num_per_box
# Use math.ceil method to round off the number
box = math.ceil(num_of_box)

# Display the result
print(f"\nFor {num_of_items} items, packing {num_per_box} items in each box, you will need {box} boxes.\n")




