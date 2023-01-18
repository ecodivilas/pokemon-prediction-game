# Pokemon
# Command pip install requests
# By: Ely

import requests
from random import choice

pokemon_names = str()
pokemon_list = list()
pokemon = {}

# This will fetch all available pokemon names from the website pokedex
def get_all_pokemon():
    global pokemon_names

    URL = "https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php"
    get_all_pokemon = "all"
    PARAMS = {'pokedex':get_all_pokemon}

    # Sending get request and saving the response as response object
    res = requests.get(url = URL, params = PARAMS)

    # print(res) # 200 OK success
    if res.status_code == 200:
            pokemon_names = res.text # .strip()
            return pokemon_names
    else:
        print(res.status_code)

def random_select_pokemon(pokemon_names):
    # Container to the list of pokemon names
    global pokemon_list

    # Pokemon names put to list for accessability
    lines = pokemon_names.split('\n')
    values = [line.split(':')[1] for line in lines]
    for value in values:
        pokemon_list.append(value)
        
    # [print(line.split(':')[1]) for line in pokemon_names.split('\n')] # One liner code checker
    
    # Randomly select pokemon in the list
    pokemon = choice(pokemon_list)
    
    return pokemon

def get_pokemon(pokemon):
    URL = "https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php"
    PARAMS = {'pokemon':pokemon}

    # Sending get request and saving the response as response object
    res = requests.get(url = URL, params = PARAMS)

    # print(res) # 200 OK success
    if res.status_code == 200:
            # Return pokemon details in json format
            pokemon_details = res.json()
            return pokemon_details
    else:
        print(res.status_code)

def pokemon_picker():
    return pokemon

def get_list_of_pokemon():
    return pokemon_list

def main():
    global pokemon

    get_all_pokemon()
    pokemon_name = random_select_pokemon(pokemon_names)
    pokemon = get_pokemon(pokemon_name)

# Exclude printing when called outside the file
# print(__name__)
if __name__ == "__main__":
    main()
    print(pokemon)

else:
    main()