"""
File: pokemon.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: The program takes a file name as input and retrieves 
    the data from that file. It then formats the Pokemon data 
    into a Pokedex, calculates the averages for each statistic, 
    and allows the user to input specific statistics names to 
    retrieve the Pokemon type with the highest average for that 
    statistic. The program continues to prompt the user for input 
    until they provide an empty input.
"""

def get_data(file_name):
    """
    This function reads data from a file and returns 
    a dictionary with data labels and statistics.
    Args:
        file_name: the name of the file to be read
    Returns:
        a dictionary with data labels and statistics 
        from the file
    """
    f = open(file_name, 'r')
    headers = f.readline().strip('\n').split(',')
    data = f.readlines()
    f.close()
    return {"Data Labels": headers, "stats": data }

def format_pokedex(data):
    """
    This function formats the data from a pokedex and 
    returns a dictionary of pokemon stats.
    Args:
        data: the data from the csv file
    Returns:
        a dictionary of pokemon stats
    """
    pokedex = {}
    headers = data['Data Labels']
    for data_line in data['stats']:
        add_pokemon_to_dict(pokedex, data_line, headers)
    return pokedex

def add_pokemon_to_dict(pokedex, pokemon_line, headers):
    """
    This function adds a pokemon to a pokedex dictionary.
    Args:
        pokedex: the dictionary where pokemon are added to
        pokemon_line: a line of data containing 
        information about a pokemon
        headers: a list of headers for the data columns
    Returns:
        the updated pokedex dictionary with the new pokemon 
        added to its corresponding type.
    """
    pokemon_values = pokemon_line.strip('\n').split(',')
    pokemon_name = pokemon_values[1]
    pokemon_type = pokemon_values[2]
    if pokemon_type not in pokedex:
        pokedex[pokemon_type] = {}
    type_dict = {}
    # Do not include the properties at these indices in the dataset
    excluded_indices = {0, 1, 2, 3, 11, 12} 
    for i in range(len(pokemon_values)):
        if i not in excluded_indices:
            type_dict[headers[i]] = pokemon_values[i]
    pokedex[pokemon_type][pokemon_name] = type_dict
    return pokedex

def get_averages(pokedex):
    """
    This function calculates the average stats 
    for each type of pokemon in a pokedex.
    Args:
        pokedex: a dictionary containing pokemon 
        types and their respective stats
    Returns:
        a dictionary containing the average stats 
        for each type of pokemon in the pokedex
    """
    averages = {}
    for pokemon_type, type_collection in pokedex.items():
        averages[pokemon_type] = {}
        for pokemon in type_collection:
            for stat_name, stat_value in type_collection[pokemon].items():
                if stat_value.isnumeric():
                    if stat_name not in averages[pokemon_type]:
                        averages[pokemon_type][stat_name] = int(stat_value)
                    else:
                        averages[pokemon_type][stat_name] += int(stat_value)
        for stat_name, stat_values in averages[pokemon_type].items():
            num_values = len(type_collection)     
            averages[pokemon_type][stat_name] = stat_values / num_values
    return averages

def get_max_average(averages, stat_name):
    """
    This function returns the maximum average stat value and 
    corresponding Pokemon type for a given stat.
    Args:
        averages: a dictionary with Pokemon types as keys 
        and average stat values as values
        stat_name: a string representing the desired stat 
        to find the maximum average for
    Returns:
        a tuple with the maximum average stat value and a 
        list of corresponding Pokemon types
    """
    # convert user input to data column header
    stat_map = {
        'total': 'Total',
        'hp': 'HP',
        'attack': 'Attack',
        'defense': 'Defense',
        'specialattack': 'Sp. Atk',
        'specialdefense': 'Sp. Def',
        'speed': 'Speed'
    }
    stat_key = stat_map[stat_name.lower()]
    type_and_stat = {}
    max_stat_value = 0
    for pokemon_type, stat_value in averages.items():
        current_stat = stat_value[stat_key]
        if current_stat > max_stat_value:
            type_and_stat = {current_stat: [pokemon_type]}
            max_stat_value = current_stat
        elif current_stat == max_stat_value:
            type_and_stat[max_stat_value].append(pokemon_type)
    
    return sorted(type_and_stat.items())[-1]

def main():
    file_name = input()
    data = get_data(file_name)
    pokedex = format_pokedex(data)
    averages = get_averages(pokedex)
    user_continue = True
    while user_continue:
        user_input = input('')
        if user_input == '':
            # end the loop on an empty input
            user_continue = False
        elif user_input.lower() in [
            'total', 'hp', 'attack', 
            'defense', 'specialattack', 
            'specialdefense', 'speed'
            ]:
            max_avg = get_max_average(averages, user_input)
            for stat_type in sorted(max_avg[1]):
                print("{}: {}".format(stat_type, max_avg[0]))
        else:
            # ignore the query
            pass 
main()