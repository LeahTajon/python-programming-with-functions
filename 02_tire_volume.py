"""
File: 02_tire_volume.py
Author: Leah Tajon

Purpose:
Prove that you can write a Python program that calls functions
and methods to get the current date and to append values to a text file.

Assignment:
The previous lesson's prove milestone required you to write program named
tire_volume.py that computes the approximate volume of air inside a tire.
Add code near the end of that program that does the following:

    1. Gets the current date from the computer's operating system
    2. Opens a text file named volumes.txt for appending
    3. Appends to the end of the volumes.txt file one line of text 
        that contains the following values:
        a. current date
        b. width of the tire
        c. aspect ratio of the tire
        d. diameter of the wheel
        e. volume of the tire
"""
# Import the datetime library to get the current date and time for this program
# Also, import the math module
from datetime import datetime
import math
from re import S


# Get the datetime.date.today() method to get the current date
current_date =  datetime.now()

# Get the width, aspect ratio, and diameter of the tire as strings
input_1 = input('Enter the width of the tire in mm (ex 205): ')
input_2 = input('Enter the aspect ratio of the tire (ex 60): ')
input_3 = input('Enter the diameter of the wheel in inches (ex 15): ')

# Convert the strings that the user entered into float
width = float(input_1)
ratio = float(input_2)
diameter = float(input_3)

# Compute the volume of the tire
volume = math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000000

# Use an f-string to create and print a message for the user to see.
print(f"\nThe approximate volume is {volume:.2f} liters\n")

"""---------------STRETCH CHALLENGE-----------------"""

# Ask the user if he/she wants to buy tires with the dimension that he/she entered.
tire_order = input("Do you want to order the tire (y/n)? ")

# If the user answers "yes", the program will ask for his/her phone number and store it in the volumes.txt
# including the date, width, ratio, dimension, and volume.
# Open a text file in append mode then append the values into the file. 
if tire_order.lower() == 'y' or tire_order.lower() == 'yes':
    contact_num = input('Please enter your phone number (555-555-5555): ')
    
    with open("volumes.txt", "at") as volumes_file:
        print(f'{current_date: %Y-%m-%d}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}, {contact_num}', file=volumes_file)
    print('Thank you for shopping. Please come again!')

# If the user answers "no", the program will only store the date, width, ratio, dimension, and volume
# Append the text into the file in append mode then append the values into the file
elif tire_order.lower() == 'n' or tire_order.lower() == 'no':
    with open("volumes.txt", "at") as volumes_file:
        print(f'{current_date: %Y-%m-%d}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}', file=volumes_file)
    print('Thank your for coming. Please come again!')

# If the user enters a different value, an error message will appear
else:
    print('Please enter y or n only.')




