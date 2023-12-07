#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:12:32 2023

@author: ethandrover

World Cup Data Program!

"""

def read_world_cup_data(file_path="World_cup_champions.txt"):
    """
    

    Parameters
    ----------
    file_path : txt file, optional
        The file path we need to read. The default is "World_cup_champions.txt".

    Returns
    -------
    world_cup_data : txt file
        

    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    world_cup_data = {}
    for line in lines[1:]:  # Skip the header line
        year, country, coach, captain = [info.strip() for info in line.split(',')]
        if country not in world_cup_data:
            world_cup_data[country] = {'Wins': 0, 'Years': []}
        world_cup_data[country]['Wins'] += 1
        world_cup_data[country]['Years'].append(year)

    return world_cup_data

def display_most_successful_country(world_cup_data):
    """
    

    Parameters
    ----------
    world_cup_data : Txt
        a dict containing information about the world up data.

    Returns
    -------
    A display of the FIFA world cup winners in alphabetical order, showing the end user\
        how much each country has won and in which years.

    """
    sorted_countries = sorted(world_cup_data.items())
    divider = "="
    print("\nFIFA World Cup Winners\n")
    print("Country\t\t\tWins  Years")
    print(f'{divider*7}\t\t\t{divider*4}  {divider*5}')

    for country, data in sorted_countries:
        wins = data['Wins']
        years = ', '.join(data['Years'])
        print(f"{country:<16} {wins:<5} {years:<15}")

def main():
    """
    The main function for running the program.

    Returns
    -------
    None.

    """
    file_path = "World_cup_champions.txt"
    world_cup_data = read_world_cup_data(file_path)
    display_most_successful_country(world_cup_data)

if __name__ == "__main__":
    main()