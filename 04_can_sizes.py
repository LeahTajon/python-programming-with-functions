"""
File: 04_can_sizes.py
Author: Leah Tajon, Immanuel Nggiku, Emmanuel Odonkor

Purpose: Strengthen your understanding of user-defined functions,
parameters, arguments, and local variable scope by writing a program
that has three or more functions.

Assignment: Write a program that computes and prints the storage efficiency
for each of the following 12 steel cans sizes. Then visually examine the output
answer this question, "Which can size has the highest storage efficiency?"
"""


"""To calculate the storage efficiency of different can sizes given their radius and height in arrays."""
import math

name = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z' \
        '#8Z short', '#10', '#211', '#300', '#303']
radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

def main():
    """ Compute and print the storage efficiency.
    
    Parameters: None
    Return: None 
    """
    print()
    for x in range(len(name)): 
        can_name = name[x]
        can_radius = radius[x]
        can_height = height[x]

        vol = compute_volume(can_radius, can_height)
        surface_area = compute_surface_area(can_radius, can_height)

        storage_efficiency = vol / surface_area

        print(f'{can_name}\t{storage_efficiency:.2f}')
    print()

def compute_volume(radius, height):
    """ Compute and return the volume of a cylinder.
    
    Parameters:
    radius - radius of the cylinder
    height - height of the cylinder

    Return: the volume of the cylinder
    """

    vol = math.pi * radius ** 2 * height
    return vol

def compute_surface_area(radius, height):
    """ Compute and return the surface area of a cylinder.
    
    Parameters:
    radius - radius of the cylinder
    height - height of the cylinder

    Return: the surface area of the cylinder
    """

    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Call the main function to display the values in the terminal window
main()
