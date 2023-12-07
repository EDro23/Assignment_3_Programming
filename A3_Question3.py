#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:11:46 2023

@author: ethandrover

Bird Counter Program!

"""

# Import the pickle  module

import pickle

def display_title():
    """
    Display the program title.

    Returns
    -------
    None
    """
    print("Bird Counter program\n")
    print("Enter 'x' to exit\n")

def enter_bird(birds):
    """
    Enter bird sightings and update the count.

    Parameters
    ----------
    birds : dict
        Dictionary to store bird sightings.

    Returns
    -------
    None
    """
    while True:
        bird_name = input("Enter name of bird: ").title()
        if bird_name.lower() == 'x':
            break  # Exit the loop if 'x' is entered
        else:
            birds[bird_name] = birds.get(bird_name, 0) + 1

def write_to_pickle(birds):
    """
    Write bird sightings to a pickle file.

    Parameters
    ----------
    birds : dict
        Dictionary containing bird sightings.

    Returns
    -------
    None
    """
    with open('Birds_spotted.pkl', 'wb') as pickle_file:
        pickle.dump(birds, pickle_file)

def read_from_pickle():
    """
    Read bird sightings from a pickle file.

    Returns
    -------
    dict
        Dictionary containing bird sightings.
    """
    try:
        with open('Birds_spotted.pkl', 'rb') as pickle_file:
            return pickle.load(pickle_file)
    except FileNotFoundError:
        # print("File Birds_spotted.pkl not found. Creating a new one.") # This is not needed.
        return {}

def display_bird_counts(birds):
    """
    Display bird counts in a formatted table.

    Parameters
    ----------
    birds : dict
        Dictionary containing bird sightings.

    Returns
    -------
    None
    """
    spacer = (30 * '=')
    spacer2 = ' '
    spacer3 = (5 * '=')
    print("\nName\t\t\t\t\t\t\t Count")
    print(spacer + spacer2 + spacer3)
    sorted_birds = sorted(birds.keys())
    for bird in sorted_birds:
        count = birds.get(bird, 0)
        print(f"{bird}:{' ' * (30 - len(bird))}{count}")

def main():
    """
    Main function for running the bird counter program.

    Returns
    -------
    None
    """
    birds = read_from_pickle()
    display_title()
    enter_bird(birds)
    write_to_pickle(birds)
    display_bird_counts(birds)

if __name__ == '__main__':
    main()
