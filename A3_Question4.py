# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:39:35 2023

@author: ethan.drover
"""

def read_world_cup_data():
    with open('World_cup_champions.txt', 'r') as file:
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
    sorted_countries = sorted(world_cup_data.items())
    divider = ("=")
    print("\nFIFA World Cup Winners\n")
    print("Country\t\t\tWins  Years")
    print(f'{divider*7}\t\t\t{divider*4}  {divider*5}')

    # most_wins_country = None
    # most_wins = 0

    for country, data in sorted_countries:
        wins = data['Wins']
        years = ', '.join(data['Years'])
        print("{:<15} {:<5} {:<15}".format(country, wins, years))

        # if wins > most_wins:
        #     most_wins = wins
        #     most_wins_country = country

   # print("\nThe country with the most championships is:", most_wins_country)

if __name__ == "__main__":
    file_path = "world_cup_champions.txt"
    world_cup_data = read_world_cup_data()
    display_most_successful_country(world_cup_data)