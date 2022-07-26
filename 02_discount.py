
"""
File: 02_discount.py
Author: Leah Tajon

Purpose:
Improve your understanding of calling built-in Python functions
and calling functions and methods that are in a standard Python module.

Assignment:
Work to write a Python program that gets a customer's subtotal as input and
gets the current day of the week from your computer's operating system. Your
program must not ask the user to enter the day of the week. Instead, it must get
the day of the week from your computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your 
program must subtract 10% from the subtotal. Your program must then compute
the total amount due by adding sales tax of 6% to the subtotal. Your program
must print the discount amount if applicable, the sales tax amount, and the
total amount due.
"""
from datetime import datetime

# Your program asks the user for the subtotal but does not ask
# the user for the day of the week. Your program gets the day
# of the week from your computer's operating system.
today = datetime.now()
subtotal = float(input('\nPlease enter the subtotal: $'))

# Your program correctly computes and prints the discount
# amount if applicable.
if today.weekday() == 1 or today.weekday() == 2:
    if subtotal >= 50:
        discount = subtotal *.10
        total_discount = subtotal - discount
        sales_tax = total_discount * 0.06
        total = total_discount + sales_tax
    
        # Your program correctly computes and prints
        # the sales tax amount and the total amount due.
        print(f'\nDiscount amount: ${discount:.2f}')
        print(f'Sales tax amount: ${sales_tax:.2f}')
        print(f'Total: ${total:.2f}\n')
    elif subtotal < 50:
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f'\nSales tax amount: ${sales_tax:.2f}')
        print(f'Total: ${total:.2f}\n')
else:
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax

    print(f'\nSales tax amount: ${sales_tax:.2f}')
    print(f'Total: ${total:.2f}\n')
    





