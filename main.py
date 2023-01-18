# Pokemon

from pokemon import Pokemon # Pokemon Class 
from random import choice

# Link external files
import pokeball as pb      
import pokedex as pd   
import pokeGUI as pg

# Exclude printing when called outside the file
if __name__ == "__main__":
    # Game Logic
    # Create an instance of Random Pokemon from Pokeball
    pb.random_pokemon()
    # Sample specific input: pb.get_pokemon('Alakazam')
    pm1 = Pokemon(pb.name, pb.shortname, pb.hp, pb.type, pb.weakness, pb.ability)
    pb.random_pokemon()
    # Sample specific input: pb.get_pokemon('Omanyte')
    pm2 = Pokemon(pb.name, pb.shortname, pb.hp, pb.type, pb.weakness, pb.ability)

    # Pop pop the GUI
    pg.GUI(pm1, pm2)

def start_game(pm1, pm2, chosen_pokemon):

    # Battle Starts Here
    change_turn = 1
    first_turn = choice([pm1, pm2])
    second_turn = pm2 if pm1 == first_turn else pm1
    change_turn = 1

    # Loop while both pokemon have HP: Health Points
    while pm1.hp > 0 and pm2.hp > 0:

        pd.clear_screen()
        # This will show the current status of each pokemon every turn
        pd.pokemon_battle_board(pm1, pm2)
        if change_turn == 1:
            first_turn.attack(first_turn, second_turn)
            change_turn = 0
        else:
            second_turn.attack(second_turn, first_turn)
            change_turn = 1
    
    # Print the result of the game
    pd.clear_screen()
    pd.pokemon_battle_board(pm1, pm2)

    # Print if you win or lose
    if chosen_pokemon._win == True:
        print("\nYou Win!")
    else:
        print("\nYou Lose!")

    exit()

    