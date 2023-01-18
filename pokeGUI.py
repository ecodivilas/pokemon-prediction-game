from tkinter import messagebox
import tkinter as tk

# Import from external file
import fetch_png_pic as fpp
import main as m

class GUI:

    def __init__(self, pm1, pm2):
        # Setting up a Tkinter GUI
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Pokemon Tournament Betting")
        self.root.iconbitmap("src/pokemon.ico")

        # Initialization of variables inside this class
        self.pm1 = pm1
        self.pm2 = pm2
        self.first_pokemon_chosen = 0
        self.second_pokemon_chosen = 0
        self.pokemon_chosen = ""
        self.pokemon_winner = ""
        self.poke1_name = pm1._short_name
        self.poke2_name = pm2._short_name

        # Getting the photo in byte
        self.photo1 = fpp.get_pokemon_png(self.poke1_name)
        self.photo2 = fpp.get_pokemon_png(self.poke2_name)

        # Set banner of two pokemon that will fight
        self.vs_banner = tk.Label(self.root,
            text=f"{self.poke1_name.capitalize()} \
VS {self.poke2_name.capitalize()}",
                 font=("Arial", 18))
        self.vs_banner.pack(padx=20, pady=10)
        
        # Set the frame to organize objects in grid form
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        # First pokemon picture with button
        self.poke_pic1 = tk.Button(self.buttonframe, image = self.photo1,
                                   command=self.first_pokemon_chose)
        self.poke_pic1.grid(row=0, column=0, sticky=tk.W+tk.E)

        # Second pokemon picture with button
        self.poke_pic2 = tk.Button(self.buttonframe, image = self.photo2,
                                   command=self.second_pokemon_chose)
        self.poke_pic2.grid(row=0, column=1, sticky=tk.W+tk.E)
        
        # Button to Initiate the battle
        self.start_battle_btn = tk.Button(self.buttonframe,
                                          text="Start Battle!",
                                          font=('Arial', 18),
                                          command=self.start_battle)
        self.start_battle_btn.grid(row=1, columnspan=2, sticky=tk.W+tk.E)

        # This pack the buttonframe and fill the entire rows with objects
        self.buttonframe.pack(fill='x')

        # Instruction to choose pokemon
        self.inst_lbl = tk.Label(self.root,
            text="Choose your pokemon", font=("Arial", 12))
        self.inst_lbl.pack(padx=20, pady=2)
        
        # Waits for any events from the player
        self.root.mainloop()


    def start_battle(self):
        # Verify if the player chose his/her pokemon
        if self.pokemon_chosen != "":
            # Starts the pokemon battle
            m.start_game(self.pm1, self.pm2, self.pokemon_chosen)
        else:
            # Pops out when the player didn't chose a pokemon
            messagebox.showinfo(title="No Chosen Pokemon",
            message="Please choose your pokemon to start the game.")

    def first_pokemon_chose(self):
        # Assign flags to check if which pokemon is chosen
        self.first_pokemon_chosen = 1
        self.second_pokemon_chosen = 0
        self.pokemon_chosen = self.pm1
        # Change state of the button if clicked
        self.poke_pic1.config(bg = 'red')
        self.poke_pic2.config(bg = 'white')
    
    def second_pokemon_chose(self):
        # Assign flags to check if which pokemon is chosen
        self.first_pokemon_chosen = 0
        self.second_pokemon_chosen = 1
        self.pokemon_chosen = self.pm2
        # Change state of the button if clicked
        self.poke_pic1.config(bg = 'white')
        self.poke_pic2.config(bg = 'red')
    
    # # Pending
    # @property
    # def reveal_winner(self):
    #     return self.pokemon_winner

    # # Pending
    # @reveal_winner.setter
    # def reveal_winner(self, winner):
    #     self.pokemon_winner = winner
    #     self.start_battle_btn.config(text = 'Play Again?')
