"""
File: 03_fuel_usage.py
Author: Leah Tajon

Purpose: Check your understanding of writing your own functions with
parameters and then calling those functions with arguments.

Assignment:
Write a Python program that asks the user for three numbers:
    1. A starting odometer value in miles
    2. An ending odometer value in miles
    3. An amount of fuel in gallons
Your program must calculate and print fuel efficiency in both miles per gallon and
liters per 100 kilometers. Your program must have three functions named as follows:
    1. main
    2. miles_per_gallon
    3. lp100k_from_mpg
"""

def main():
    # Get an odometer value in U.S. miles from the user.
    start = float(input('Enter the first odometer reading (miles): '))
    # Get another odometer value in U.S. miles from the user.
    end = float(input('Enter the second odometer reading (miles): '))
    # Get a fuel amount in U.S. gallons from the user.
    fuel = float(input('Enter the amount of fuel used (gallons): '))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    gallon = miles_per_gallon(start, end, fuel)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100k kilometer
    liters = lp100k_from_mpg(gallon)

    # Display the results for the user to see.
    # pass
    print(f"{gallon:.2f} miles per gallon")
    print(f"{liters:.2f} liters per 100 kilometers")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """ Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    miles_gallon = abs(end_miles - start_miles) / amount_gallons
    
    return miles_gallon

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    liter_km = 235.215 / mpg

    return liter_km

# Call the main function so that
# this program will start executing.
main()