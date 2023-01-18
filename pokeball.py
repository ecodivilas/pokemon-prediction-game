# pokeball
# This file pull out pokemon randomly from a specific website
# Disclaimer: The website is not mine and for project demo purpose only

# I used here requests module to fetch data from the website
import requests
from random import choice

# Initiatialize global variables
pokemon_names = str()
pokemon_list = list()
pokemon_name = str()
pokemon_details = {}

# Pokemon Attributes
hp = None
type = None
name = None
shortname = None
ability = None
weakness = None

# Functional Programming 

# This will fetch all available pokemon names from the website pokedex
def get_all_pokemon():
    URL = "https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php"
    get_all_pokemon = "all"
    PARAMS = {'pokedex':get_all_pokemon}

    # Sending get request and saving the response as response object
    res = requests.get(url = URL, params = PARAMS)

    # print(res) # 200 OK success
    if res.status_code == 200:
            return res.text
    # print(res) # 400 Error failed
    else:
        pass
        
def random_select_pokemon(pokemon_names):
    # Container to the list of pokemon names
    global pokemon_list

    # Pokemon names put to list for accessability
    lines = pokemon_names.split('\n')
    values = [line.split(':')[1] for line in lines]
    for value in values:
        pokemon_list.append(value)
    
    # Randomly select pokemon in the list
    return choice(pokemon_list)

# Fetch Data of the Pokemon from the Web request
def get_pokemon(pokemon):
    URL = "https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php"
    PARAMS = {'pokemon':pokemon}
    
    # Sending get request and saving the response as response object
    res = requests.get(url = URL, params = PARAMS)

    # print(res) # 200 OK success
    if res.status_code == 200:
            # Assign the necessary data
            extract_pokemon_details(res.json())
            # Return pokemon details in json format
            return res.json()
    else:
        print(res.status_code)
    

# This will
def extract_pokemon_details(pokemon_details):
    # global pokemon_details
    global name
    global hp
    global type
    global weakness
    global ability
    global shortname

    # Assign all global variable with fetch data
    name = pokemon_details["name"]
    shortname = pokemon_details["shortname"]
    hp = pokemon_details["hp"]
    type = pokemon_details["info"]["type"]
    weakness = pokemon_details["info"]["weakness"]
    ability = pokemon_details["moves"]


def random_pokemon():
    # Make the global variables editable using global keyword
    global pokemon_names
    global pokemon_list
    global pokemon_name
    # Returns a dictionary
    global pokemon_details 

    # Pull out Pokemon Randomly
    pokemon_names = get_all_pokemon()
    pokemon_name = random_select_pokemon(pokemon_names)
    pokemon_details = get_pokemon(pokemon_name)

if __name__ == "__main__":
    pass
    # Start the whole program if run in this page
    # Randomized Pokemon Sample Calls for debugging
    # random_pokemon()

    # Hard Coded Pokemon
    # pokemon_details = get_pokemon('mr-mime')
