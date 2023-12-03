#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:11:46 2023

@author: ethandrover

Bird Counter Program!

"""
# Import the pickle module

import pickle

# List of default birds in a dict

birds = {'Red-Tailed Hawk': 0,
         'Black-Capped Chickadee': 0,
         'Killdeer': 0,
         'Snowy Plover': 0,
         'Western Gull': 0}


def title():
    """
    Title for the program when it starts

    Returns
    -------
    None.

    """
    print("Bird Counter program\n")
    print("Enter 'x' to exit\n")


def enter_bird(birds):
    """
    

    Parameters
    ----------
    birds : str
        checks if there is a bird within the birds and if there is it adds 1 to the counter.

    Returns
    -------
    None.

    """
    while True:
        bird = input("Enter name of bird: ").title()
        if bird.lower() == 'x':
            break  # Exit the loop if 'x' is entered
        elif bird in birds:
            # Increment the count for the entered bird to add to the pickle file
            birds[bird] += 1
        else:
            print("Invalid bird name. Try again.")


def write_pickle_file(birds):
    """
    

    Parameters
    ----------
    birds : str
        writes birds to a pickle file as a string.

    Returns
    -------
    None.

    """
    with open('Birds_spotted.pkl', 'wb') as bfh:
        pickle.dump(birds, bfh)


def read_pickle_file():
    """
    function for reading the pickle file

    Returns
    -------
    pickle
        Reads the pickle file so if the watcher exits it is saved to a file that can be read again.

    """
    # Try & Except block for reading the birds_spotted pickle file
    try:
        with open('Birds_spotted.pkl', 'rb') as rbfh:
            return pickle.load(rbfh)
    except FileNotFoundError:
        print("File Birds_spotted.pkl not found. Creating a new one.")
        return {}


def main():
    """
    Main function for running the program

    Returns
    -------
    None.

    """
    birds = read_pickle_file()
    title()
    enter_bird(birds)
    write_pickle_file(birds)
    spacer = (30 * '=')
    spacer2 = ' '
    spacer3 = (5 * '=')
    print("\nName\t\t\t\t\t\t\t Count")
    print(spacer + spacer2 + spacer3)
    sorted_birds = sorted(birds.keys())
    # Print all birds with counts, including those with count 0
    for bird in sorted_birds:
        count = birds.get(bird, 0)
        print(f"{bird}:{' ' * (30 - len(bird))}{count}")


if __name__ == '__main__':
    main()
