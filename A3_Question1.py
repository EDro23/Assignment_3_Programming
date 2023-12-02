#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:01:31 2023

@author: ethandrover
    
Tip Calculator Program!

"""

def title():
    """
    Title for the program

    Returns
    -------
    title

    """
    print("TIP CALCULATOR")

def tipping_calc():
    """
    

    Returns
    -------
    cost : float
        cost of the meal.
    tip : int
        the tip percentage.

    """
    while True:
        try:
            cost = float(input("Cost of meal: "))
            
            if cost <= 0:
                print("The cost must be above 0")
            else:
                tip_valid = True  # Flag to check the validity of the tip input
                while True:
                    try:
                        tip = int(input("Tip percent: "))
                        if tip < 0:
                            print("Tip percent must be a positive integer")
                            tip_valid = False  # Set the flag to False for an invalid tip input
                        else:
                            tip_valid = True  # Set the flag to True for a valid tip input
                            break  # Exit the inner loop for tip input
                    except ValueError:
                        print("Tip percent must be a valid integer. Please try again.")
                        tip_valid = False  # Set the flag to False for an invalid tip input
                if tip_valid:
                    return cost, tip
        except ValueError:
            print("Must be valid decimal number. Please try again.")

def output(cost, tip):
    """
    

    Parameters
    ----------
    cost : float
        Cost of meal can be decimal number
    tip : int
        The tip for meal, this will only be an even integer.

    Returns
    -------
    Total amount with tip percent added.

    """
    tip_percent = tip / 100
    tip_amount = cost * tip_percent
    total = cost + tip_amount
    print(f"Cost of the meal: {cost}")
    print(f"Tip percent:\t\t {tip}%")
    print(f"Tip amount:\t\t {tip_amount:.2f}")
    print(f"Total amount:\t {total:.2f}")

def main():
    """
    Main function for the program.

    Returns
    -------
    None.

    """
    title()
    print()
    cost, tip = tipping_calc()
    print()
    output(cost, tip)


if __name__ == '__main__':
    main()