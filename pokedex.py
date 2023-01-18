# pokedex
# Showing pokemon details and happennings in the terminal
from time import sleep
import pyfiglet as pfg
from sys import stdout
import os


def clear_screen():
    # Clear screen to avoid distraction
    os.system('cls||clear')
    # Use the FigletFont class to create a Beautiful Header
    print(pfg.figlet_format('Pokemon Prediction Game',
                            font="slant",
                            justify="left",
                            width=150
                            ))

# Delay printing
def delay_print(s):
    # print one character at a time
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(0.05)

# Serve as the battle Board
def pokemon_battle_board(poke1, poke2):
    # Display pokemon ability
    pokedex(poke1)
    print()
    pokedex(poke2)

# Display Info of the Pokemon
def pokedex(pokemon):
    print("Pokemon Name:", pokemon.name)
    health_percentage =  pokemon.hp/pokemon.original_hp * 100
    health = int(health_percentage) * "="
    print(f"Pokemon HP: {int(pokemon.hp)}            HP Bar: {health}")
    print("Pokemon Type:", pokemon.type)
    print("Pokemon Weakness:", pokemon.weakness)
    print("Pokemon Abilities:")

    # Showing Abilities with (dp: Damage Power)
    numbering = 1
    for i,c in enumerate(pokemon.ability):
        if "dp" in c:
            ability = c["name"].strip()
            dp = c["dp"]
            a_type = c["type"].strip()
            print(f"{numbering}. {ability} ", end="")
            print(f"DP: {dp} ", end="")
            print(f"Type: {a_type}")
            numbering += 1
        else:
            continue