# Pokemon
# By: Ely

# ----------------------------- OOP Programming -------------------------------------------
# This is just a getter class
class Pokemon:
    def __init__(self, name, hp, type, weakness, ability):
        self._name = name
        self._hp = hp
        self._type = type
        self._weakness = weakness
        self._ability = ability
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp
    
    @property
    def type(self):
        return self._type
    
    @property
    def weakness(self):
        return self._weakness
    
    @property
    def ability(self):
        return self._ability

# Main Program
def main():
    # pm1 = Pokemon()
    pass

# Run the main function
main()

# Excluder
if __name__ == "__main__":
    pass