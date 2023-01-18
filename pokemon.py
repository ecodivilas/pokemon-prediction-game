# Pokemon
# By: Ely

from time import sleep
from random import choice

import pokedex as pd

# OOP Programming 

# This is just a getter class
class Pokemon:
    def __init__(self, name, short_name, hp, type, weakness, ability):
        self._name = name
        self._short_name = short_name
        self._hp = hp
        self._original_hp = hp
        self._type = type
        self._weakness = weakness
        self._ability = ability
        self._win = False
    
    @property
    def name(self):
        return self._name
    
    @property
    def short_name(self):
        return self._short_name

    @property
    def hp(self):
        return self._hp
    
    @property
    def original_hp(self):
        return self._original_hp
    
    @property
    def type(self):
        return self._type
    
    @property
    def weakness(self):
        return self._weakness
    
    @property
    def ability(self):
        return self._ability
    
    @hp.setter
    def hp(self, new_health):
        self._hp = new_health

    def attack(self, attacker, defender):

        while True:
            # Choose an attack from the list randomly
            attack = choice(attacker._ability)

            # Get the chosen ability w/ DP
            if "dp" in attack:
                attack_name = attack["name"]
                attack_type = attack["type"]
                attack_dp = attack["dp"]
                break
            else:
                continue

        # Have a delay anouncer
        pd.delay_print(f"\n{attacker._name} attacked \
{defender._name} with {attack_name}!")
        sleep(1)

        # Evaluate the attack of the attacker
        if attack_type == defender._weakness:
            pd.delay_print(" It was super effective!")
            defender._hp -= 1.5 * attack_dp
        else:
            pd.delay_print(" It was not very effective...")
            # Reduce defender's HP by the attack's damage points
            defender._hp -= attack_dp

        if defender._hp <= 0:
            defender._hp = 0
            defender._win = False
            attacker._win = True
            pd.delay_print("\n\n..." + defender._name + " fainted.")
            sleep(1)
            pd.delay_print("\n\n..." + attacker._name + " Won!")
            sleep(1)
            pd.delay_print("\n\n..." + attacker._name \
                + " Return ... Well Done! \n")
        else:
            pd.delay_print(f" {defender._name} \
has {int(defender._hp)} HP left\n\n")

# Excluder
if __name__ == "__main__":
    pass