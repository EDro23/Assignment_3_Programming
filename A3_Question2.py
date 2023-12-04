#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:15:10 2023

@author: ethandrover

Game Stats Program!

"""
# List of players in a nests dictionary.

players = {'Kailey':{'wins':27,'losses':5,'ties':2},
           'Mike':{'wins':17,'losses':3,'ties':5},
           'Michael':{'wins':31,'losses':11,'ties':1},
           'Arun':{'wins':52,'losses':1,'ties':3}}

def title():
    """
    Title for the program.

    Returns
    -------
    None.

    """
    print("Game Stats program")
    
def all_plyrs(): 
    """
    Lists all the players on the list when the program starts.

    Returns
    -------
    None.

    """
    print("ALL PLAYERS:")
    plyrs = list(players.keys())
    plyrs.sort() # Sorts the players
    print_string = ""
    for x in plyrs:
        print_string += x + "\n" # New line after each player is listed
    print(print_string)

def view_stats():
    """
    Function for viewing stats of individual players.

    Returns
    -------
    None.

    """
    while True:
        name = input("Enter a player name: ").capitalize() # Makes first letter capital if user fails to do so
        if name in players:
            plyr_wins = players[name]['wins']
            plyr_loss = players[name]['losses']
            plyr_tie = players[name]['ties']
            print(f"Wins:\t{plyr_wins}\nLosses:\t{plyr_loss}\nTies:\t{plyr_tie}")
            print()
            contin = input("Continue? (y/n): ").lower() # Continue loop
            print()
            if contin == 'y':
                continue
            else:
                print("Bye!")
                break
                
        else:
            print(f"There is no player named {name}\n")
        
 
def main():
    """
    Main program for running the program.

    Returns
    -------
    None.

    """
    title()
    print()
    all_plyrs()
    view_stats()
    
if __name__ == '__main__':
    main()
